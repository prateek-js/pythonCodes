num = int(input('Enter a number : '))
check = int(input('Enter a number to be divided by : '))

if num%4 == 0:
	print(num, ' is multiple of 4 ')
elif num%2 == 0:
	print(num, ' is even number ')
else:
	print(num, ' is odd number ')

if num%check == 0:
	print(num, ' is evenly divided by : ',check)
else:
	print(num, ' is not evenly divided by : ',check)