array = [5,7,9,0,3,1,6,2,4,8] #저장해놓은 리스트

def quick_sort(array): #퀵정렬 함수선언
    if len(array) <= 1: #만약 리스트의 값이 1보다 작으면
        return array #다시 돌아가라~
    pivot = array[0] #리스트인덱스[0]을 pivot으로 선언
    tail = array[1:] #나머지는 tail로 선언
    
    left_side = [x for x in tail if x <= pivot] #left_side에는 피벗보다 작은 애들
    right_side = [x for x in tail if x > pivot] #right_side에는 피벗보다 큰 애들
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side) #이걸 재귀함수해서 다시 부르고 불러서 정렬
print(quick_sort(array)) #하고 프린트하면 짜라란