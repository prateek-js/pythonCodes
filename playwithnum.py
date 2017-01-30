# numbers in list that are less than 5 and print - logic in one line only


# a = [1,1,3,5,6,7,8,9,12,13,25]
# print([x for x in a if x<5])

###################################################

# asks the user for a number and then prints out a list of all the divisors of that number

# num = int(input('Enter a number : '))

# list(range(start_num,end_number)) -- it will create a list of numbers
# listRange = list(range(1,num+1))
# divisorList = []
# for number in listRange:
# 	if num%number == 0:
# 		divisorList.append(number)

# print(divisorList)

###################################################

#write a program that returns a list that contains only the elements that are common between the lists (without duplicates)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# commonNum = []
# for i in a: 
# 	if i in b and i not in commonNum :
# 		commonNum.append(i)
# print(commonNum)

###################################################

#Ask the user for a string and print out whether this string is a palindrome or not

pstring = str(input('Enter a String : '))
rvs=pstring[::-1]
print(rvs)

if pstring == rvs:
	print(pstring, ' is palindrome')
else:
	print(pstring, ' is not palindrome')

###################################################

#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
	
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [element for element in a if element % 2 == 0]

print(b)