import os
from pydantic_settings import BaseSettings, SettingsConfigDict

# Определяем путь к папке, где лежит этот файл (app/)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Поднимаемся на уровень выше к корню бэкенда, где обычно лежит .env
root_dir = os.path.dirname(current_dir)
env_path = os.path.join(root_dir, ".env")

class Settings(BaseSettings):
    # Указываем точный путь к .env файлу
    model_config = SettingsConfigDict(
        env_file=env_path, 
        env_file_encoding='utf-8',
        case_sensitive=True, 
        extra="ignore"
    )
    
    PROJECT_NAME: str = "HireMatch MVP"
    DATABASE_URL: str = "sqlite:///./app.db"
    API_PREFIX: str = "/api/v1"
    
    # Значения будут приоритетно браться из .env, если они там прописаны
    OPENROUTER_API_KEY: str = ""
    OPENROUTER_MODEL: str = "tencent/hy3-preview:free"
    OPENROUTER_TIMEOUT_SECONDS: int = 30

settings = Settings()