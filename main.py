from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers.download import file
from routers.upload import upload

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

# Description for api docs
description = """
### Made by FusionSid

[My Github](https://github.com/FusionSid)

This api lets you upload files which are stored and can be retreived later

#### Source Code:
[https://github.com/FusionSid/Filehost](https://github.com/FusionSid/Filehost)

#### Contact:
Discord: FusionSid#3645

#### LICENCE:
"""

# Creates an instance of the FastAPI class
app = FastAPI(
    title = "Filehost",
    description=description,
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get("/")
async def home():
    return RedirectResponse("/docs")

app.include_router(file)
app.include_router(upload)