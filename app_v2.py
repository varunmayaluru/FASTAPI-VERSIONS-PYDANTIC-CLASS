from fastapi import FastAPI
from src.routers import book_routers_v1
from src.routers import book_routers_v2


def create_app():
    app = FastAPI()

    app.include_router(book_routers_v1.router, prefix="/v1")
    
    app.include_router(book_routers_v2.router)
    app.include_router(book_routers_v2.router, prefix="/v2")
    app.include_router(book_routers_v2.router, prefix="/latest")

    return app


app = create_app()