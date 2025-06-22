# agent-b/Dockerfile

FROM python:3.10-slim

WORKDIR /app
COPY . /app

# Copy requirements.txt from the root folder (one level up)
COPY ../requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001
CMD ["uvicorn", "agent_b:app", "--host", "0.0.0.0", "--port", "8001"]