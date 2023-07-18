def selection_sort(array):
    for i in range(len(array)-1):
        print(i,"회전")
        min_index = i
        for j in range(i+1, len(array)):
            min_index = j
            print("교환전 : ",array[i],array[min_index])
            array[i],array[min_index] = array[min_index],array[i]
            print('교환 후 :', array[i], array[min_index])
            print(array)
        return array
    
array = [5,2,4,6,1,3]
selection_sort(array)
print(array)