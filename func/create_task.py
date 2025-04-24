from save import tasks as taskdb
import uuid

def generated_unique_id():
    return str(uuid.uuid4())

def create_task(description: str):
    new_task = {
        "id": generated_unique_id(),
        "description": description,
        "completed": False
    }
    taskdb.tasks.append(new_task)
    print(f'Your task was added successfully')