# AI Text Summarizer using n8n and OpenAI GPT-4.1

## Overview

This project is an AI-powered text summarization workflow built using **n8n** and **OpenAI GPT-4.1**. It receives text through an HTTP Webhook, processes the input using a Large Language Model (LLM), summarizes the content into three bullet points, identifies action items if present, transforms the response into a structured JSON format, and returns the processed output.

This project was developed as part of the technical assignment provided by **OS3 Infotech Pvt. Ltd.**

---

## Features

- HTTP Webhook Trigger
- OpenAI GPT-4.1 Integration
- AI-based Text Summarization
- Action Item Detection
- JavaScript Data Transformation
- JSON Response Generation
- API Testing using Postman

---

## Technologies Used

- n8n
- OpenAI GPT-4.1
- JavaScript
- HTTP Webhook
- Postman

---

## Workflow Architecture

```
Client (Postman)
        │
        ▼
Webhook Trigger
        │
        ▼
OpenAI GPT-4.1
(Message a Model)
        │
        ▼
Code Node
(JavaScript)
        │
        ▼
Respond to Webhook
(JSON Response)
```

---

## Data Flow

1. Client sends an HTTP POST request through Postman.
2. The Webhook node receives the request.
3. The input text is forwarded to OpenAI GPT-4.1.
4. GPT-4.1 summarizes the text and detects action items.
5. The Code node extracts the required information and adds a timestamp.
6. The final JSON response is returned to the client.

---

## Workflow Logic

### Webhook

- Accepts HTTP POST requests
- Starts the workflow
- Receives input in JSON format

### OpenAI (Message a Model)

- Receives input text
- Generates a summary
- Detects action items

### Code Node

- Extracts summary from the OpenAI response
- Adds timestamp
- Returns structured JSON

### Respond to Webhook

- Sends the processed response back to the client

---

## Project Structure

```
AI_Text_Summarizer/
│
├── AI_Text_Summarizer.json
├── README.md
```

---

## Sample Input

```json
{
  "text": "MS Dhoni is an Indian professional cricketer who plays as a right-handed batter and wicket-keeper. He captained India to multiple ICC tournament victories."
}
```

---

## Sample Output

```json
{
  "timestamp": "2026-07-14T08:17:18.806Z",
  "summary": "Summary:
- MS Dhoni is one of India's greatest captains.
- He led India to multiple ICC tournament victories.
- He is regarded as one of the greatest wicket-keeper batsmen.

Action Items:
No action items found."
}
```

---

## How to Run

1. Import the provided `AI_Text_Summarizer.json` workflow into n8n.
2. Activate the workflow.
3. Copy the Webhook URL.
4. Open Postman.
5. Create a POST request using the Webhook URL.
6. Set the request body to **JSON**.
7. Provide the input text.
8. Send the request.
9. View the generated summary in the workflow execution or webhook response.

---

## Deliverables

- Exported n8n Workflow (`AI_Text_Summarizer.json`)
- README Documentation
- Example Input
- Example Output

---

## Author

**Sneha Shrinivas Dubhashi**
