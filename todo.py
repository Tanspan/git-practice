tasks = [1,2,3,4,5]

def show_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_tasks(task):
    tasks.append(task)

def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)
        print("Task deleted")
    else:
        print("Invalid index")

if __name__ == "__main__":
    show_tasks()