from fastapi import APIRouter, UploadFile
from utils import *

tags_metadata = [
    {
        "name": "Upload image",
    }
]

upload = APIRouter(tags=tags_metadata)

@upload.post("/api/upload")
async def post_upload(file : UploadFile, author = None):
    file = await file.read()
    code = await insert_image(bytes(file), author)
    return {
        "code" : code,
        "url" : f"https://filehost.fusionsid.repl.co/api/image?code={code}"
    }