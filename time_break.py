import webbrowser
import time
break_taken = 0
number_of_breaks = 3

print('This program started at ' +time.ctime())
while break_taken<number_of_breaks:

	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=JxDdCNvtofA&spfreload=10")
	break_taken += 1