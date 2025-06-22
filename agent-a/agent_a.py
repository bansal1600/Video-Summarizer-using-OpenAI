# agent-a/agent_a.py

from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI
import httpx
from utils import extract_transcript, search_related_articles
import os

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment")

client = OpenAI(api_key=openai_api_key)

app = FastAPI()

class VideoInput(BaseModel):
    video_url: str

def get_openai_summary(transcript: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Summarize this YouTube transcript as if for a study guide:\n" + transcript}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

@app.post("/summarize_agui")
async def summarize_agui(input: VideoInput):
    transcript = extract_transcript(input.video_url)
    summary = get_openai_summary(transcript)

    async with httpx.AsyncClient(timeout=10.0) as client_http:
        response = await client_http.post("http://agent-b:8001/explain", json={"summary": summary})
        response.raise_for_status()
        enhanced = response.json()

    related_articles = await search_related_articles(summary[:300])
    links_text = "\n".join(related_articles)

    return {
        "agui_spec": {
            "type": "object",
            "title": "Video Summary Assistant",
            "description": "Learn deeply from video, AI Q&A, and external resources.",
            "sections": [
                {"title": " Summary", "type": "text", "content": summary},
                {"title": " FAQs", "type": "text", "content": enhanced["faq"]},
                {"title": " Jargon Explained", "type": "text", "content": enhanced["jargon_explained"]},
                {"title": " Related Articles", "type": "text", "content": links_text}
            ]
        }
    }
