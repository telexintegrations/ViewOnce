#!/usr/bin/python3
"""FastApi to return a JSON for telex integration"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://toluairbnb.tech"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/viewOnce")
def nginx_status():
    """ The function for the integration endpoint"""

    return JSONResponse(
        status_code=200,
        content={
            "data": {
                "date": {
                    "created_at": "2025-02-20",
                    "updated_at": "2025-02-20"
                },
                "descriptions": {
                    "app_name": "ViewOnce",
                    "app_description": "To set a view once setting for messages",
                    "app_logo": "https://imgur.com/a/wOwIpco",
                    "app_url": "http://toluairbnb.tech/viewOnce",
                    "background_color": "#fff"
                },
                "is_active": True,
                "integration_category": "Monitoring & Logging",
                "integration_type": "modifier",
                "key_features": ["check box"],
                "author": "TeeCoded",
                "permissions": {
                    "monitoring_user": {
                        "always_online": True,
                        "display_name": "Performance Monitor"
                    }
                },
                "settings": [
                    {
                        "label": "Update view once",
                        "type": "checkbox",
                        "required": True,
                        "default": False,
                        "options": [True, False]
                    }
                ],
                "target_url": "http://toluairbnb.tech/target_url",
                "tick_url": "None"
            }
        }
    )


@app.post("/target_url")
async def targetUrl(message: str, channel_id: str, settings: List[Dict]):
    """The target url for the telex integration"""

    if len(settings) == 0:
        return JSONResponse(
            status_code=400,
            content={
                "error": "No setting was found for your message"""
            }
        )
    for setting in settings:
        if setting.get('default') == "true":
            return JSONResponse(
                status_code=200,
                content={
                    "event_name": "message_formatted",
                    "message": "This is a view once message, Contact the \
sender for further clarifications",
                    "status": "success",
                    "username": "VeiwOnce-bot"
                }
            )
    return JSONResponse(
        status_code=200,
        content={
            "event_name": "message_ not_formatted",
            "message": "message",
            "status": "success",
            "username": "VeiwOnce-bot"
        }
    )
