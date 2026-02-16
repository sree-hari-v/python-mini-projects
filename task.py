class TodoApp:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                return f.read().splitlines()
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")


app = TodoApp()

while True:
    print("\n1.Add  2.Show  3.Delete  4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        app.add_task(task)

    elif choice == "2":
        app.show_tasks()

    elif choice == "3":
        num = int(input("Task number: ")) - 1
        app.delete_task(num)

    elif choice == "4":
        break