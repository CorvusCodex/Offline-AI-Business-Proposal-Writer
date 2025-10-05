from utils import run_llama
import json
import datetime
import os

def create_proposal_folder():
    """Create proposals folder if it doesn't exist"""
    if not os.path.exists("proposals"):
        os.makedirs("proposals")

def business_proposal_writer(client_info):
    """
    Generate a comprehensive business proposal based on client information
    """
    prompt = f"""
    Write a detailed, professional business proposal using the following client information:
    
    CLIENT PROJECT DETAILS:
    {client_info}
    
    Please create a comprehensive business proposal that includes:
    
    1. EXECUTIVE SUMMARY
       - Brief overview of the project
       - Key objectives and value proposition
    
    2. PROJECT OVERVIEW
       - Detailed description of the project scope
       - Problem statement and solution
    
    3. OBJECTIVES & GOALS
       - Clear, measurable objectives
       - Success criteria
    
    4. METHODOLOGY & APPROACH
       - Proposed approach and methodology
       - Key activities and processes
    
    5. TIMELINE & MILESTONES
       - Project timeline with key milestones
       - Delivery schedule
    
    6. BUDGET & PRICING
       - Detailed cost breakdown
       - Payment terms and schedule
    
    7. DELIVERABLES
       - Clear list of what will be delivered
       - Acceptance criteria
    
    8. TEAM & EXPERTISE
       - Key team members and their roles
       - Relevant experience
    
    9. TERMS & CONDITIONS
       - Project assumptions
       - Terms and conditions
    
    10. NEXT STEPS
        - Clear call to action
        - Implementation roadmap

    Make the proposal professional, persuasive, and tailored to business clients.
    Use appropriate business language and ensure all sections are comprehensive.
    """
    
    return run_llama(prompt)

def collect_client_information():
    """Collect detailed client information for proposal generation"""
    print("\n📋 BUSINESS PROPOSAL INFORMATION COLLECTION")
    print("=" * 50)
    
    client_data = {
        "client_name": input("Client Company Name: "),
        "contact_person": input("Contact Person: "),
        "project_title": input("Project Title: "),
        "project_description": input("Project Description: "),
        "key_objectives": input("Key Objectives/Goals: "),
        "budget_range": input("Budget Range: "),
        "timeline": input("Project Timeline: "),
        "key_requirements": input("Key Requirements/Specifications: "),
        "target_audience": input("Target Audience/Users: "),
        "success_metrics": input("Success Metrics/KPIs: ")
    }
    
    return format_client_info(client_data)

def format_client_info(client_data):
    """Format client data into a structured string for the AI"""
    formatted_info = f"""
    CLIENT INFORMATION:
    Company: {client_data['client_name']}
    Contact: {client_data['contact_person']}
    
    PROJECT DETAILS:
    Title: {client_data['project_title']}
    Description: {client_data['project_description']}
    
    OBJECTIVES:
    {client_data['key_objectives']}
    
    REQUIREMENTS:
    {client_data['key_requirements']}
    
    TARGET AUDIENCE:
    {client_data['target_audience']}
    
    SUCCESS METRICS:
    {client_data['success_metrics']}
    
    BUDGET & TIMELINE:
    Budget Range: {client_data['budget_range']}
    Timeline: {client_data['timeline']}
    """
    
    return formatted_info

def save_proposal(proposal_content, client_name, project_title):
    """Save proposal to a text file with proper naming"""
    create_proposal_folder()
    
    # Clean filename
    clean_client = "".join(c for c in client_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
    clean_project = "".join(c for c in project_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"proposals/Business_Proposal_{clean_client}_{clean_project}_{timestamp}.txt"
    
    # Add header to the proposal file
    header = f"""BUSINESS PROPOSAL
Generated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Client: {client_name}
Project: {project_title}
{'=' * 50}

"""
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(header + proposal_content)
    
    return filename

def display_proposal_preview(proposal, max_lines=20):
    """Display a preview of the generated proposal"""
    lines = proposal.split('\n')
    print("\n📄 PROPOSAL PREVIEW")
    print("=" * 60)
    for i, line in enumerate(lines[:max_lines]):
        print(line)
    if len(lines) > max_lines:
        print(f"\n... and {len(lines) - max_lines} more lines")
    print("=" * 60)

def main():
    """Main function to run the Business Proposal Writer"""
    print("🤖 OFFLINE AI BUSINESS PROPOSAL WRITER")
    print("=" * 50)
    print("Generate professional business proposals using AI\n")
    
    try:
        # Collect client information
        client_info = collect_client_information()
        
        print("\n🔄 Generating your business proposal...")
        print("This may take a few moments...\n")
        
        # Generate proposal
        proposal = business_proposal_writer(client_info)
        
        # Extract client name and project title for saving
        lines = client_info.split('\n')
        client_name = next((line.split(': ')[1] for line in lines if 'Company:' in line), "Unknown_Client")
        project_title = next((line.split(': ')[1] for line in lines if 'Title:' in line), "Unknown_Project")
        
        # Display preview
        display_proposal_preview(proposal)
        
        # Save proposal
        print("\n💾 Saving proposal...")
        filename = save_proposal(proposal, client_name, project_title)
        print(f"✅ Proposal saved as: {filename}")
        
        # Additional options
        print("\n🎯 NEXT STEPS:")
        print("1. Review the generated proposal")
        print("2. Customize specific sections as needed")
        print("3. Add your company branding and contact information")
        print("4. Send to client for review")
        
    except Exception as e:
        print(f"❌ Error generating proposal: {e}")
        print("Please check your AI model setup and try again.")

if __name__ == "__main__":
    main()
