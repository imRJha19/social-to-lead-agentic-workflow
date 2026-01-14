def detect_intent(state: dict) -> dict:
    """
    Rule-based intent detection.
    This version properly triggers the lead flow and stays there until finished.
    """
    # 1. Safety check for messages
    if not state.get("messages"):
        return {**state, "intent": "greeting"}
        
    text = state["messages"][-1].content.lower()
    lead_data = state.get("lead_data", {})
    lead_complete = state.get("lead_complete", False)

    # 2. THE LOCK: If we are in the middle of lead capture, DON'T change the intent.
    # We check if lead_data has started OR if the last AI message was a lead question.
    # This keeps the user 'trapped' in the form until it is done.
    if lead_data and not lead_complete:
        return {**state, "intent": "high_intent"}

    # 3. HIGH-INTENT: User is choosing a plan or wants to sign up.
    # This is the "Doorway" into the lead flow.
    high_intent_triggers = [
        "buy", "sign up", "signup", "subscribe", "get started",
        "choose", "want the", "pro plan", "basic plan", "selected"
    ]
    
    if any(w in text for w in high_intent_triggers):
        return {**state, "intent": "high_intent"}
    
    # 4. PRODUCT/PRICING: User is still just asking questions (RAG flow).
    elif any(w in text for w in ["price", "pricing", "cost", "features", "how much", "difference"]):
        return {**state, "intent": "product_pricing"}
    
    # 5. GREETING: Default fallback.
    else:
        return {**state, "intent": "greeting"}