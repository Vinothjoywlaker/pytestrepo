def fibbonacci(value):
    prev = 0
    current = 1

    while current < value :
        prev,current = current, current+prev
        yield current

print(0)
print(1)
for i in fibbonacci(10000000):
    print(i)
