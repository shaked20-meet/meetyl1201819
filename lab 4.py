'''
class Animal(object):
	def __init__(self, sound, name, age, favorite_color, amount):
		self.sound = sound
		self.amount = amount
		self.name = name
		self.age = age
		self.favorite_color = favorite_color

	def eat(self,food):
		print ("Yummy!!! " + self.name + " is eating " + food)
	def description (self):
		print (self.name + " is " + self.age + " years old and loves the color " + self.favorite_color)
	def make_sound(self, sound, amount):
		print(sound*amount)


s = Animal("bark", "Shady", "10", "red", 5)
print(s.name)

food = "fish"
s.eat(food)

s.description()

s.make_sound("bark", 5)
'''
class person(object):
	def __init__(self, name, city, gender, age, food, language):
		self.name = name
		self.city = city
		self.gender = gender
		self.age = age
		self.food = food
		self.language = language
	
	def favorite_breakfast (self, food):
		print(self.name + " is eating " + self.food + " the favorite breakfast!!!")

	def favorite_language (self, language):
		print(self.name + " is talking " + self.language + " the best language!!!")

h = person("Harry", "Paris", "male", "50", "eggs", "French")
h.favorite_breakfast("eggs")
h.favorite_language("French")