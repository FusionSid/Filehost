from fastapi import FastAPI
from routers.image import image
from routers.upload import upload

app = FastAPI()

app.include_router(image)
app.include_router(upload)