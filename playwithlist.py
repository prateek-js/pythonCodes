#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
#and makes a new list of only the first and last elements of the given list. 
#For practice, write this code inside a function.


# a = [5, 10, 15, 20, 25]

# plist(a)

# def plist(a):
# 	print(a[0],a[-1])

#################################################################
#Write a program (function!) that takes a list and returns a new list that contains all 
#the elements of the first list minus all the duplicates.

#one with loop

def dupwithloop(a):
	y = []
	for i in a:
		if i not in y:
			y.append(i)
	return y

#one with sets

def dupwithsets(a):
	return list(set(a))

slist = [1,2,3,4,3,2,1]

print(dupwithloop(slist))
print(dupwithsets(slist))
