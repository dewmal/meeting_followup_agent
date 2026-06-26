from data import Meetings
from db import create_table, insert_meeting


class MeetingManager:
    def __init__(self):
        create_table()
        self._meetings: list[Meetings] = []

    def add_meeting(self, meeting: Meetings):
        insert_meeting(meeting)
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
