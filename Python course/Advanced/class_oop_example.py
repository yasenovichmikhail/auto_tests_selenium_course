
class Car:
 
    # создаем атрибуты класса
    car_count = 0
 
    # создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1


car_a = Car()  
car_a.start("Corrola", "Toyota", 2015)  
print(car_a.name)  
print(car_a.car_count)

car_b = Car()  
car_b.start("City", "Honda", 2013)  
print(car_b.name)  
print(car_b.car_count)

#переопределение метода __str__
class Car:
 
    # создание методов класса
    def __str__(self):
        return "Car class Object"
 
    def start(self):
        print ("Двигатель заведен")
 
car_a = Car()  
print(car_a)

# статичный метод, вызов напрямую
class Car:
 
    @staticmethod
    def get_class_details():
        print ("Это класс Car")
 
Car.get_class_details()

#конструктор при создании объекта
class Car:
 
    # создание атрибутов класса
    car_count = 0
 
    # создание методов класса
    def __init__(self):
        Car.car_count +=1
        print(Car.car_count)

# публичный, приватный, защищенный доступ (' ', '__', '_')
class Car:  
    def __init__(self):
        print ("Двигатель заведен")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 1999