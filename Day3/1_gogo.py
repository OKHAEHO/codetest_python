import time
import os
import psutil

n = int(input('거슬러줄 돈은 얼마입니까? : '))
k = int(input('거슬러줄 돈은 얼마입니까? : '))

count = 0
total = 0
process = psutil.Process(os.getpid())
start_time = time.time()
while True :
    
    if 1<=n<=100000 and 2<=k<=100000 :
        
        if n%k != 0 :
            a = n%k
            count = ((n-a)//k)-a
            total += count
            break
            
            

end_time = time.time()

print("time : ",format(end_time - start_time,'.10f'))
print('MB bytes : ', process.memory_info().rss / (1024.0 * 1240.0))
print(count,"번")