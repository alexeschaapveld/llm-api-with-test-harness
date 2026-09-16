# Local LLM API Gateway

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Local-orange.svg)](https://ollama.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A asynchronous API gateway built with **FastAPI** designed to route requests to local LLM inference engines (**Ollama**). This project focuses heavily on system resilience, predictable error handling, and performance benchmarking under load. 

---

## 🚀 Key Features

* **Sub-Second Health Monitoring:** A dedicated `/health` endpoint that proactively verifies downstream uptime for both the gateway and the local Ollama engine without executing costly inference tasks.
* **Resilient Timeout Management:** Enforces strict asynchronous request timeouts using `httpx` (2s for health checks, 30s for generation) to prevent frozen LLM tasks from locking up Uvicorn’s event loop.
* **Standardized Error Handling:** Replaces generic `500 Internal Server Error` crashes with predictable, structured HTTP status codes (`503 Service Unavailable`, `504 Gateway Timeout`) for clean downstream client handling.
* **Performance Benchmarked:** Hardware throughput limits, p95 latencies, and system failure points evaluated and documented via **Locust** load testing.

---

## 🛠️ Tech Stack

* **Core Framework:** FastAPI, Uvicorn (ASGI)
* **HTTP Client:** `httpx` (AsyncClient)
* **Inference Engine:** Ollama (`smollm2:135m`)
* **Load Testing:** Locust
* **Version Control:** Git  (Feature-branch workflow)

---

## ⚙️ Getting Started

### Prerequisites
* Python 3.13.x installed
* [Ollama](https://ollama.com/) installed and running locally with your target model pulled (e.g., `ollama run smollm2:135m`)

> This project has been validated on Python 3.13. The dependency stack in `uvicorn[standard]` can fail under Python 3.14 on this Windows/MSYS2 environment due to `watchfiles` platform compatibility issues.

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment with Python 3.13:**
   ```bash
   py -3.13 -m venv .venv313
   .\.venv313\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Run tests:**
   ```bash
   python -m pytest -q
   ```

## Performance & Benchmarks

### Test Enviroment
* **Model:** 'smollm2:135M' (via Ollama)
* **CPU:** AMD Ryzen 5500U with Radeon Graphics
* **RAM:** 32GB of DDR4 

### Results
* **Optimal Capacity:** 1-2 concurrent users (~0.9 RPS, p95 latency < 7s, 0% failure)
* **Soft Limit (Latency Degradation):** 5+ concurrent users (~1.6 RPS, p95 latency spikes to 28s, 0% failure)
* **Hard Breaking Point:** 8+ concurrent users (Requests fail due to queue timeouts)

### Running Load Tests
```bash
locust -f load_tests/locustfile.py --host http://localhost:8000
```
