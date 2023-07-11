#자료형
a = 1000
b = 1.3333
b_1 = 5.
b_2 = -.733
c = -3333
d = 0
print(a,b,b_1,b_2,c,d)

e = 1e9
e_1 = 175.25e1
e_2 = 39555e-3
print(e,e_1,e_2)

a = 0.333 + 0.666
print(a)

if a ==0.999 :
    print(True)
else :
    print(False)
    

#반올림을 해야지 귀여운 0.999가 된다. 반올림을 하지 않으면 
#0.9999999999999999999999999999999 이렇게 되기 때문에 False가 나오는 것 round를 통하여 반올림을 한다.
a = 0.333 + 0.666
print(round(a,4))
if round(a,4) == 0.999 :
    print(True)
else :
    print(False)