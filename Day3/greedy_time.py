import time
import os
import psutil

process = psutil.Process(os.getpid())
start_time = time.time()
n = int(input('거슬러줄 돈은 얼마입니까? : '))
count = 0

array = [500,100,50,10]
for coin in array:
    count += n // coin
    n %= coin

print("최소갯수는 : ",count)

end_time = time.time()
print("time : ",format(end_time - start_time,'.10f'))
print('MB bytes : ', process.memory_info().rss)