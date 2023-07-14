small_list = [chr(i) for i in range(97,123)]
small_copy = []
#print(small)
i = 0
j = 0

select = ord(input("선택할 알파벳을 적으세요.(a~z) : "))
lng = input("단어를 입력하세요")

print(select)

for clear in small_list :
    clear = ord(clear)
    if select == clear :
        small_copy.append(clear-select-1)
    else :
        small_copy.append((clear - select)-(clear - select + 1))

for j in range(len(lng)):
    a = small_list.index(lng[j])
    small_copy[a] = i
    i += 1
    
    #small_copy.append((clear - select)-(clear - select)+(j+1))
    

print (small_copy)