from fastapi import APIRouter, UploadFile, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from utils import *

limiter = Limiter(key_func=get_remote_address)

tags_metadata = [
    {
        "name": "Upload image",
    }
]

upload = APIRouter(tags=tags_metadata)

@upload.post("/api/upload")
@limiter.limit("10/minute")
async def post_upload(request : Request, file : UploadFile, author = None):
    file = await file.read()
    code = await insert_image(bytes(file), author)
    return {
        "code" : code,
        "url" : f"https://filehost.fusionsid.repl.co/api/image?code={code}"
    }