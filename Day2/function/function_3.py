#함수
def arugument(*args):
    a=0
    for i in args:
        a = a+1
    return a

b = arugument(1,2)
c = arugument(1,2,3,4,5)
d = arugument()
print(b,c,d)