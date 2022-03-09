from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from io import BytesIO
from utils import *

tags_metadata = [
    {
        "name": "Gets image",
    }
]

image = APIRouter(tags=tags_metadata)

@image.get("/api/image")
async def getimage(code : str):
    image_bytes = await get_image(code)
    if len(image_bytes) == 0:
        return {"error", "Image not found"}
    image = BytesIO(image_bytes[3])
    image.seek(0)

    return StreamingResponse(image, media_type="image/png")