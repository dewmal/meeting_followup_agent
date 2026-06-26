import sqlite3
from unittest.main import main

from data import Meetings

DB_NAME = "meeting.db"


def get_db_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meetings (
            id TEXT PRIMARY KEY,
            title TEXT,
            date TEXT,
            start_time TEXT,
            duration TEXT,
            notes TEXT,
            participants TEXT
        )
    """)
    conn.commit()
    conn.close()


def insert_meeting(meeting: Meetings):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO meetings (id, title, date, start_time, duration, notes, participants)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (
            meeting.id,
            meeting.title,
            meeting.date,
            meeting.start_time,
            meeting.duration,
            meeting.notes,
            meeting.participants_str,
        ),
    )
    conn.commit()
    conn.close()


def get_meetings() -> list[Meetings]:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM meetings")
    rows = cursor.fetchall()
    conn.close()
    meetings = []
    for row in rows:
        meeting = Meetings(
            id=row[0],
            title=row[1],
            date=row[2],
            start_time=row[3],
            duration=row[4],
            notes=row[5],
            participants=row[6].split(","),
        )
        meetings.append(meeting)

    return meetings


def delete_meeting(meeting_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM meetings WHERE id = ?", (meeting_id,))
    conn.commit()
    conn.close()


def update_meeting(meeting_id: str, meeting: Meetings):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE meetings
        SET title = ?, date = ?, start_time = ?, duration = ?, notes = ?, participants = ?
        WHERE id = ?
        """,
        (
            meeting.title,
            meeting.date,
            meeting.start_time,
            meeting.duration,
            meeting.notes,
            meeting.participants_str,
            meeting_id,
        ),
    )
    conn.commit()
    conn.close()


def get_meeting(meeting_id: str) -> Meetings | None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM meetings WHERE id = ?", (meeting_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Meetings(
            id=row[0],
            title=row[1],
            date=row[2],
            start_time=row[3],
            duration=row[4],
            notes=row[5],
            participants=row[6].split(","),
        )
    return None
