from save import tasks as db

def remove_task(id):
    for data in db.tasks:
        if data['id'] == id:
            print(f"Your task '{data['description']}' has been successfully deleted.")
            db.tasks.remove(data)
        else:
            print(f'No tasks with that id were found.')