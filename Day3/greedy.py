a = int(input('거슬러줄 돈은 얼마입니까? : '))

one = a//500
two = (a%500)//100
three = ((a%500)%100)//50
four = (((a%500)%100)%50)//10

count = (one+two+three+four)
print(count,"개")

count=0
array = [500,100,50,10]
for coin in array:
    count += a // coin
    a %= coin

print("최소갯수는 : ",count)