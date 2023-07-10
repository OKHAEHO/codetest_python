#Day1 - 조건문, 반복문
while True:
    a = input("0이 될 때까지  무한 반복 : ")
    a = int(a)
    if(a == 0):
        break
    else :
        print(a)
        
a = int(input("정수를 카운트 다운 출력 1 : "))
while a!= 0:
    print(a)
    a= a-1