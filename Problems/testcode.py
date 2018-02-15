from libs.primelib import Prime
import time
import math
import bisect

# prime = Prime()
# start = time.clock()
# print(prime.getByIndex(0))
# print(prime.getByIndex(5000))
# print(prime.getByIndex(10000))
# end = time.clock()
# print(end - start)
# 
# list = [1,2,3,4,7,8,9,34,45,78,98]
# print(list)
# x = 6
# print(str(x) + ' is at location: ' + str(bisect.bisect_left(list, x)))

# 10001ste prime is 104743

prime = Prime()
print(prime.getByIndex(100000))
print(prime.getCalcedList())