a = input('문자를 입력해 : ')
a_list = []

i = 0
while i < len(a):
    if a[i] == 'g':
        i += 2  # 'g'를 만나면 현재 인덱스에서 2를 더해 건너뜁니다.
    else:
        a_list.append(a[i])
        i += 1  # 'g'가 아닌 경우는 인덱스를 1만큼 증가시킵니다.

print(*a_list)
