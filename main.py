from pydantic import BaseModel


class Meetings(BaseModel):
    id: str
    title: str
    date: str
    start_time: str
    duration: str
    notes: str


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


def main():
    print("Hello from ai-meeting-follow-up-agent!")


if __name__ == "__main__":
    m = Meetings(id="1", title="", date="", start_time="", duration="", notes="")
    print(m)
