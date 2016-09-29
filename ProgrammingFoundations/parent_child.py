class Parent():
	""" This class acts as the Parent. The child class inherits from it. """
	def __init__(self, last_name, eye_color):
		print ("Parent constructor called.")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print (self.last_name + ' - ' + self.eye_color)

class Child(Parent):  ## Note putting the class it inherits from in the ()
	""" This class inherits from the Parent class. """
	def __init__(self, last_name, eye_color, number_of_toys):
		print ("Child constructor called.")
		Parent.__init__(self, last_name, eye_color)  ##Calling Parent constructor
		self.number_of_toys = number_of_toys

	# To override the show_info() from Parent. Not needed if they are the same.
	def show_info(self):
		print (self.last_name + ' - ' + self.eye_color + ' - ' + str(self.number_of_toys))


greg = Parent('Kirschner', 'brown')
ellie = Child('Kirschner', 'brown', 5)


greg.show_info()
ellie.show_info()  # Inherits method from Parent class, but can override if you want by defining

