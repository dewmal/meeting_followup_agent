from pydantic import BaseModel, EmailStr
from pydantic.fields import computed_field


class Meetings(BaseModel):
    id: str
    title: str
    date: str  # YYYY-MM-DD
    start_time: str  # HH:MM
    duration: str  # HH:MM
    notes: str
    participants: list[EmailStr]

    @computed_field
    def end_time(self) -> str:
        hours, minutes = map(int, self.duration.split(":"))
        print(
            f"start_time: {self.start_time}, duration: {self.duration}",
            self.start_time.split(":"),
        )
        start_time = int(self.start_time.split(":")[0])
        start_minute = int(self.start_time.split(":")[1])
        end_hour = start_time + hours
        end_minute = start_minute + minutes

        # Need to handle minute overflow and hour overflow and day overflow

        return f"{end_hour:02d}:{end_minute:02d}"


class MeetingManager:
    def __init__(self):
        self._meetings: list[Meetings] = []

    def add_meeting(self, meeting: Meetings):
        self._meetings.append(meeting)

    def get_meetings(self) -> list[Meetings]:
        return self._meetings

    def delete_meeting(self, meeting_id: str):
        for meeting in self._meetings:
            if meeting.id == meeting_id:
                self._meetings.remove(meeting)
                break

    def update_meeting(self, meeting_id: str, meeting: Meetings):
        for i, m in enumerate(self._meetings):
            if m.id == meeting_id:
                self._meetings[i] = meeting
                break

    def get_meeting(self, meeting_id: str) -> Meetings | None:
        for meeting in self._meetings:
            if meeting.id == meeting_id:
                return meeting
        return None


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
    print(manager.get_meetings())
    manager.update_meeting(
        "1",
        Meetings(
            id="1",
            title="test",
            date="2026-07-10",
            start_time="11:00",
            duration="01:00",
            notes="Na",
            participants=["abc@example.com"],
        ),
    )
    print(manager.get_meetings())

    m = manager.get_meeting("1")
    print(m.end_time)
