from classes.car_class import Car
from classes.engine_class import Engine


car1=Car()
car1.year=2022
car1.brand='Москвич'
car1.color='blue'
car1.engine=Engine()
car1.engine.vol=2.0
car1.engine.hp=150
print(car1.brand,car1.color,car1.year,car1.engine.hp,car1.engine.vol)


car2=Car()
car2.year=2020
car2.brand='Lexus'
car2.color='red'
car2.engine=Engine()
car2.engine.vol=200.0
print(car2.brand,car2.color,car2.year,car2.engine.hp,car2.engine.vol)