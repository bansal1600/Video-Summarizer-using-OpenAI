import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

print(os.getenv("GOOGLE_API_KEY"))  # Should print the key

# Get API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")

# # Debug: Print to check if API key is loaded
if not api_key:     
    st.error("API key not found. Please check your .env file.")
    raise ValueError("API key not found. Make sure your .env file is set correctly.")
else:
    st.success("API key loaded successfully.")  # This should appear in Streamlit

genai.configure(api_key=api_key)

## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):
    model=genai.GenerativeModel("gemini-1.5-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

# Streamlit app layout
st.title("YouTube Video Summarizer")

# Input text box for the video link
video_url = st.text_input("Enter YouTube Video URL:")

# Input text box for the video link
prompt = st.text_input("Enter what you want to chat about the video:")

if st.button("Summarize"):
    # Get transcript and summarize it
    if video_url:
        with st.spinner('Fetching and summarizing...'):
            transcript = extract_transcript_details(video_url)
            if "Error" not in transcript:
                summary = generate_gemini_content(transcript, prompt)
                st.subheader("Summary")
                st.write(summary)
            else:
                st.error(transcript)
    else:
        st.warning("Please enter a YouTube video URL.")