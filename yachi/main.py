from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import connect, ask, images
from app.services.ollama_client import is_ollama_available

app = FastAPI(title="Product Data Assistant API")

# Flutter desktop runs as its own process and calls this over HTTP, so CORS
# needs to be open. This server is meant for local-machine use only —
# don't expose it to an untrusted network without adding real auth.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(connect.router)
app.include_router(ask.router)
app.include_router(images.router)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "ollama_available": is_ollama_available(),
    }
