tasks = [1,2,3,4,5]

def show_tasks():
    print(tasks)
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)
        print("Task deleted")
    else:
        print("Invalid index")

if __name__ == "__main__":
    show_tasks()
