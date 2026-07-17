# Architecture

```
                  User

                    │

            REST API Request

                    │

                FastAPI API

                    │

              LangGraph Agent

                    │

              ChatOllama LLM

                    │

      Determines whether Tool is Required

                    │

          MCP Client Adapter

                    │

        Calculator MCP Server

                    │

           Executes Tool Logic

                    │

         Returns Tool Response

                    │

          LangGraph Agent

                    │

           FastAPI Response

                    │

                 User
```

---

# Components

## FastAPI

Provides REST API endpoints.

---

## LangGraph Agent

Controls reasoning and tool execution.

---

## Ollama

Provides Large Language Model.

---

## MCP

Connects external tools.

---

## Calculator Server

Performs mathematical calculations.

---

## Streaming

Uses Server-Sent Events (SSE) for incremental responses.

---

## Docker

Packages the complete application.