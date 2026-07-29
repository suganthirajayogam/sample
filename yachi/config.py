"""
Central configuration. Everything that might need tuning for a different
machine, model, or folder layout lives here — not scattered through the code.
"""
import os
from pathlib import Path

# --- Storage locations ---
# Where Chroma persists its vector index and where we cache per-product
# SQLite databases built from Excel/SQL files. This is OUR storage, separate
# from the user's product folders (which we only ever read, never write to).
BACKEND_ROOT = Path(__file__).resolve().parent.parent
STORAGE_DIR = Path(os.environ.get("RAG_STORAGE_DIR", BACKEND_ROOT / "storage"))
CHROMA_DIR = STORAGE_DIR / "chroma"
SQLITE_CACHE_DIR = STORAGE_DIR / "sqlite_cache"

STORAGE_DIR.mkdir(parents=True, exist_ok=True)
CHROMA_DIR.mkdir(parents=True, exist_ok=True)
SQLITE_CACHE_DIR.mkdir(parents=True, exist_ok=True)

# --- Embedding model ---
# all-MiniLM-L6-v2: ~80MB, runs fine on CPU, good enough quality for this
# scale of data. Change here if you want a different one later.
EMBEDDING_MODEL = os.environ.get("RAG_EMBEDDING_MODEL", "all-MiniLM-L6-v2")

# --- Ollama (LLM) ---
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "qwen2:0.5b")
OLLAMA_TIMEOUT_SECONDS = 60

# --- Ingestion behavior ---
SUPPORTED_EXCEL_EXTENSIONS = {".xlsx", ".xls", ".csv"}
SUPPORTED_PDF_EXTENSIONS = {".pdf"}
SUPPORTED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
SUPPORTED_DB_EXTENSIONS = {".db", ".sqlite", ".sqlite3"}

# Columns in Excel sheets that likely reference an image filename. Matching
# is case-insensitive substring match against the header, so "Image Ref",
# "image_url", "photo_file" etc. all match.
IMAGE_COLUMN_HINTS = ["image", "photo", "picture", "img", "thumbnail"]

# Chunk size (characters) for splitting PDF text before embedding.
PDF_CHUNK_SIZE = 800
PDF_CHUNK_OVERLAP = 120

# How many vector search results to retrieve per query.
TOP_K_RESULTS = 5
