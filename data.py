from pydantic import BaseModel, EmailStr, computed_field, field_validator


class Meetings(BaseModel):
    id: str
    title: str
    date: str  # YYYY-MM-DD
    start_time: str  # HH:MM
    duration: str  # HH:MM
    notes: str
    participants: list[EmailStr]

    @field_validator("start_time")
    @classmethod
    def validate_start_time(cls, value):
        hours = int(value.split(":")[0])
        minutes = int(value.split(":")[1])
        if not (0 <= hours < 24 and 0 <= minutes < 60):
            raise ValueError("Invalid start time")
        return value

    @computed_field
    def end_time(self) -> str:
        print(self.start_time, type(self.start_time))
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

    @computed_field
    def participants_str(self) -> str:
        return ", ".join(self.participants)
