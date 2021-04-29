
import pytest
class calc():
	def __init__(self):
		"""This class is used for testing python calculator as test project"""
		print("Class initilised")
	
	def add(self,*datas):
		"""
		This function is used to add the given numbers. It takes any number of inputs and provide single output.
		:param argument: arguments in the form of list, we can provide any number of list
		: return :float or decimal
		"""
		result = sum(datas)
		return result

	def subtract(self,*datas):
		"""
		This function is used to subract the given values. It takes any number of inputs . Input is in the 
		form of decimal or float. And output is in the form of decimal or float
		:param argument: argument is in the form og list or arguments decimal or float
		: return : float or decimal
		"""
		datas = list(datas)
		result = datas.pop(0)
		for data in datas:
			result -= data
		return result

	def multiply(self,*datas):
		"""
		This function is used for multiply the given set of numbers
		:input param: decimal or float : we can pass any number of arguments 
		:output :decimal or float
		"""
		result = 1
		for data in datas:
			result *=data
		return result

	def divide(self,*datas):
		"""
		This function is to calculate division of the given numbers
		:param datas: decimal or float we can pass any number of arguments
		:return :  decimal or float
		"""
		datas = list(datas)
		result = datas.pop(0)
		for data in datas :
			result /= data

		return result

	def exponential(self,*datas):
		""" 
		This function is used to calculate the exponential of the given numbers
		:param: decimal or float : we can pass any number of arguments
		:return : decimal or float
		"""
		datas = list(datas)
		result = datas.pop(0)
		for data in datas:
			result **= data

		return result




if __name__ == '__main__':
	calc = calc()
	result = calc.add(1,2,2,2)
	print(result)
	result = calc.subtract(40,4,8)
	print(result)
	result = calc.multiply(2,5)
	print(result)
	result = calc.divide(88,5)
	print(result)
	result = calc.exponential(2,4)
	print(result)