from todo_list import TodoList

def main():
    todo = TodoList()
    while True:
        print("\n1. Add Task\n2. Show Tasks\n3. Mark Done\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == '2':
            todo.show_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark done: "))
            todo.mark_done(task_id)
        elif choice == '4':
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
