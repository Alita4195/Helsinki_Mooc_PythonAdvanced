# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):#petrol:int, odemeter:int
        self.__petrol=0
        self.__odmeter=0
    def fill_up(self):
        if self.__petrol<60:
            self.__petrol=60
            return self.__petrol

    # def drive(self, km:int):
    #     if self.__petrol>0: 
    #         self.__odmeter+=km
    #         self.__petrol-=km

    #     if self.__petrol>0:
    #         return self.__petrol
    #     else:
    #         self.__petrol=0
    #         return self.__petrol
    
    def drive(self, km: int):
        if km > self.__petrol:
            km = self.__petrol
 
        self.__odmeter += km
        self.__petrol -= km
        
    # def drive(self, km: int):
    #     # Calculate the distance the car can actually drive with the current petrol
    #     distance_possible = self.__petrol

    #     if km < distance_possible:
    #         self.__odmeter += km
    #         self.__petrol -= km
    #     else:
    #         self.__odmeter += distance_possible
    #         self.__petrol = 0

    def __str__(self):
        return (f"Car: odometer reading {self.__odmeter} km, petrol remaining {self.__petrol} litres")
if __name__ == "__main__":
    car = Car()
    car.fill_up()
    car.drive(10)
    car.drive(20)
    car.drive(10)
    car.drive(20)
    car.drive(5)
    print(car)
