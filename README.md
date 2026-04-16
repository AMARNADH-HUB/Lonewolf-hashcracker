# Lonewolf Hash Security Auditor

A modern web-based **hash security auditing** tool (safe scope) built with FastAPI.

> ⚠️ This project is for legitimate security testing and education only. It does **not** implement brute-force or unauthorized cracking workflows.

## Features

- Hash type detection (heuristics): `md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `bcrypt`
- Plaintext verification against known hash values
- Risk feedback for detected algorithm type
- Polished responsive Web UI
- Linux-friendly deployment
  - Docker Engine + Compose
  - Direct Python (`uvicorn`)

## Project Structure

```txt
.
├─ app/
│  ├─ __init__.py
│  ├─ hash_utils.py
│  └─ main.py
├─ static/
│  ├─ app.js
│  ├─ index.html
│  └─ styles.css
├─ docker-compose.yml
├─ Dockerfile
├─ requirements.txt
└─ README.md
```

## Run on Linux (without Docker)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Then open:

```txt
http://localhost:8000
```

If accessing from another device on same LAN:

```txt
http://<your-linux-ip>:8000
```

## Run on Linux (Docker Engine + Compose)

```bash
docker compose up --build -d
```

Open:

```txt
http://localhost:8000
```

Stop:

```bash
docker compose down
```

## API Endpoints

- `GET /` → Web UI
- `GET /health` → health check
- `POST /api/detect`
- `POST /api/verify`

### Example: Detect

```bash
curl -X POST http://localhost:8000/api/detect \
  -H "Content-Type: application/json" \
  -d '{"hash_value":"5d41402abc4b2a76b9719d911017c592"}'
```

### Example: Verify

```bash
curl -X POST http://localhost:8000/api/verify \
  -H "Content-Type: application/json" \
  -d '{"hash_value":"5d41402abc4b2a76b9719d911017c592","plaintext":"hello"}'
```

## Notes

- Heuristic detection is probabilistic, not cryptographic certainty.
- For password storage in production systems, prefer Argon2id or bcrypt with secure parameters.
