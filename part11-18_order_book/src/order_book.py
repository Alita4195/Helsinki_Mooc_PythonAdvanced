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
        self.orders = set()

    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.orders.add(task)

    def all_orders(self):
        return sorted(self.orders, key=lambda task: task.id)

    def programmers(self):
        return sorted(set(task.programmer for task in self.orders))


# t1 = Task("program hello world", "Eric", 3)
# print(t1.id, t1.description, t1.programmer, t1.workload)
# print(t1)
# print(t1.is_finished())
# t1.mark_finished()
# print(t1)
# print(t1.is_finished())
# t2 = Task("program webstore", "Adele", 10)
# t3 = Task("program mobile app for workload accounting", "Eric", 25)
# print(t2)
# print(t3)

orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

for order in orders.all_orders():
    print(order)

print()

for programmer in orders.programmers():
    print(programmer)
