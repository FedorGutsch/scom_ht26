from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.config import settings
from app.routers.candidates import router as candidates_router
from app.routers.vacancies import router as vacancies_router
from app.database.base import Base
from app.database.session import engine
from app.exceptions import AppException
from app.routers.analyze import router as analyze_router 
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os



def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, docs_url="/docs", redoc_url=None)
    
    # 1. Подключаем API роутеры (как и было)
    app.include_router(candidates_router, prefix=settings.API_PREFIX)
    app.include_router(vacancies_router, prefix=settings.API_PREFIX)
    app.include_router(analyze_router, prefix=settings.API_PREFIX)

    # 2. ДОБАВЛЯЕМ: Раздача статики (папка dist)
    # Важно: это должно быть ПОСЛЕ API роутеров
    if os.path.exists("dist"):
        app.mount("/assets", StaticFiles(directory="dist/assets"), name="static")
        
        @app.get("/{full_path:path}")
        async def serve_frontend(full_path: str):
            # Если запрос не к API, отдаем index.html нашего фронтенда
            return FileResponse("dist/index.html")
            
    return app


app = create_app()