from dataclasses import dataclass, field
from uuid import uuid4
from datetime import datetime


STATUS = ("todo", "in-progress", "done")
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


@dataclass
class Task:
    _id: str = field(init=False, default_factory=lambda: str(uuid4()))
    _title: str
    _description: str
    _status: str
    _create_at: datetime = field(init=False, default_factory=datetime.now)
    _update_at: datetime = field(init=False)

    @classmethod
    def from_dict(cls, task: dict) -> "Task":
        print(task.keys())
        task_obj = Task(task["title"], task["description"], task["status"])
        task_obj._id = task["id"]
        task_obj._create_at = datetime.strptime(task["create_at"], DATE_FORMAT)
        task_obj._update_at = datetime.strptime(task["update_at"], DATE_FORMAT)

        return task_obj

    def __post_init__(self) -> None:
        self._update_at = self._create_at
        if not self.status in STATUS:
            raise f"Invalid status: {self._status}"

        if not (isinstance(self._title, str)):
            self._title = str(self._title)

        if not (isinstance(self._description, str)):
            self._description = str(self._description)

    @property
    def id(self) -> str:
        return self._id

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        if status in STATUS:
            self._status = status
        else:
            raise f"Invalid status: {status!r}"

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        if not (isinstance(title, str)):
            title = str(title)
        self._title = title

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        if not (isinstance(description, str)):
            description = str(description)
        self._description = description

    @property
    def create_at(self) -> datetime:
        return self._create_at

    @property
    def update_at(self) -> datetime:
        return self._update_at

    @update_at.setter
    def update_at(self, date: datetime) -> None:
        if isinstance(date, datetime) and date > self.create_at:
            self._update_at = date
        else:
            raise f"Invalid datetime: {date!r}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "create_at": self.create_at.strftime(DATE_FORMAT),
            "update_at": self.update_at.strftime(DATE_FORMAT),
        }

    def __str__(self) -> str:
        return f"""Title:\t {self.title}
Description:\t {self.description}
Status:\t {self.status}
Create At:\t {self.create_at.strftime(DATE_FORMAT)}
Update At:\t {self.update_at.strftime(DATE_FORMAT)}
Id:\t {self.id}"""
