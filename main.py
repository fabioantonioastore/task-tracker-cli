from utils.task import *
from datastructures import LinkedList


JSON_FILE = "data.json"

if __name__ == "__main__":
    data = get_tasks_from_json("data.json")
    linked_list = LinkedList()
    if data:
        for task in data:
            task = Task.from_dict(task)
            linked_list.append(task)

    while True:
        print(
            """
        What do you want to do:
        1 - Create Task
        2 - Delete Task
        3 - Update Task
        4 - Show all tasks
        5 - Show all done tasks
        6 - Show all non-done tasks
        7 - Mark in Progress
        8 - Mark Done
        9 - Mark ToDo
        CTRL + C to Exit"""
        )

        awnser = int(input("\n"))

        match awnser:
            case 1:
                task = create_task()
                linked_list.append(task)
                synchronize_data(linked_list, JSON_FILE)
            case 2:
                delete_task(linked_list)
                synchronize_data(linked_list, JSON_FILE)
            case 3:
                update_task(linked_list)
                synchronize_data(linked_list, JSON_FILE)
            case 4:
                list_all_tasks(linked_list)
            case 5:
                list_all_done_tasks(linked_list)
            case 6:
                list_all_non_done_tasks(linked_list)
            case 7:
                mark_as_in_progress(linked_list)
                synchronize_data(linked_list, JSON_FILE)
            case 8:
                mark_as_done(linked_list)
                synchronize_data(linked_list, JSON_FILE)
            case 9:
                mark_as_todo(linked_list)
                synchronize_data(linked_list, JSON_FILE)
            case _:
                raise f"Invalid option: {awnser}"
