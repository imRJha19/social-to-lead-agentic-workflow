import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq  # New import
from graph import build_graph

# 1. Load the API key from your .env file
load_dotenv()

def main():
    # Verify Groq API key is loaded
    if not os.getenv("GROQ_API_KEY"):
        print("Error: GROQ_API_KEY not found. Check your .env file.")
        return

    # Initialize the Groq Model
    # llama-3.3-70b-versatile is a great all-rounder
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    print("AutoStream Agent (Groq Edition) - type 'exit' to quit")
    
    # ... rest of your main logic (build_graph, app.invoke, etc)

    app = build_graph()

    state = {
        "messages": [],
        "intent": None,
        "lead_data": {
            "name": None,
            "email": None,
            "platform": None,
        },
        "lead_complete": False,
    }

    print("AutoStream Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        # Store lead info if we are in high-intent flow
        if state["intent"] == "high_intent":
            if state["lead_data"]["name"] is None:
                state["lead_data"]["name"] = user_input
            elif state["lead_data"]["email"] is None:
                # Validation check: Only save if it looks like an email
                if "@" in user_input and "." in user_input:
                    state["lead_data"]["email"] = user_input
            elif state["lead_data"]["platform"] is None:
                state["lead_data"]["platform"] = user_input

        # Add user message
        state["messages"].append(HumanMessage(content=user_input))

        # Invoke LangGraph
        state = app.invoke(state)

        # Print agent response
        print("Agent:", state["messages"][-1].content)


if __name__ == "__main__":
    main()