#함수
def add(a,b):
    print("함수를 호출합니다 : ", a+b)
    return a+b

print("add 함수를 호출합니다 : ")
print("add(3,15)")
print(add(b=3,a=10))

def add2(a,b):
    a = 25
    b = 25
    print(a+b)
    
print("add2 함수를 호출합니다 : ")
add2(1,1)

a = 15
def add3():
    global a
    b = 25
    print(a+b)
    
print("add3함수를 호출합니다 : ")
add3()