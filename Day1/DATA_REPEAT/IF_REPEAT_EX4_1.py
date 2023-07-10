a = int(input("정수(1~100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 출력하시오 : "))
plus = 0

while True :
    if (a > 100) :
        print("잘못입력했어요")
        break
    else : 
        
        for a in range (1, a+1):
            if (a%2==0):
                plus += a
            
        print(plus)
        
        break