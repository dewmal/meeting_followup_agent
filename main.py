from dotenv import load_dotenv

from data import Meetings
from meetings_mgt import MeetingManager

load_dotenv()


def main():
    print("Hello from ai-meeting-follow-up-agent!")


if __name__ == "__main__":
    manager = MeetingManager()
    manager.add_meeting(
        Meetings(
            id="1",
            title="test",
            date="2026-07-10",
            start_time="10:00",
            duration="01:00",
            notes="Na",
            participants=["abc@example.com"],
        )
    )
    manager.update_meeting(
        "1",
        Meetings(
            id="1",
            title="test",
            date="2026-07-10",
            start_time="12:00",
            duration="01:00",
            notes="Na",
            participants=["abc@example.com"],
        ),
    )
    print(manager.get_meetings())
