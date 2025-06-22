# 🎓 YouTube Educational Assistant (Multi-Agent + AG-UI)

This project is a multi-agent GenAI-powered application that summarizes educational YouTube videos, generates FAQs and jargon explanations, and enriches learning using external article search — all wrapped in an interactive UI using the AG-UI protocol.

Built with:  
🧠 OpenAI GPT-3.5  
🔀 Agent-to-Agent (A2A) communication  
🌐 Tavily API for article search  
📦 Docker Compose for orchestration  
🎛️ Streamlit frontend (AG-UI protocol)

---

## 🚀 Features

- Extracts and summarizes YouTube transcripts  
- Communicates between agent-a and agent-b using A2A  
- Generates FAQs and simplifies jargon  
- Enriches knowledge with Tavily-powered article search  
- Outputs rendered in AG-UI-compatible spec  
- Fully containerized with Docker Compose  

---

## 🧱 Project Structure

```
yt-edu-assistant/
├── agent-a/
│   ├── agent_a.py
│   ├── utils.py
│   └── Dockerfile
├── agent-b/
│   ├── agent_b.py
│   └── Dockerfile
├── ui/
│   ├── streamlit_app.py
│   └── Dockerfile
├── docker-compose.yml
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone this repo**  
   ```bash
   git clone https://github.com/your-username/yt-edu-assistant.git
   cd yt-edu-assistant
   ```

2. **Create a `.env` file in the root**  
   ```
   OPENAI_API_KEY=your_openai_key
   TAVILY_API_KEY=your_tavily_key
   ```

3. **Run the app using Docker Compose**  
   ```bash
   docker compose --env-file .env up --build
   ```

---

## 🌍 Access the Services

| Service    | URL                          |
|------------|------------------------------|
| 🧠 Agent A | http://localhost:8000/docs   |
| 🧠 Agent B | http://localhost:8001/docs   |
| 🖥️ UI      | http://localhost:8501        |

---

## 🧪 How It Works

1. You input a YouTube video URL in the UI  
2. `agent-a` fetches the transcript and summarizes it using OpenAI  
3. `agent-a` sends the summary to `agent-b` (via A2A) to generate:  
   - FAQs  
   - Jargon explanations  
4. `agent-a` enriches the summary with external articles from Tavily  
5. The UI displays all output in an interactive AG-UI format  

---

## 🔧 Requirements

- Python 3.10+  
- Docker & Docker Compose  
- OpenAI API Key  
- Tavily API Key  

---

## 📌 Tech Stack

| Layer         | Tools/Frameworks       |
|---------------|------------------------|
| LLM           | OpenAI GPT-3.5 Turbo   |
| Agent Runtime | FastAPI, httpx         |
| UI            | Streamlit + AG-UI Spec |
| Orchestration | Docker Compose         |
| Search        | Tavily API             |

---

## 📜 License

MIT License

---

## 🙌 Acknowledgments

Built by [Gaurav Bansal](https://github.com/gauravbansalutd), with inspiration from AG-UI, A2A protocol, and GenAI innovation.
# Video-Summarizer-using-OpenAI
# Video-Summarizer-using-OpenAI
# Video-Summarizer-using-OpenAI
