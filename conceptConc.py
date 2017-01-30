from statistics import *

admins = {'Py':'Pass123', 'user2':'Pass2'}

studentDict = {'A':[89,88,87],
			'D':[65,44,23],
			'C':[78,76,74]}

def enterGrades():
	nameToEnter = input('Student Name: ')
	gradeToEnter = input('Grade: ')

	if nameToEnter in studentDict:
		print('Adding Grade...')
		studentDict[nameToEnter].append(float(gradeToEnter))
	else: 
		print('Student not exist')

	print(studentDict)

def removeStudent():
	nametoRemove = input('enter student name to remove: ')
	if nametoRemove in studentDict:
		del studentDict[nametoRemove]
	print(studentDict)

def studentAvg():
	for eachStudent in studentDict:
		gradeList = studentDict[eachStudent]
		avgGrade = mean(gradeList)

		print(eachStudent, 'has average grade of : ', avgGrade)

def main():
	print("""
		Grade central

		[1] - Enter grades
		[2] - Remove student
		[3] - student average grades
		[4] - Exit
	""")
	action = input('Choose your option? (enter a number)')
	if action == '1':
		enterGrades()
	elif action == '2':
		removeStudent()
	elif action == '3':
		studentAvg()
	elif action == '4':
		exit()
	else: 
		print('no valid choices')

login = input('username: ')
password = input('password: ')

if login in admins:
	if admins[login] == password:
		print('Welcome,', login)
		while True:
			main()
	else:
		print('CID calling')
else:
	print('FBI calling')
