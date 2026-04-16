import hashlib
import re
from typing import Any, Dict, List

import bcrypt


HEX_RE = re.compile(r"^[a-fA-F0-9]+$")


def _risk_for_algorithm(algo: str) -> Dict[str, str]:
    weak = {"md5", "sha1"}
    moderate = {"sha224", "sha256", "sha384", "sha512"}
    strong_password_hash = {"bcrypt"}

    if algo in weak:
        return {
            "level": "high",
            "message": f"{algo.upper()} is weak for password storage. Migrate to bcrypt/Argon2.",
        }
    if algo in moderate:
        return {
            "level": "medium",
            "message": f"{algo.upper()} is a fast hash. Prefer bcrypt/Argon2 for password hashing.",
        }
    if algo in strong_password_hash:
        return {
            "level": "low",
            "message": "bcrypt is suitable for password hashing when cost is tuned.",
        }
    return {"level": "unknown", "message": "Algorithm risk profile unavailable."}


def detect_hash_type(hash_value: str) -> Dict[str, Any]:
    value = hash_value.strip()
    candidates: List[Dict[str, Any]] = []

    if value.startswith("$2a$") or value.startswith("$2b$") or value.startswith("$2y$"):
        candidates.append(
            {
                "algorithm": "bcrypt",
                "confidence": 0.98,
                "reason": "Matches bcrypt modular crypt format prefix.",
                "risk": _risk_for_algorithm("bcrypt"),
            }
        )

    if HEX_RE.fullmatch(value):
        length_to_algo = {
            32: ("md5", 0.92),
            40: ("sha1", 0.92),
            56: ("sha224", 0.90),
            64: ("sha256", 0.92),
            96: ("sha384", 0.90),
            128: ("sha512", 0.92),
        }
        if len(value) in length_to_algo:
            algo, confidence = length_to_algo[len(value)]
            candidates.append(
                {
                    "algorithm": algo,
                    "confidence": confidence,
                    "reason": f"Hex digest length {len(value)} is typical for {algo.upper()}.",
                    "risk": _risk_for_algorithm(algo),
                }
            )

    candidates.sort(key=lambda x: x["confidence"], reverse=True)

    return {
        "input": value,
        "detected": len(candidates) > 0,
        "candidates": candidates,
        "recommendation": "Use bcrypt or Argon2 for password hashing; avoid fast general-purpose hashes.",
    }


def _verify_hex_digest(algo: str, hash_value: str, plaintext: str) -> bool:
    hasher = hashlib.new(algo)
    hasher.update(plaintext.encode("utf-8"))
    return hasher.hexdigest().lower() == hash_value.lower()


def verify_hash(hash_value: str, plaintext: str) -> Dict[str, Any]:
    detection = detect_hash_type(hash_value)
    candidates = detection.get("candidates", [])

    if not candidates:
        return {
            "verified": False,
            "algorithm": None,
            "message": "Could not determine supported hash type.",
            "detection": detection,
        }

    top = candidates[0]
    algo = top["algorithm"]

    try:
        if algo == "bcrypt":
            verified = bcrypt.checkpw(plaintext.encode("utf-8"), hash_value.encode("utf-8"))
        else:
            verified = _verify_hex_digest(algo, hash_value, plaintext)
    except Exception as exc:
        return {
            "verified": False,
            "algorithm": algo,
            "message": f"Verification failed: {exc}",
            "detection": detection,
        }

    return {
        "verified": bool(verified),
        "algorithm": algo,
        "message": "Plaintext matches hash." if verified else "Plaintext does not match hash.",
        "detection": detection,
    }
