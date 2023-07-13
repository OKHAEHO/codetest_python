coin_list = []
#print(coin_list)
a = int(input('동전의 종류를 선택하세요 : '))
b = int(input('가격을 정하세요 : '))

count=0

while True :
    
    for i in range(a) :
        coin_list.append(int(input('동전 가치를 입력하세요 : ')))
        
        
    coin_list.sort(reverse=True)
    
    for i in coin_list :
        
        count += b//i
        b %= i
    break
        
print(count,"개")