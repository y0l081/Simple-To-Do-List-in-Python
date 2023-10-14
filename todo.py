class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added: {task}")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Removed: {task}")
        else:
            print("Task not found.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")


def main():
    todo_list = ToDoList()
    while True:
        print("\nSimple To-Do List")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
