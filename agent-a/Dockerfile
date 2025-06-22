# agent-a/Dockerfile

FROM python:3.10-slim

WORKDIR /app
COPY . /app

# Copy requirements.txt from the root folder (one level up)
COPY ../requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "agent_a:app", "--host", "0.0.0.0", "--port", "8000"]
