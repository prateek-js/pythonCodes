def example():
	return 15,19

a,b = example()

print(a)
print(b)

#python doesnt have array it has list
x = [6,2,3,4,5,3,5,6,7,8,7,4,3]
print(x)
print(x[4])
x.append(12)
print(x)

x.insert(5,7)
print(x)

x.remove(7)
print(x)

print(x.index(2))
print(x.count(3))

x.sort()
print(x)