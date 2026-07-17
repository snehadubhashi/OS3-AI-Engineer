# Production LangGraph Agent API

A production-ready REST API built using **FastAPI**, **LangGraph**, and **Model Context Protocol (MCP)**. The application exposes a LangGraph-based AI agent capable of answering user queries and invoking external tools through MCP.

---

# Features

- LangGraph-based AI Agent
- FastAPI REST API
- MCP Tool Integration
- Ollama LLM
- Streaming Responses (Server-Sent Events)
- Swagger Documentation
- Request Validation using Pydantic
- Structured Error Handling
- Logging
- Docker Support
- Docker Compose Support

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | REST API Framework |
| LangGraph | AI Agent Workflow |
| LangChain | Agent Framework |
| Ollama | Local LLM |
| MCP | Tool Integration |
| Docker | Containerization |
| Docker Compose | Multi-container Deployment |
| SSE | Streaming Responses |

---

# Project Structure

```
Production-LangGraph-Agent/
│
├── app/
│   ├── agent.py
│   ├── api.py
│   ├── config.py
│   ├── logger.py
│   ├── main.py
│   ├── mcp_server.py
│   ├── models.py
│   ├── streaming.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env
```

---

# Architecture

```
                User

                  │

            POST /chat

                  │

              FastAPI API

                  │

           LangGraph Agent

                  │

            Ollama (LLM)

                  │

        MCP Client Adapter

                  │

        Calculator MCP Server

                  │

          Tool Execution

                  │

         Final AI Response

                  │

                User
```

---

# Installation


## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Start Ollama

Ensure Ollama is running locally.

Example:

```bash
ollama run llama3.2
```

---

# Run MCP Server

```bash
python app/mcp_server.py
```

---

# Run FastAPI

```bash
uvicorn app.main:app --reload
```

---

# Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Swagger

```
http://localhost:8000/docs
```

---

# API Endpoints

## GET /

Returns application status.

Response

```json
{
    "status":"Running"
}
```

---

## GET /health

Checks application health.

Response

```json
{
    "status":"healthy"
}
```

---

## GET /version

Returns application version.

Response

```json
{
    "version":"1.0.0",
    "framework":"LangGraph",
    "llm":"Ollama"
}
```

---

## POST /chat

Processes user requests using the LangGraph agent.

Request

```json
{
    "message":"Who is Virat Kohli?"
}
```

Response

```json
{
    "response":"Virat Kohli is..."
}
```

---

## POST /stream

Streams responses using Server-Sent Events.

Request

```json
{
    "message":"Explain LangGraph"
}
```

---

# MCP Tool Integration

The project integrates external tools through Model Context Protocol (MCP).

Current Tool

- Calculator

Example

Input

```
Calculate 245 × 78
```

Output

```
19110
```

---

# Logging

The application logs

- Incoming Requests
- Agent Execution
- Execution Time
- Errors

Example

```
INFO Request Received

INFO Execution Completed in 1.2 sec
```

---

# Streaming

Streaming responses are implemented using Server-Sent Events (SSE), allowing responses to be sent incrementally instead of waiting for the complete output.

---

# Validation

Incoming requests are validated using Pydantic.

Example

```json
{
    "message":"Explain LangGraph"
}
```

---

# Error Handling

Example

```json
{
    "success": false,
    "message": "Agent execution failed",
    "error": "Detailed error"
}
```

---

# Future Enhancements

- Authentication (JWT)
- Redis Caching
- PostgreSQL
- Vector Database
- Multiple MCP Tool Servers
- Kubernetes Deployment
- CI/CD Pipeline
- Monitoring with Prometheus & Grafana

---

# Author

Sneha Dubhashi
