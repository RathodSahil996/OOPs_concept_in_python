
from abc import ABC, abstractmethod


class Animal(ABC):

	@abstractmethod
	def make_sound(self):
         pass

class Dog(Animal):
	def make_sound(self):
		return "Woof!"


class Cat(Animal):
	def make_sound(self):
		return "Meow!"


class Cow(Animal):
	def make_sound(self):
		return "Moo!"

animal_types = [Dog, Cat, Cow]


for AnimalClass in animal_types: 
    my_animal = AnimalClass() 
    animal_name = AnimalClass.__name__ 
    
    print(f"The {animal_name} says: {my_animal.make_sound()}")

