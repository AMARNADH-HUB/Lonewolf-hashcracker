# Lonewolf Hash Security Auditor
<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/ca9c47c9-2968-4a4e-9cdd-79d70616fbf2" />


Lonewolf Hash Security Auditor is a modern, Linux-ready web application for **safe hash analysis and verification**. It is designed for legitimate security auditing, password policy testing, and educational use.

> ⚠️ Ethical and legal use only.
> This project does **not** include brute-force modules, wordlist cracking, or unauthorized access features.

---

## Description

This tool helps you quickly inspect a hash string, estimate likely hash type, and test whether a known plaintext matches the given hash. It provides an easy-to-use Web UI with clean result cards and risk guidance, making it useful for internal security reviews and training labs.

Supported workflows:
- Identify likely algorithm using format/length heuristics
- Verify known plaintext against supported hashes
- Review risk level guidance for the detected algorithm

---

## Features

### Core Security Features
- **Hash type detection (heuristics)** for:
  - `MD5`
  - `SHA1`
  - `SHA224`
  - `SHA256`
  - `SHA384`
  - `SHA512`
  - `bcrypt`
- **Plaintext verification** against supported hash formats
- **Algorithm risk feedback** (high / medium / low) with recommendations

### Web UI Features
- Polished dark/glassmorphism style interface
- Responsive layout (desktop + mobile)
- Dedicated tabs:
  - **Detect Hash**
  - **Verify Plaintext**
- API health indicator on top panel
- Structured result cards with confidence and risk badges

### Deployment Features
- Linux-friendly architecture
- Run with:
  - **Docker Engine + Docker Compose plugin**
  - **Direct Python (FastAPI + Uvicorn)**

---

## Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Containerization:** Docker, Docker Compose

---

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

---

## Installation Guide

## Option 1: Install and Run on Linux (Without Docker)

### 1) Prerequisites
- Python 3.10+ installed
- `pip` available

### 2) Clone repository
```bash
git clone https://github.com/AMARNADH-HUB/Lonewolf-hashcracker.git
cd Lonewolf-hashcracker
```

### 3) Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4) Install dependencies
```bash
pip install -r requirements.txt
```

### 5) Start server
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 6) Open Web UI
- Local machine: `http://localhost:8000`
- Same LAN: `http://<your-linux-ip>:8000`

---

## Option 2: Install and Run on Linux (Docker)

### 1) Prerequisites
- Docker Engine installed and running
- Docker Compose plugin available (`docker compose`)

### 2) Clone repository
```bash
git clone https://github.com/AMARNADH-HUB/Lonewolf-hashcracker.git
cd Lonewolf-hashcracker
```

### 3) Build and run container
```bash
docker compose up --build -d
```

### 4) Open Web UI
- `http://localhost:8000`

### 5) Stop service
```bash
docker compose down
```

---

## API Endpoints

- `GET /` → Web UI
- `GET /health` → Health check
- `POST /api/detect` → Detect likely hash type
- `POST /api/verify` → Verify plaintext against hash

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

---

## Troubleshooting

- **Port already in use**
  - Run on another port: `--port 8080` and update URL accordingly.
- **Docker daemon not running**
  - Start Docker service first, then rerun `docker compose up --build -d`.
- **Cannot access from LAN**
  - Ensure firewall allows inbound traffic on port `8000`.

---

## Security Notes

- Detection is heuristic/probabilistic, not guaranteed certainty.
- For real password storage, prefer **Argon2id** or **bcrypt** with secure settings.
- Use this tool only for authorized systems and legal security testing.
