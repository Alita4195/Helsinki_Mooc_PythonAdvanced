# Write your solution here:
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


if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
