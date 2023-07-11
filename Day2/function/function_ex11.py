list = []
average = 0

while True :
    num = int(input("평균을 계산할거예요 숫자를 입력하세요 (0을 누르면 평균계산이 시작됩니다.): "))

    if num == 0:
        break
        
    list.append(num)
    
    
def avg() :
    
    average = sum(list)/len(list)
    
    return average

print(avg())



