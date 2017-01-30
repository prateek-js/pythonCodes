from statistics import * 
from statistics import mean as m, stdev as s

exList = [5,3,2,4,7,8,9,1,3]

print(m(exList))

x = median(exList)
print(x)

x = mode(exList)
print(x)

print(s(exList))

x = variance(exList)
print(x)

