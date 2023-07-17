stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
print(stack) #최하단 원소부터 출력한다.
print(stack[::-1]) #최상단 원소부터 출력한다. 

#DFS사용하기 위해 stack을 배워보았다.