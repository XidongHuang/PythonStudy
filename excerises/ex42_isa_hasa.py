"""*************************************************************************
    > File Name: ex42_isa_hasa.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Fri  7 Oct 13:34:56 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Invoke supclass's constructor, and set its name
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet, the pet is satan (satan is-a Cat)
mary.pet = satan

## frank is-a Employee, and frank has-a name "Frank", has-a salary "120000"
frank = Employee("Frank", 120000)

## frank has-a pet, the pet is-a Dog(rover)
frank.pet = rover

## flipper is-a fish (instance of fish)
flipper = Fish()

## crouse is-a Salmon (instance of Salmon)
crouse = Salmon()

## harry is-a Halibut (instance of Halibut)
harry = Halibut()
