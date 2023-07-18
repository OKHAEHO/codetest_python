a = int(input('몇개를 넣을 것이냐! : '))

age = []
name = []

for _ in range(a):
    x, y = input('나이와 이름을 입력하세요: ').split(' ')
    age.append(int(x))
    name.append(y)

print(age)
print(name)

print(sorted(age), sorted(name, key=lambda  x : x[0])) # 이게 중요하다


for i in range(a):
    print(age[i], name[i])