import json
import os.path
from datetime import datetime

from classes.dataclasses.task import Task
from datastructures import LinkedList


def synchronize_data(tasks: LinkedList, file_path: str) -> None:
    data = [task.to_dict() for task in tasks.gen()]
    create_json_file(file_path, data)


def create_json_file(file_path: str, data: list[dict] | None = None) -> None:
    with open(file_path, "w") as file:
        if data:
            json.dump(data, file, indent=4)
        else:
            json.dump([], file, indent=4)


def get_tasks_from_json(file_path: str) -> list[dict]:
    if not (os.path.exists(file_path)):
        create_json_file(file_path)

    with open(file_path, "r") as file:
        data = json.load(file)
        return data


def store_data(data, file_path: str) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def create_task() -> Task:
    title = str(input("Title:\n"))
    description = str(input("Description:\n"))
    status = str(input("Task Status: [todo | in-progress | done]\n")).lower()

    return Task(title, description, status)


def delete_task(tasks: LinkedList) -> None:
    task_id = str(input("Task id:\n"))

    for task in tasks.gen():
        if task.id == task_id:
            tasks.remove(task)


def update_task(tasks: LinkedList) -> None:
    task_id = str(input("Say task id:\n"))
    for task in tasks.gen():
        if task.id == task_id:
            title = None
            description = None
            status = None

            if str(input("Want update title: [Y/N]\n")).upper() == "Y":
                title = str(input("Title:\n"))
            if str(input("Want update description: [Y/N]\n")).upper() == "Y":
                description = str(input("Description\n"))
            if str(input("Want update status: [Y/N]\n")).upper() == "Y":
                status = str(input("Status [todo | in-progress | done]:\n"))

            if title:
                task.title = title
            if description:
                task.description = description
            if status:
                task.status = status

            if title or description or status:
                update_time = datetime.now()
                task.update_at = update_time

            return
    raise "Task not found"


def list_all_tasks(tasks: LinkedList) -> None:
    for task in tasks.gen():
        print(f"{task}\n")


def list_all_done_tasks(tasks: LinkedList) -> None:
    for task in tasks.gen():
        if task.status == "done":
            print(f"{task}\n")


def list_all_non_done_tasks(tasks: LinkedList) -> None:
    for task in tasks.gen():
        if task.status == "todo":
            print(f"{task}\n")


def list_all_in_progress_tasks(tasks: LinkedList) -> None:
    for task in tasks.gen():
        if task.status == "in-progress":
            print(f"{task}\n")


def mark_as_done(tasks: LinkedList) -> None:
    task_id = str(input("Say task id:\n"))
    for task in tasks.gen():
        if task.id == task_id:
            if task.status != "done":
                task.status = "done"
                task.update_at = datetime.now()
            return
    raise "Task not found"


def mark_as_in_progress(tasks: LinkedList) -> None:
    task_id = str(input("Say task id:\n"))
    for task in tasks.gen():
        if task.id == task_id:
            if task.status != "in-progress":
                task.status = "in-progress"
                task.update_at = datetime.now()
            return
    raise "Task not found"


def mark_as_todo(tasks: LinkedList) -> None:
    task_id = str(input("Say task id:\n"))
    for task in tasks.gen():
        if task.id == task_id:
            if task.status != "todo":
                task.status = "todo"
                task.update_at = datetime.now()
            return
    raise "Task not found"
