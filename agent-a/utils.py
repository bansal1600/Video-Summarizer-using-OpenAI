# agent_a/utils.py

from youtube_transcript_api import YouTubeTranscriptApi
import os
import httpx

def extract_transcript(video_url):
    try:
        video_id = video_url.split("v=")[-1]
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([entry["text"] for entry in transcript_data])
        return transcript
    except Exception as e:
        raise RuntimeError(f"Transcript fetch failed: {e}")

async def search_related_articles(query):
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return ["(Missing Tavily API Key)"]

    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "query": query,
        "search_depth": "basic",
        "include_answers": False,
        "include_raw_content": False
    }

    async with httpx.AsyncClient(timeout=8.0) as client:
        response = await client.post("https://api.tavily.com/search", json=payload, headers=headers)
        response.raise_for_status()
        results = response.json()
        return [f"{item['title']} - {item['url']}" for item in results.get("results", [])[:3]]
