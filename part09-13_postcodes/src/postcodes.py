# Add the requested members to the class below:

class City:
    postcodes = {
        "Helsinki": "00100",
        "Turku": "20100",
        "Tampere": "33100",
        "Rovaniemi": "96100",
        "Oulu": "90100",
    }

    def __init__(self, name: str, postcode: str):
        self.__name = name
        self.__postcode = postcode

    @property
    def name(self):
        return self.__name

    @property
    def postcode(self):
        return postcodes

    def __str__(self):
        return f"{self.__name} {self.__postcode}"


if __name__ == "__main__":
    print(City("Helsinki", "00100"))
    print(City.postcodes)
