"""
Módulo de configuración de RAG (Retrival Aumented Generation)
"""

from pydantic import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).resolve().parents[1]
    DATA_DIR: Path = BASE_DIR / "data"
    CHROMA_DIR: Path = DATA_DIR / "chroma"

    OPENAI_API_KEY: str | None = None
    EMBEDDING_MODEL: str = "text-embedding3_small"

    TOP_K: int = 5
    MIN_RELEVANCE_SCORE: float = 0.5
    
    class Config: 
        env_file = ".env"

# Creamos una instancia de la clase settings 
settings = Settings()
