from langchain_core.messages import AIMessage

def rag_answer(state: dict) -> dict:
    """
    Simple RAG using local Markdown knowledge file.
    """

    query = state["messages"][-1].content.lower()

    with open("knowledge/autostream.md", "r") as f:
        knowledge = f.read()

    # Simple keyword-based retrieval
    if "pro" in query:
        retrieved = knowledge.split("## Pro Plan")[1]
    elif "basic" in query:
        retrieved = knowledge.split("## Basic Plan")[1]
    elif "refund" in query or "policy" in query:
        retrieved = knowledge.split("## Policies")[1]
    else:
        retrieved = knowledge

    return {
        **state,
        "messages": state["messages"] + [
            AIMessage(content=retrieved.strip())
        ]
    }
