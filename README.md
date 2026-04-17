# Lonewolf Hash Security Auditor
<img width="1408" height="768" alt="lonewolf-hashcracker" src="https://github.com/user-attachments/assets/e94d0889-1c0a-49cb-9251-4acc88af6a0b" />

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
uvicorn app.main:app --host <your-linux-ip> --port 8000
```
<img width="1235" height="947" alt="Screenshot 2026-04-17 112825" src="https://github.com/user-attachments/assets/1029591c-20b6-43a3-9e72-256b517868a8" />

### 6) Open Web UI
- Local machine: `http://localhost:8000`
- Same LAN: `http://<your-linux-ip>:8000`

<img width="1919" height="748" alt="Screenshot 2026-04-17 124519" src="https://github.com/user-attachments/assets/9d3f72fb-cf83-4ff4-ae59-43340d127889" />

---

## Option 2: Install and Run on Linux (Docker)

### 1) Prerequisites
- Docker Engine installed and running
- Docker Compose plugin available (`docker compose`)
- you can verify:
```bash
docker --version
docker compose version
```

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
```bash
http://localhost:8000
```  
If you're on a remote server, replace localhost with your server’s IP.

### 5) Stop service
```bash
docker compose down
```
⚠️ Useful Tips
If port 8000 is already in use, edit the docker-compose.yml file.
To see logs:
```bash
docker compose logs -f
```
If something fails, try:
```bash
docker compose down
docker compose up --build
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

<img width="1919" height="956" alt="Screenshot 2026-04-17 105105" src="https://github.com/user-attachments/assets/6e52be26-149a-4e14-b254-c0f622a58119" />

### Example: Verify

```bash
curl -X POST http://localhost:8000/api/verify \
  -H "Content-Type: application/json" \
  -d '{"hash_value":"5d41402abc4b2a76b9719d911017c592","plaintext":"hello"}'
```
<img width="1919" height="964" alt="Screenshot 2026-04-17 105222" src="https://github.com/user-attachments/assets/e9946461-61cd-4869-ba71-9bcc4c8cff68" />

<img width="1918" height="969" alt="Screenshot 2026-04-17 105717" src="https://github.com/user-attachments/assets/6e941b6b-3e0a-493b-8f0d-77d27dbcd48d" />

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

---
---

## MIT LICENSE

Copyright (c) 2026 Amarandh S

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
