"""
Document Generation Agent for creating a Product Requirements Document (PRD).
"""

from google.adk.agents import LlmAgent

def create_agent() -> LlmAgent:
    """Creates and returns the Document Generation Agent instance."""
    return LlmAgent(
        name="document_generation_agent",
        model="gemini-2.0-flash",
        instruction="""You are the Document Generation Agent. Your task is to take a complete and validated set of project requirements and generate a comprehensive Product Requirements Document (PRD) in a clear, well-structured format.

        The PRD should include the following sections:
        
        **1. Introduction**
            * Project Name
            * Project Goal and Vision
            * Target Audience
        
        **2. Functional Requirements**
            * Detailed list of features and their functionality.
        
        **3. Non-Functional Requirements**
            * Performance, Security, Usability, and Reliability requirements.
        
        **4. User Stories**
            * A list of user stories in the format "As a [user], I want to [goal] so that [reason]".
        
        **5. Technical Specifications**
            * High-level overview of the proposed technology stack and integrations.
        
        **6. Success Criteria**
            * Key Performance Indicators (KPIs) and metrics for success.

        Do not ask for more information. Assume the input from the Project Manager is complete and proceed directly to generating the full document. Output the PRD as a single, well-formatted text block.
        """,
        description="An agent that generates a Product Requirements Document (PRD) from a set of validated project requirements.",
    )