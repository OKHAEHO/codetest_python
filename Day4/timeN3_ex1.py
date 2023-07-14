#모든 시각에서 3이 포함되는 모든 경우의 수
import time
import os
import psutil

time3 = int(input("시간의 숫자를 입력하세요 : "))

hour = 0
minute = 60
second = 60
count = 0
process = psutil.Process(os.getpid())
str_time = time.time()
while True :
    if not 0 <= time3 <=23 :
        print("잘못입력하셨습니다!")
        break
        
    else :
        for i in range(time3 + 1):
            for j in range(minute):
                for k in range(second):
                    if '3' in str(i) + str(j) + str(k) :
                        count += 1
    break
end_time = time.time()

print("time : ",format(end_time - str_time,'.10f'))
print('MB bytes : ', process.memory_info().rss*10e-6)
print(count)
    