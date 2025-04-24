from save import tasks as db

def show_tasks():
    if not db.tasks:
        print(f'There are no registered tasks!')
        return
    
    print(f'\n**TO-DO LIST**')
    for task in db.tasks:
        status = '✅' if task['completed'] else '❌'
        print(f"- Description: {task['description']} | Completed: {status} | ID: {task['id']}")
