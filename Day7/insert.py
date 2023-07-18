array = [8,5,6,2,4]

for i in range(1, len(array)):
    print(i, "회전")
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            print('교환 전 :', array[j-1],array[j])
            array[j], array[j-1] = array[j-1], array[j]
            print('교환 후 : ',array[j-1],array[i])
        else :
            break
            
print(array)