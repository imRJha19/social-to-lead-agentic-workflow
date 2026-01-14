from langgraph.graph import StateGraph, END
from langchain_core.messages import AIMessage
from state import AgentState
from intent import detect_intent
from rag import rag_answer
from lead import lead_qualification

def intent_router(state: AgentState) -> str:
    # 1. Get the detected intent
    intent = state.get("intent")
    
    # 2. Check if we are ALREADY in the middle of a lead
    # We only stay in 'lead' if the name has been captured already.
    # This prevents 'Hi' from triggering the form.
    lead_data = state.get("lead_data", {})
    if lead_data.get("name") and not state.get("lead_complete"):
        return "lead"

    # 3. If the user just chose a plan (High Intent), go to lead
    if intent == "high_intent":
        return "lead"
    
    # 4. If the user is asking about plans/pricing, go to RAG
    if intent == "product_pricing":
        return "rag"
    
    # 5. Otherwise, just greet
    return "greeting"

def greeting_node(state: AgentState) -> dict:
    return {
        "messages": [AIMessage(content="Hi! 👋 I can help you with AutoStream pricing, features, or help you get started.")]
    }

def build_graph():
    """
    Builds the graph. All paths eventually lead to END so the 
    terminal can wait for your next message.
    """
    graph = StateGraph(AgentState)

    # Nodes
    graph.add_node("intent", detect_intent)
    graph.add_node("rag", rag_answer)
    graph.add_node("greeting", greeting_node)
    graph.add_node("lead", lead_qualification)

    # Entry point
    graph.set_entry_point("intent")

    # Routing logic from the intent node
    graph.add_conditional_edges(
        "intent",
        intent_router,
        {
            "rag": "rag",
            "greeting": "greeting",
            "lead": "lead"
        }
    )

    # Path finishes
    # After RAG or Greeting, we wait for user input (END)
    graph.add_edge("rag", END)
    graph.add_edge("greeting", END)
    
    # After Lead asks a question (like "What is your name?"), 
    # it must go to END so you can type your answer.
    graph.add_edge("lead", END)

    return graph.compile()