## Performance & Benchmarks

### Test Enviroment
* **Model:** 'smollm2:135M' (via Ollama)
* **GPU/VRAM:** AMD Ryzen 5500U with Radeon Graphics
* **CPU/RAM:** 32GB of DDR4 

### Results
* **Optimal Capacity:** 1-2 concurrent users (~0.9 RPS, p95 latency < 7s, 0% failure)
* **Soft Limit (Latency Degradation):** 5+ concurrent users (~1.6 RPS, p95 latency spikes to 28s, 0% failure)
* **Hard Breaking Point:** 8+ concurrent users (Requests fail due to queue timeouts)
