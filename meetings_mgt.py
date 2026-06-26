from data import Meetings
from db import (
    create_table,
    delete_meeting,
    get_meeting,
    get_meetings,
    insert_meeting,
    update_meeting,
)


class MeetingManager:
    def __init__(self):
        create_table()

    def add_meeting(self, meeting: Meetings):
        insert_meeting(meeting)

    def get_meetings(self) -> list[Meetings]:
        return get_meetings()

    def delete_meeting(self, meeting_id: str):
        delete_meeting(meeting_id)

    def update_meeting(self, meeting_id: str, meeting: Meetings):
        update_meeting(meeting_id, meeting)

    def get_meeting(self, meeting_id: str) -> Meetings | None:
        return get_meeting(meeting_id)
