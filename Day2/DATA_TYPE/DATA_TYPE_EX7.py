a = []

while True :
    list = input("리스트에 쓸 내용 : ")
    if list == '' : 
        break
    a.append(list)

print("입력한 이름의 전체목록")
for list in a :
    print(list, end=' ')

