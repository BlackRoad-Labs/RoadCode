"""Inference benchmarks — measure tokens/sec across fleet."""
import time
import httpx
from dataclasses import dataclass

@dataclass
class BenchResult:
    node: str
    model: str
    tokens_per_sec: float
    time_to_first_token: float
    total_tokens: int
    total_time: float

async def benchmark_node(host: str, port: int = 11434, model: str = "llama3.2:3b") -> BenchResult:
    prompt = "Explain the concept of sovereignty in computing in exactly 100 words."
    start = time.monotonic()
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(f"http://{host}:{port}/api/generate",
                                  json={"model": model, "prompt": prompt, "stream": False})
        total = time.monotonic() - start
        data = resp.json()
        tokens = data.get("eval_count", 0)
        return BenchResult(host, model, tokens / total if total > 0 else 0, 0, tokens, total)
