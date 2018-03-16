#! python3
#calculates the time spent in computation

import time

starttime=time.time()
for i in range(10000):
    print("blah")
endtime=time.time()

print(endtime-starttime)
