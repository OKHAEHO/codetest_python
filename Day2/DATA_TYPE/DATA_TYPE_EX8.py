t = ()
a = []

while True :
    list = input("리스트에 쓸 내용 : ")
    if list == '' : 
        break
    a.append(list)
    
t = tuple(a)

print(type(a))

for list in t :
    print(list, end=' ')
print(type(t))