def mock_lead_capture(name: str, email: str, platform: str) -> str:
    """
    Mock function to simulate capturing a lead into a CRM or database.
    This fulfills the 'Tool Execution' requirement of the AutoStream assignment.
    """
    
    print("\n" + "="*50)
    print("🚀 [CRM SYSTEM] NEW LEAD DETECTED")
    print(f"👤 Name:     {name}")
    print(f"📧 Email:    {email}")
    print(f"📱 Platform: {platform}")
    print("="*50 + "\n")
    
    return "Success: Lead recorded in the system."