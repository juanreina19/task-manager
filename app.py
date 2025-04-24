from func import create_task
from func import show_task

def main():
    while True:
        print(f'\n**TASK MANAGER**\n1. Create task\n2. Remove task\n3. Show tasks\n4. Mark task as completed\n5. Exit')
        op = int(input("Option: "))
        match op:
            case 1:
                task = str(input("Write the description of your task: "))
                create_task.create_task(task)
            case 2:
                break
            case 3:
                show_task.show_tasks()
            case 4:
                break
            case 5:
                print(f'\nYou have exited correctly.')
                return False
            
main()

