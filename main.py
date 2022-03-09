from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers.image import image
from routers.upload import upload


# Description for api docs
description = """
### Made by FusionSid

[My Github](https://github.com/FusionSid)

This api lets you upload images which are stored and can be retreived later

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

@app.get("/")
async def home():
    return RedirectResponse("/docs")

app.include_router(image)
app.include_router(upload)