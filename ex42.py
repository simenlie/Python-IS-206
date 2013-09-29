class Person(object):

	def __init__(self,name, sex):
		self.name = name
		self.sex = sex
		
	def gen_info(self):
		return "%s is a %s" % (self.name, self.sex)

class Ansatt(Person):
	def __init__(self,name, salary, sex):
		super(Ansatt,self).__init__(name,sex)
		self.salary = salary
		self.pet = pets
		
	def info(self):
		inherit =  super(Ansatt,self).gen_info()
		print "%s and has a salary of %d" % (inherit, self.salary)
		print "%s has these animals: " % self.name, self.pet 
		
pets = {'Cat': 'Jonas', 'Dog': 'Thomas'}
		
		
einar = Ansatt("Einar", 1000, "Male")
einar.info()

mari = Person("Mari", "Female")
print mari.gen_info()

