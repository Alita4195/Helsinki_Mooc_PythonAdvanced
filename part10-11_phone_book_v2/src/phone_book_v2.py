# Write your solution here:


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
        return f"{self.name_value}\n{self.numbers_value}\n{self.address_value}"


class PhoneBook:
    def __init__(self):
        self.__persons = {}  # the values should be Person-objects and not lists.

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)  # Create a Person object
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)  # Create a Person object
        self.__persons[name].add_address(address)

    def get_numbers(self, name: str):
        if name not in self.__persons or len(self.__persons[name].numbers()) == 0:
            return "number unknown"
        return self.__persons[name].numbers()

    def get_names(self, number: str):
        for name, person in self.__persons.items():
            if number in person.numbers():
                return name

    def get_address(self, name: str):
        if name in self.__persons:
            return self.__persons[name].address()
        else:
            return "address unknown"

    def get_entry(self, name: str):
        if name in self.__persons:
            return self.__persons[name]
        return None


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
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers is None:
            print("numbers unknown")
        else:
            print("Numbers:", numbers)
            address = self.__phonebook.get_address(name)
            if address is not None:
                print("Address:", address)
            else:
                print("address unknown")

    def search_by_number(self):
        number = input("number: ")
        names = self.__phonebook.get_names(number)
        if names:
            print("Names:", ", ".join(names))
        else:
            print("Name unknown")

    def exit(self):
        pass  # Add your exit logic here

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

# person = Person("Eric")
# print(person.name())
# print(person.numbers())
# print(person.address())
# person.add_number("040-123456")
# person.add_address("Mannerheimintie 10 Helsinki")
# print(person.numbers())
# print(person.address())
# part 1 check


# phonebook = PhoneBook()
# phonebook.add_number("Eric", "02-123456")
# print(phonebook.get_entry("Eric"))
# print(phonebook.get_entry("Emily"))
# part 2 check

application = PhoneBookApplication()
application.execute()
