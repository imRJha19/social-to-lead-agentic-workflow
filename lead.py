from langchain_core.messages import AIMessage
from tool import mock_lead_capture
import re

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def lead_qualification(state: dict) -> dict:
    """
    Manages the lead collection. 
    Order: Plan -> Name -> Email -> Platform
    """
    lead_data = state.get("lead_data", {}).copy()
    messages = state.get("messages", [])
    
    if not messages:
        return {"lead_data": lead_data}

    last_user_msg = messages[-1].content

    # 1. DATA HARVESTING (Save what the user just said)
    if len(messages) >= 2:
        last_agent_msg = messages[-2].content.lower()
        
        # If agent asked for plan
        if "which plan" in last_agent_msg:
            lead_data["plan"] = last_user_msg
        # If agent asked for name
        elif "name?" in last_agent_msg:
            lead_data["name"] = last_user_msg
        # If agent asked for email
        elif "email address" in last_agent_msg:
            if is_valid_email(last_user_msg):
                lead_data["email"] = last_user_msg
        # If agent asked for platform
        elif "platform" in last_agent_msg:
            lead_data["platform"] = last_user_msg

    # 2. THE QUESTIONS (The Sequence)

    # STEP A: Ask for Plan (The missing piece!)
    if not lead_data.get("plan"):
        return {
            "lead_data": lead_data,
            "messages": [AIMessage(content="I'd love to help you get started! Which plan would you like to go with: the Basic Plan ($29) or the Pro Plan ($79)?")]
        }

    # STEP B: Ask for Name
    if not lead_data.get("name"):
        return {
            "lead_data": lead_data,
            "messages": [AIMessage(content=f"Great choice with the {lead_data['plan']}! To set that up, what's your name?")]
        }

    # STEP C: Ask for Email
    if not lead_data.get("email"):
        return {
            "lead_data": lead_data,
            "messages": [AIMessage(content=f"Nice to meet you, {lead_data['name']}! What's a good email address for you?")]
        }

    # STEP D: Ask for Platform
    if not lead_data.get("platform"):
        return {
            "lead_data": lead_data,
            "messages": [AIMessage(content="Got it. And which platform do you create content for? (YouTube, Instagram, etc.)")]
        }

    # STEP E: FINALIZE
    if not state.get("lead_complete"):
        mock_lead_capture(
            name=lead_data["name"], 
            email=lead_data["email"], 
            platform=lead_data["platform"]
        )
        return {
            "lead_data": lead_data,
            "lead_complete": True,
            "messages": [AIMessage(content=f"🎉 You're all set! We've registered your interest for the {lead_data['plan']}. Our team will reach out to {lead_data['email']} soon.")]
        }

    return {"lead_data": lead_data}