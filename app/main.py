from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import ballot_router, lottery_router, partecipant_router
from app.settings import settings


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return _app


app = get_application()
app.include_router(partecipant_router)
app.include_router(ballot_router)
app.include_router(lottery_router)
