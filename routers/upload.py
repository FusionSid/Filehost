from fastapi import APIRouter, UploadFile, Request, Query
from slowapi import Limiter
from slowapi.util import get_remote_address
from utils import *

limiter = Limiter(key_func=get_remote_address)

tags_metadata = [
    {
        "name": "Upload file",
    }
]

upload = APIRouter(tags=tags_metadata)

@upload.post("/api/upload")
@limiter.limit("42/minute")
async def post_upload(request : Request, file : UploadFile, file_type : str):
    if file_type.lower() not in ['png', 'txt', 'jpeg', 'gif', 'mp4', 'mp3']:
        return {
            "error" : "Must include file type, Options: png, txt, jpeg, gif, mp4, mp3]"
        }
    file = await file.read()
    if len(file) > 15000000:
        return {
            "error" : "File to large, Max size 15mb"
        }
    code = await insert_file(bytes(file), file_type)
    return {
        "code" : code,
        "url" : f"https://file-host.herokuapp.com/api/file?code={code}"
    }