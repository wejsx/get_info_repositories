from fastapi import FastAPI
from .endpoint import router

def createApp() -> FastAPI:
    app = FastAPI(
        title='Github get user info',
        version='1.0',
        debug=True)
    app.include_router(router)
    return app

app = createApp()