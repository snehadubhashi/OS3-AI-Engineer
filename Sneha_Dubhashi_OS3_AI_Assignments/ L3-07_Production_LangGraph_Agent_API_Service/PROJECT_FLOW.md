# Project Flow

1. User sends request to FastAPI.

2. FastAPI validates request.

3. Request forwarded to LangGraph Agent.

4. Agent sends prompt to Ollama.

5. LLM determines whether external tool is required.

6. If required:

   LangGraph invokes MCP Tool.

7. MCP Tool executes operation.

8. Tool result returned to Agent.

9. Agent generates final response.

10. FastAPI returns response to user.

```
User

↓

FastAPI

↓

LangGraph Agent

↓

Ollama

↓

MCP Tool

↓

Result

↓

FastAPI

↓

User
```