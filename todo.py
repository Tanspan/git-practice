tasks = [1,2,3,4,5]

def show_tasks():
    print(tasks)
<<<<<<< HEAD
def add_tasks(task):
    tasks.append(task)
=======
def show_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

>>>>>>> feature-show
if __name__ == "__main__":
    show_tasks()
