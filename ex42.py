class Person(object):

	def __init__(self,name, sex):
		self.name = name
		self.sex = sex
		
	def gen_info(self):
		return "%s is a %s" % (self.name, self.sex)
		
class Animal(object):

	def __init__(self, name, legs):
		self.name = name
		self.legs = legs
		
	def get_info(self):
		return "A %s with %s legs" % (self.name, self.legs)

class Ansatt(Person):
	def __init__(self,name, salary, sex):
		super(Ansatt,self).__init__(name,sex)
		self.salary = salary
		#has-many
		#self.pets = pets
		self.animals = animals
		
	def info(self):
		inherit =  super(Ansatt,self).gen_info()
		print "%s and has a salary of %d" % (inherit, self.salary)
		#print "%s has these animals: " % self.name, self.pets
		print "%s has these animals: " % self.name
		for animal in self.animals:
			print animal.get_info()
		
pets = {'Cat': 'Jonas', 'Dog': 'Thomas'}

animals = [Animal("Dog",4),Animal("Cat",4), Animal("Spider",8)]

		
einar = Ansatt("Einar", 1000, "Male")
einar.info()

mari = Person("Mari", "Female")
print mari.gen_info()

