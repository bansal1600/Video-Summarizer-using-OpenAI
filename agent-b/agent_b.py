# agent-b/agent_b.py

from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI
import os

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment")

client = OpenAI(api_key=openai_api_key)

app = FastAPI()

class SummaryInput(BaseModel):
    summary: str

def generate_with_openai(prompt: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

@app.post("/explain")
async def explain_summary(data: SummaryInput):
    faq_prompt = f"Based on the following summary, generate 3 helpful FAQ questions and their answers:\n{data.summary}"
    jargon_prompt = f"From this summary, extract and explain 5 complex or technical terms in a simple way:\n{data.summary}"

    faq_response = generate_with_openai(faq_prompt)
    jargon_response = generate_with_openai(jargon_prompt)

    return {
        "faq": faq_response,
        "jargon_explained": jargon_response
    }
