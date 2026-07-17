# API Documentation

## Base URL

```
http://localhost:8000
```

---

# 1. Home

## GET /

### Description

Returns API status.

### Response

```json
{
    "status":"Running"
}
```

---

# 2. Health Check

## GET /health

### Description

Checks whether the API is healthy.

### Response

```json
{
    "status":"healthy"
}
```

---

# 3. Version

## GET /version

### Description

Returns framework information.

### Response

```json
{
    "version":"1.0.0",
    "framework":"LangGraph",
    "llm":"Ollama"
}
```

---

# 4. Chat

## POST /chat

### Description

Sends a user prompt to the LangGraph Agent.

### Request

```json
{
    "message":"Who is Virat Kohli?"
}
```

### Response

```json
{
    "response":"Virat Kohli is..."
}
```

---

# 5. Stream

## POST /stream

### Description

Returns streamed response using Server-Sent Events.

### Request

```json
{
    "message":"Explain LangGraph"
}
```

### Response

```
data: LangGraph

data: is

data: a

event:end
```