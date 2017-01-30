try:
	print('Running inside try block')
	import jupiter
	print('5'+x)

except TypeError as t:
	print('Inside typeError')
	print(str(t))

except NameError as n:
	print('Inside NameError')
	print(str(n))

except Exception as e:
	print('Inside General exception')
	print(str(e))



print('code is able to continue')