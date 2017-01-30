class Parent():
	def __init__(self,arg1,arg2):
		#print("Parent constructor called")
		self.last_name = arg1
		self.eye_color = arg2

	def show_info(self):
		print("Last name: " +self.last_name+ " Eye color: " +self.eye_color)

class Child(Parent):
	def __init__(self,arg1,arg2,arg3):
		#print("child constructor called")
		Parent.__init__(self,arg1,arg2)
		self.money = arg3

	def show_info(self):
		print("Last name: " +self.last_name+ " Eye color: " +self.eye_color+ " Pocket Money: " +self.money)

prateek = Parent("Desai","black")
# prateek.show_info()

sonal = Child("Partani","Blue","50000")
sonal.show_info()
# print(sonal.last_name+" "+sonal.money+" "+sonal.eye_color)