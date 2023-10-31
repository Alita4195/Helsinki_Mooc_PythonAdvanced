# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str):
        self.name_value = name
        self.numbers_value = []
        self.address_value = None

    def add_number(self, number):
        self.numbers_value.append(number)

    def add_address(self, address: str):
        self.address_value = address

    def name(self):
        return self.name_value

    def numbers(self):
        return self.numbers_value

    def address(self):
        return self.address_value

    def __str__(self):
        return f"Name: {self.name_value}, Numbers: {self.numbers_value}, Address: {self.address_value}"


class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_person(self, person):
        self.__persons[person.name()] = person

    def get_person(self, name):
        return self.__persons.get(name, None)

    def __str__(self):
        result = []
        for person in self.__persons.values():
            result.append(str(person))
        return "\n".join(result)


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 add address")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        person = Person(name)
        person.add_number(number)
        self.__phonebook.add_person(person)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        person = self.__phonebook.get_person(name)
        if person is not None:
            person.add_address(address)

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_person(name)
        if person is not None:
            print(person)
        else:
            print("Person not found.")

    def exit(self):
        exit

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# Running the application
application = PhoneBookApplication()
application.execute()
