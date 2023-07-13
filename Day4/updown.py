

x,y=1,1

n = int(input("정사각형의 크기를 입력하세요 : "))
moves = input("방향을 입력하세요 (D A W S) : ").split(' ')
road = [[0] * n for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
move_type = ["D","A","W","S"]

for move in moves :
    for i in range(len(move_type)):
        if move == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny <1 or nx>n or ny>n:
        continue
    
xy = nx,ny
    
print("모험가의 위치 : ",x,y)