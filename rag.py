import os
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage

def rag_answer(state: dict) -> dict:
    # 1. Load the knowledge base
    file_path = "knowledge.md" 
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            knowledge = f.read()
    except FileNotFoundError:
        knowledge = "Knowledge base not found. Please contact support."

    # 2. Initialize the Groq LLM (inside the function)
    llm = ChatGroq(
        model="llama-3.3-70b-versatile", 
        temperature=0
    )

    # 3. Combine instructions + knowledge + user question
    messages = [
        SystemMessage(content=(
            "You are a concise AutoStream salesman. "
            "Rules:\n"
            "1. ONLY use the provided knowledge base.\n"
            "2. Keep responses under 3 sentences.\n"
            "3. Do NOT explain what you are doing or why (no 'I can help with that' or 'Keep in mind').\n"
            "4. Be direct and conversational.\n"
            "5. Use bold text for prices."
            "If the user says they want to sign up or says 'yes' to providing info, "
"respond ONLY with the words: 'LEAD_CAPTURE_START'. "
"Otherwise, answer their question briefly."
        )),
        SystemMessage(content=f"KNOWLEDGE BASE CONTENT:\n{knowledge}"),
        state["messages"][-1] 
    ]

    # 4. Get the response from Groq
    response = llm.invoke(messages)

    # 5. Return the updated state
    return {
        **state,
        "messages": state["messages"] + [AIMessage(content=response.content)]
    }