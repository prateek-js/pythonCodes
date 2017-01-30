#write a program that returns a list that contains only 
#the elements that are common between the lists (without duplicates)

import random

numList1 = random.sample(range(1,30), 12)
numList2 = random.sample(range(1,30), 15)

result = [i for i in numList1 if i in numList2]

print(numList1)
print(numList2)
print(result)