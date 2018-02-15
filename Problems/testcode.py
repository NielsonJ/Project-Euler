from libs.primelib import Prime
import time



prime = Prime()
start = time.clock()
print(prime.getByIndex(10000))
end = time.clock()
print(end - start)