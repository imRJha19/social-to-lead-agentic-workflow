# Social to Lead Agentic Workflow

## Introduction

This project was developed as part of a **technical internship assignment for ServiceHive**.  
The main objective of this project is to understand how a **conversational AI agent** can analyze chat conversations and convert interested users into qualified leads.

The agent is built for a fictional SaaS product called **AutoStream**, an automated video editing platform for content creators.  
Instead of focusing on UI or deployment, this project focuses on **agent behavior, intent handling, and safe backend execution**.

---

## Project Objective

The agent is designed to:
- Answer basic product and pricing questions
- Identify users who show strong interest
- Collect lead information in a structured, step-by-step manner
- Trigger backend actions only when all required details are available

---

## Key Features

- Intent detection (greeting, product inquiry, high interest)
- RAG-based answers using a local knowledge source
- Multi-turn conversation memory
- Lead qualification flow (Name → Email → Platform)
- Safe tool execution after data validation
- Simple CLI-based interaction

---

## Technologies Used

- **Python** – primary programming language
- **LangGraph** – for managing agent workflow and state
- **LLM API (Gemini/OpenAI compatible)** – for natural language responses
- **RAG** – retrieval from a local Markdown knowledge file
- **CLI (Terminal)** – used for interaction and evaluation

---

social-to-lead-agentic-workflow/
- ├── main.py
- ├── graph.py
- ├── intent.py
- ├── rag.py
- ├── lead.py
- ├── state.py
- ├── tools.py
- └── README.md




---

## How to Run the Project

### Prerequisites
- Python 3.9 or higher
- An API key for the LLM provider

### Steps

1. Clone the repository:
```bash
git clone https://github.com/imRJha19/social-to-lead-agentic-workflow.git
cd social-to-lead-agentic-workflow
User: tell me pricing
Agent: AutoStream offers two plans...

User: i want to try pro
Agent: Great! What's your name?

User: Adarsh
Agent: Thanks! What's your email address?

User: adarsh@gmail.com
Agent: Which platform do you create content on?

User: YouTube
Agent: You're all set! Our team will reach out to you shortly.
```

## Architecture Overview

The agent is implemented using LangGraph, which allows the conversation to be modeled as a state-based workflow.
A central state object stores user intent, conversation history, and lead details.

Each message is first analyzed to detect intent.
If the user asks about pricing or product details, the agent retrieves relevant information from a local knowledge file using a RAG approach.
When high intent is detected, the agent enters a lead qualification flow and collects user details step-by-step.

The backend tool is executed only after all required details are collected, ensuring controlled and safe behavior.

## WhatsApp Integration (Concept)

In a production environment, this agent can be integrated with WhatsApp using a webhook-based backend.
Incoming messages can be forwarded to the agent, and conversation state can be stored using a database or Redis.

This project does not implement WhatsApp integration but explains how it can be done conceptually.

## Notes

The project is intentionally CLI-based for clarity

No model training or fine-tuning is performed

Backend behavior is mocked for demonstration

Focus is on learning real-world agent workflows

## Author

- Adarsh Jha
- B.Tech Student at IIT Jammu
- Interested in Generative AI and Backend Development
## Project Structure

