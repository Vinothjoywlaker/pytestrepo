import itertools
for num in itertools.count():
	print(num)
	if(num == 23343):
		break

print("Testing itertools zip_longest:")
value = [1,2,3,4,5,6,7,8,9,10]
result = dict(itertools.zip_longest(value,range(100)))
print(result)


print("\n\n Testing cycle from itertools")
cyc = itertools.cycle([1,2,3,4,5])
for i in range (1,20):
	for spot in cyc:
		result = float(i/spot)
		print(f"for the value {i} and spot {spot} is : {result}")




print("\n\n repeat in itertools")
repeat_mode = itertools.repeat(2, times = 3)
while repeat_mode:
	print(next(repeat_mode))
itertools.starmap(func(),[(1,2),(2,3)])
poker = ["a","b","c","d"]
#combination is to show combination without the place data like [a,b] but not [b,a]
itertools.combinations(poker ,2)
#in permutation it allows all tje combination
itertools.permutations(poker,2)
#product will hold all the same vaule in all place like [a,a]
itertools.product(poker,repeat = 3)
print("itertoolls. ")

#chain
itertools.chain(list1,list2,list3)
itertools.filterfalse()
itertools.dropwhile(predicate, iterable)
itertools.dropwhile(predicate, iterable)
itertools.