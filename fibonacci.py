# Write a program that asks the user how many Fibonacci numbers to generate and then generates them
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate

fiblimit = int(input('Enter limit for fibonacci series'))
fib = []

def genFib(a):
	i = 1
	if fiblimit == 0:
		fib = []
	elif fiblimit == 1:
		fib = [1]
	elif fiblimit == 2:
		fib = [1,1]
	elif fiblimit>2:
		fib = [1,1]
		while i<(fiblimit-1):
			fib.append(fib[i]+fib[i-1])
			i += 1
	print(fib)

genFib(fiblimit)