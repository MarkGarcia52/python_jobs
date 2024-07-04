from car import Car

my_used_car = Car('audi', 'R8', 2024)
print(my_used_car.get_descriptive_name())
my_used_car.read_odometer()

# Tells python to open the Car module and import the class Car

from car import Car

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

import car

my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())


from electric_car import ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
