#!/usr/bin/python3
"""FastApi to return a JSON for telex integration"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from os import environ
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
		"author": "Micah Shallom",
		"date": {
			"created_at": "2025-02-13",
			"updated_at": "2025-02-13"
		},
		"descriptions": {
			"app_description": "A message formatter bot that processes incoming messages and sends back formatted responses.",
			"app_logo": "https://media.tifi.tv/telexbucket/public/logos/formatter.png",
			"app_name": "Message Formatter",
			"app_url": "https://txtformat.com/",
			"background_color": "#ffffff"
		},
		"integration_category": "Communication & Collaboration",
		"integration_type": "modifier",
		"is_active": "true",
		"key_features": [
			"Receive messages from Telex channels.",
			"Format messages based on predefined templates or logic.",
			"Send formatted responses back to the channel.",
			"Log message formatting activity for auditing purposes."
		],
		"permissions": {
			"events": [
				"Receive messages from Telex channels.",
				"Format messages based on predefined templates or logic.",
				"Send formatted responses back to the channel.",
				"Log message formatting activity for auditing purposes."
			]
		},
		"settings": [
			{
				"default": 100,
				"label": "maxMessageLength",
				"required": "true",
				"type": "number"
			},
			{
				"default": "world,happy",
				"label": "repeatWords",
				"required": "true",
				"type": "multi-select"
			},
			{
				"default": 2,
				"label": "noOfRepetitions",
				"required": "true",
				"type": "number"
			}
		],
		"target_url": "https://system-integration.telex.im/format-message",
		"tick_url": "https://system-integration.telex.im/format-message",
		"website": "https://telex.im"
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

if __name__ == "__main__":
    """ Run the FastAPI application """
    import uvicorn
    port = int(environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)