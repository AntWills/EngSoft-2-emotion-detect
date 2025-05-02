# main.py
from fastapi import FastAPI, Request
# from src.agent.base_agent.base import agent
# from src.agent.domain.handler_emotion.input import APIGatewayProxyRequestEvent
from handlers.handler_emotion import get_emotion_chain

app = FastAPI()


@app.post("/")
async def hello(request: Request):
    body = await request.json()
    return {"hello": body}


@app.post("/emotion")
async def emotion_endpoint(request: Request):
    body = await request.json()
    return get_emotion_chain(body, None).get("emotions")
