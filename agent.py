from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel

from data import Meetings
from meetings_mgt import MeetingManager

load_dotenv()

model = GroqModel("llama-3.3-70b-versatile")
agent = Agent(model)

meeting_manager = MeetingManager()


@agent.tool_plain
def add_meeting(
    id: str,
    title: str,
    date: str,  # YYYY-MM-DD
    start_time: str,  # HH:MM
    duration: str,  # HH:MM
    notes: str,
    participants: list,
):
    print(
        f"Adding meeting: {title}, {date}, {start_time}, {duration}, {notes}, {participants}"
    )
    meeting = Meetings(
        id=id,
        title=title,
        date=date,
        start_time=start_time,
        duration=duration,
        notes=notes,
        participants=participants,
    )
    meeting_manager.add_meeting(meeting)
    return f"Meeting '{title}' has been added."


if __name__ == "__main__":
    result = agent.run_sync(
        "Create a meeting titled 'Team Meeting' on 2026-07-06 at 10:00 AM for 1 hour with participants [john@example.com, jane@example.com]"
    )
    print(result)
