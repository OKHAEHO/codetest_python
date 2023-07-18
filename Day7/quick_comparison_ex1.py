import random
import time

array = []
st1 = time.time()
for _ in range(10000):
    array.append(random.randint(1,100))
    
def quick_sort(array):
    if len(array)<=1:
        return array

    pivot = array[0]
    tail = array [1:]
    
    lf_side = [x for x in tail if x <= pivot]
    rg_side = [x for x in tail if x > pivot]
    
    return quick_sort(lf_side) + [pivot] + quick_sort(rg_side)
ed1 = time.time()

print('quick time : ',ed1 - st1)


st2 = time.time()
regular_sort = array.sort()
ed2 = time.time()

print('regular time : ', ed2 - st2)
