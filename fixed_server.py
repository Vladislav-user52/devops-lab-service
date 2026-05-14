from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI()

REQUESTS = Counter('http_requests_total', 'Total requests', ['method'])

@app.get("/")
def root():
    REQUESTS.labels(method='GET').inc()
    return {"message": "Service is running", "status": "ok"}

@app.get("/metrics")
def metrics():
    REQUESTS.labels(method='GET').inc()
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/health")
def health():
    return {"status": "healthy"}
