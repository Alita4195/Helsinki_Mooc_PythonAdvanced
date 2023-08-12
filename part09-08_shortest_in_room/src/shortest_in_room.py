# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"


class Room:
    def __init__(self):
        self.persons = []
        self.total_height_list = []
        self.count = 0

    def add(self, person: Person):
        self.persons.append(person)
        self.total_height_list.append(person.height)
        self.count += 1
        return self.count, self.total_height_list  # both are lists

    def shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            shortest_person = self.persons[0]  # Assume the first person is the shortest
            for person in self.persons:
                if person.height < shortest_person.height:
                    shortest_person = person
            return shortest_person

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {sum(self.total_height_list)} cm")
        for item in self.persons:
            print(item)

    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person is not None:
            self.persons.remove(shortest_person)
            return shortest_person
        return None


if __name__ == "__main__":
    room = Room()
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    if removed:
        print(f"Removed from room: {removed}")
    else:
        print("No one was removed from the room.")

    print()

    room.print_contents()
