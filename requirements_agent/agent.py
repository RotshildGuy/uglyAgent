# import random
# from datetime import date, datetime, timedelta

from google.adk.agents import LlmAgent


# def generate_karley_calendar() -> dict[str, list[str]]:
#     """Generates a random calendar for Karley for the next 7 days."""
#     calendar = {}
#     today = date.today()
#     possible_times = [f"{h:02}:00" for h in range(8, 21)]  # 8 AM to 8 PM

#     for i in range(7):
#         current_date = today + timedelta(days=i)
#         date_str = current_date.strftime("%Y-%m-%d")

#         # Select 8 random unique time slots to increase availability
#         available_slots = sorted(random.sample(possible_times, 8))
#         calendar[date_str] = available_slots

#     print("Karley's calendar:", calendar)

#     return calendar


# KARLEY_CALENDAR = generate_karley_calendar()


# def get_availability(start_date: str, end_date: str) -> str:
#     """
#     Checks Karley's availability for a given date range.

#     Args:
#         start_date: The start of the date range to check, in YYYY-MM-DD format.
#         end_date: The end of the date range to check, in YYYY-MM-DD format.

#     Returns:
#         A string listing Karley's available times for that date range.
#     """
#     try:
#         start = datetime.strptime(start_date, "%Y-%m-%d").date()
#         end = datetime.strptime(end_date, "%Y-%m-%d").date()

#         if start > end:
#             return "Invalid date range. The start date cannot be after the end date."

#         results = []
#         delta = end - start
#         for i in range(delta.days + 1):
#             day = start + timedelta(days=i)
#             date_str = day.strftime("%Y-%m-%d")
#             available_slots = KARLEY_CALENDAR.get(date_str, [])
#             if available_slots:
#                 availability = f"On {date_str}, Karley is available at: {', '.join(available_slots)}."
#                 results.append(availability)
#             else:
#                 results.append(f"Karley is not available on {date_str}.")

#         return "\n".join(results)

#     except ValueError:
#         return (
#             "Invalid date format. Please use YYYY-MM-DD for both start and end dates."
#         )


def create_agent() -> LlmAgent:
    """returns the requirements agent."""
    return LlmAgent(
        model="gemini-2.0-flash",
        name="requirements_agent",
         instruction="""Your primary role is to ensure all essential project information is provided, clear, and consistent. When you receive a project request, perform a comprehensive check against your checklist. If any key information is missing, unclear, or contradictory, formulate a clear, specific question to the user requesting the missing details. Once all requirements are validated, return a message confirming that the specifications are complete.

        **Checklist for Requirements:**
        1.  **Functional Requirements:**
            * Core Functionality: What should the system do?
            * User Stories/Use Cases: How will users interact with the system?
            * Input/Output: What data goes in, and what comes out?
        2.  **Non-Functional Requirements:**
            * Performance: Speed, load times, concurrent users.
            * Security: Data protection, authentication, privacy.
            * Usability: User-friendliness, accessibility.
            * Reliability & Availability: Uptime, error handling.
        3.  **Technical & Architectural Specifications:**
            * Technology Stack: Preferred languages, frameworks, databases.
            * Integrations: External APIs, third-party services.
            * Scalability: Expected growth in users/data.
        4.  **Content and Logic Consistency:**
            * Clarity: Unambiguous language for all stakeholders.
            * Completeness: No obvious gaps, all scenarios considered.
            * Consistency: No contradictions between requirements.
            * Constraints: Budget, timeline, technical limits.
        """,
        description="An agent that ensures all essential project information is provided, clear, and consistent.",
        tools=[],
    )
