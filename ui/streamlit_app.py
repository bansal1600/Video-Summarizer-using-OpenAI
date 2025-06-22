# ui/streamlit_app.py

import streamlit as st
import requests

st.set_page_config(page_title="🎓 YouTube Educational Assistant", layout="wide")

st.title("YouTube Video Learning Assistant")
st.caption("Powered by A2A, AG-UI, and Tavily")

video_url = st.text_input("Enter a YouTube Video URL")

if st.button("Analyze"):
    if not video_url:
        st.warning("Please enter a valid video URL.")
    else:
        with st.spinner("Analyzing video, summarizing, and enriching content..."):
            try:
                response = requests.post(
                    "http://agent-a:8000/summarize_agui",
                    json={"video_url": video_url},
                    timeout=30
                )
                response.raise_for_status()
                agui_spec = response.json().get("agui_spec", {})
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.stop()

        st.success("✅ Process complete. Here's what we found:")

        # Render AG-UI sections
        if agui_spec:
            st.header(agui_spec.get("title", "Agent Output"))
            st.markdown(agui_spec.get("description", ""), unsafe_allow_html=True)

            for section in agui_spec.get("sections", []):
                with st.expander(section.get("title", "Section")):
                    st.markdown(section.get("content", ""), unsafe_allow_html=True)
        else:
            st.warning("No AG-UI spec returned by the agent.")
