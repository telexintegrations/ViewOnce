#!/usr/bin/python3
"""FastApi to return a JSON for telex integration"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from os import environ
from typing import List, Dict

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://toluairbnb.tech",
         "http://staging.telextest.im",
        "http://telextest.im",
        "https://staging.telex.im",
        "https://telex.im"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/viewOnce")
def nginx_status():
    """ The function for the integration endpoint"""

    return {
        "data": {
            "date": {
                "created_at": "2025-02-20",
                "updated_at": "2025-02-20"
            },
            "descriptions": {
                "app_name": "ViewOnce",
                "app_description": "A telex app to create view once messages",
                "app_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRRVxPRCAc6HBRl_tR-aMkrCUHZq45ChY_RiwkzwqdF0T8IO52m3Yb9yvp1jjlpyyzVS0&usqp=CAU",
                "app_url": "https://viewonce.onrender.com/viewOnce",
                "background_color": "#fff"
            },
            "is_active": True,
            "integration_type": "modifier",
            "integration_category": "Monitoring & Logging",
            "key_features": [
                "Find and close view once messages"
            ],
            "author": "Toluwaloju Kayode",
            "settings": [
                {
                    "label": "Find view once",
                    "type": "checkbox",
                    "required": True,
                    "default": True
                },
                {
                    "label": "View Once message",
                    "type": "text",
                    "required": True,
                    "default": "Contact <INPUT YOUR NUMBER> for the message"
                }
            ],
            "target_url": "https://viewonce.onrender.com/target_url",
            "endpoints": [
                {
                    "path": "/target_url",
                    "method": "POST",
                    "description": "Default endpoint"
                }
            ]
        }
    }
        


@app.post("/target_url")
async def targetUrl(request: Request):
    """The target url for the telex integration"""

    body = await request.json()

    settings = body.get('settings')
    for setting in settings:
        if setting.get('type') == 'text':
            edited_message = setting.get('default')
        if setting.get('type') == "checkbox":
            viewonce = setting.get("default")
    if viewonce:
        return {"message": edited_message}
    return {"message": body.get("message")}


if __name__ == "__main__":
    """ Run the FastAPI application """
    import uvicorn
    port = int(environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)