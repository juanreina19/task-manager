from save import tasks
import uuid

def generated_unique_id():
    return str(uuid.uuid4())

def create_task(description):
    new_task = {
        "id": generated_unique_id(),
        "description": description,
        "completed": False
    }
    tasks.append(new_task)