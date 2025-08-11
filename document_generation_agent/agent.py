"""
Document Generation Agent for creating a Product Requirements Document (PRD).
"""

from google.adk.agents import LlmAgent

def create_agent() -> LlmAgent:
    """Creates and returns the Document Generation Agent instance."""
    return LlmAgent(
        name="document_generation_agent",
        model="gemini-2.0-flash",
        instruction="""You are the Document Generation Agent. Your task is to take a complete set of project requirements and generate a **brief and concise** Product Requirements Document (PRD) with a maximum length of 200 words. The PRD should only include the following sections:

        **1. Introduction**
        **2. Functional Requirements**
        **3. User Stories**

        Do not ask for more information. Assume the input from the Project Manager is complete and proceed directly to generating the short document.
        """,
        description="An agent that generates a Product Requirements Document (PRD) from a set of validated project requirements.",
    )