print("prime number : 0")
print("prime number : 1")
print("prime number : 2")
print("prime number : 3")

for numerator in range (5,10000000,2):
	prime = True
	for  div in range (3, round(numerator/2),2):
		if numerator % div == 0:
			prime = False
			break
	print(f"prime number : {numerator}")

