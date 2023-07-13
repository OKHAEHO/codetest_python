import time
import os
import psutil

s = input("숫자를 입력하세요~ : ")

#print(s)

count1 = 1
count2 = 0
st_t = time.time()
for i in range (len(s)) :
    if int(s[i]) > 1 :
        count1 *= int(s[i])
        
    elif int(s[i]) <= 1 :
        count2 += int(s[i])    
end_t=time.time()

print(format(end_t - st_t,'.10f'))
print(count1+count2)