# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length: int):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("Recording length should be greater than 0")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length: int):
        if new_length > 0:
            self.__length = new_length
        else:
            raise ValueError("Recording length should be greater than 0")


if __name__ == "__main__":
    the_wall = Recording(-1)
    print(the_wall.length) 
    the_wall.length = 44
    print(the_wall.length)  

