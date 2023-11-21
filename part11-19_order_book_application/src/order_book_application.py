# Write your solution here
class Task:
    id = 0  # Class variable to keep track of task IDs

    def __init__(self, description, programmer, workload):
        Task.id += 1
        self.id = Task.id
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self):
        self.orders = set()  # {}set

    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.orders.add(task)

    def all_orders(self):
        return sorted(self.orders, key=lambda task: task.id)

    def programmers(self):
        return sorted(set(task.programmer for task in self.orders))

    def mark_finished(self, id: int):
        for task in self.orders:
            if task.id == id:
                task.mark_finished()
                break
        else:
            raise ValueError

    def finished_orders(self):
        return [task for task in self.orders if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.orders if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        finished_task_count = 0
        unfinished_task_count = 0
        finished_task_hour = 0
        unfinished_task_hour = 0
        programmer_found = False
        for task in self.orders:
            if task.programmer == programmer:
                programmer_found = True  # Set the flag to True
                if task.is_finished():
                    finished_task_count += 1
                    finished_task_hour += task.workload
                else:
                    unfinished_task_count += 1
                    unfinished_task_hour += task.workload
        if not programmer_found:
            raise ValueError

        return (
            finished_task_count,
            unfinished_task_count,
            finished_task_hour,
            unfinished_task_hour,
        )

    def applications(self):
        print(
            "commands:\n 0 exit\n 1 add order\n 2 list finished tasks\n 3 list unfinished tasks\n 4 mark task as finished\n 5 programmers\n 6 status of programmer"
        )

        # while True:
        command = input("command: ")

        # try:
        if command == "0":
            exit()
        elif command == "1":
            description = input("description: ")
            info = input("programmer and workload estimate: ")
            parts = info.split()

            if len(parts) != 2:
                raise ValueError("erroneous input")

            programmer = parts[0]
            workload = int(parts[1])

            self.add_order(description, programmer, workload)
            print("added!")

        elif command == "2":
            finished_tasks = self.finished_orders()

            for task in finished_tasks:
                print(task)

        elif command == "3":
            unfinished_tasks = self.unfinished_orders()

            for task in unfinished_tasks:
                print(task)

        elif command == "4":
            task_id = input("id: ")
            if not task_id.isdigit():
                raise ValueError("erroneous input")
            self.mark_finished(int(task_id))
            print("marked as finished")

        elif command == "5":
            programmers = self.programmers()
            print("Programmers:", programmers)

        elif command == "6":
            programmer = input("programmer: ")
            if not any(task.programmer == programmer for task in self.orders):
                raise ValueError("erroneous input")
            status = self.status_of_programmer(programmer)
            print(status)
            # except ValueError:
            #     print("Erroneous input")


if __name__ == "__main__":
    orders = OrderBook()
    orders.applications()
