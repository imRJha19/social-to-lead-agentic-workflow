# Social to Lead Agentic Workflow

## Introduction

This project was developed as part of a **technical internship assignment for ServiceHive**.  
The objective of this project is to build a **real-world GenAI agent** that can convert normal chat conversations into **qualified business leads**.

The agent is designed for a fictional SaaS product called **AutoStream**, an automated video editing platform for content creators.  
Instead of building a simple chatbot, the focus of this project is on **intent detection, stateful conversation flow, RAG-based answers, and safe backend tool execution**.

---

## Project Objective

The agent is built to:
- Answer product and pricing-related questions accurately
- Detect when a user shows high intent to sign up
- Collect lead details in a structured, step-by-step manner
- Trigger backend actions only after all required data is collected

---

## Key Features

- Intent classification (greeting, pricing inquiry, high-intent lead)
- RAG-based responses using a local knowledge base
- Stateful multi-turn conversation handling
- Lead qualification flow (Name → Email → Platform)
- Guarded backend tool execution
- Command-line (CLI) interface for clarity

---

## Technologies Used

- **Python 3.9+**
- **LangGraph** for agent workflow and state management
- **LLM API (Gemini / OpenAI compatible)**
- **RAG** using a local Markdown knowledge file
- **CLI (Terminal)** for interaction

---

## Project Structure

social-to-lead-agentic-workflow/
- ├── main.py
- ├── graph.py
- ├── intent.py
- ├── rag.py
- ├── lead.py
- ├── state.py
- ├── tools.py
- ├── requirements.txt
- └── README.md


---

## How to Run the Project Locally

### Prerequisites
- Python 3.9 or higher
- An API key for the LLM provider

### Steps

1. Clone the repository:
```bash
git clone https://github.com/imRJha19/social-to-lead-agentic-workflow.git
cd social-to-lead-agentic-workflow

pip install -r requirements.txt

GEMINI_API_KEY=your_api_key_here

python main.py

```
The agent will start in the terminal.
Type exit to stop the program.

User: tell me pricing
Agent: AutoStream offers two plans...

User: i want to try pro.
Agent: Great! What's your name?.

User: Adarsh.
Agent: Thanks! What's your email address?.

User: adarsh@gmail.com.
Agent: Which platform do you create content on?.

User: YouTube.
Agent: You're all set! Our team will reach out to you shortly.

## Architecture Explanation

This project uses LangGraph to implement a state-driven conversational AI agent.
LangGraph was chosen because it allows the agent workflow to be modeled as a graph of deterministic steps, which is closer to how real production agents are built. Instead of relying on a single prompt, each stage of the conversation (intent detection, RAG answering, lead qualification) is handled as a separate node.

A centralized agent state is maintained across the conversation. This state stores information such as the detected intent, user-provided details (name, email, platform), and conversation progress. Because the state persists across turns, the agent can correctly handle multi-step conversations spanning 5–6 messages or more.

When a user asks about pricing or features, the agent uses a Retrieval-Augmented Generation (RAG) approach. Relevant information is retrieved from a local knowledge file and passed to the LLM to ensure accurate and grounded responses. When high intent is detected, the agent transitions into a lead qualification flow and collects details step-by-step. The backend tool is executed only after all required details are present, ensuring safe and controlled behavior.

## WhatsApp Deployment (Conceptual)

In a production setup, this agent can be integrated with WhatsApp using a webhook-based architecture. Incoming WhatsApp messages (via providers like Twilio or WhatsApp Cloud API) would be received by a backend server (e.g., FastAPI). Each message would be associated with a session ID (such as the user’s phone number) and forwarded to the agent.

The agent’s state can be stored in a database or Redis to preserve conversation memory across messages. The agent’s response would then be sent back to the user via the WhatsApp API. This allows the same agent logic to work across multiple channels while maintaining consistent lead qualification behavior.

## Notes

The project is intentionally CLI-based for evaluation clarity

No model training or fine-tuning is performed

Backend behavior is mocked for demonstration

Focus is on learning real-world agent workflows

## Author

- Adarsh Jha
- B.Tech Student, IIT Jammu
- Interested in Generative AI and Backend Development

