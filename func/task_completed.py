from save import tasks as db

def completed_task(id):
    if not db.tasks:
        print("There are no registered task")
    for data in db.tasks:
        if data['id'] == id and data['completed'] == False:
            data['completed'] = True
            print(f"Your task '{data['description']}' has been completed.")
            return
        elif data['id'] == id and data['completed'] == True:
            print(f'This task has already been completed.')
        else:
            print(f'No task found with that id!')