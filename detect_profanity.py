import urllib.request

def read_text():
	quotes = open("support/profanity.txt")
	contents_file = quotes.read()
	print(contents_file)
	quotes.close()
	check_profanity(contents_file)

def check_profanity(text_to_check):
	connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	#print(output)
	connection.close()
	if "true" in output:
		print("Profanity Alret!")
	elif "false" in output:
		print("This document is clear")
	else:
		print("Error in scanning the document")

read_text()