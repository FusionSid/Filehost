from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from io import BytesIO
from slowapi import Limiter
from slowapi.util import get_remote_address
from utils import *

limiter = Limiter(key_func=get_remote_address)

tags_metadata = [
    {
        "name": "Gets image",
    }
]

image = APIRouter(tags=tags_metadata)


@image.get("/api/image")
@limiter.limit("69/minute")
async def getimage(request : Request, code : str):
    image_bytes = await get_image(code)

    if image_bytes == False:
        return {"error" : "Image not found"}

    if len(image_bytes) == 0:
        return {"error" : "Image not found"}

    image = BytesIO(image_bytes[3])
    image.seek(0)

    return StreamingResponse(image, media_type="image/png")