st = input("대문자와 숫자를(0~9)로 구성된 문자열을 입력하세요 :")
print(st)
st_list =[]
count = 0

for i in range(len(st)):
    if st[i].isalpha():
        st_list.append(st[i])
        st_list.sort()
    else :
        count += int(st[i])
        
print(*st_list,count)