#This script is for testing python class
class Base:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.num = 20

	def print_info(self):
		print("This is from Base class".title())

		print(f"student is {self.name} and his age is {self.age}")

class Child(Base):
	def __init__(self,name,age,gender):
		super().__init__(name,age)
		self.gender = gender

	def print_info(self):
		super().print_info()
		print("This is from Child class".title())
		self.num = 100
		print(self.num)
		print(f"child student is {self.name} and his age is {self.age}. But she is {self.gender}")


student1 = Base("Vinoth",29)
student2 = Child("Anjana",23, "Female")
student1.print_info()
student2.print_info()

