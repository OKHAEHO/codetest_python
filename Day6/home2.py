from collections import deque

n = int(input("단지의 크기 N을 입력하세요: ")) #크기 입력받기
arr = [list(map(int, input("단지 지도 세부 정보를 입력하세요: "))) for _ in range(n)] #단지 세부 정보 입력받기
cnt = 0 #단지 안의 집의 수 저장
cnt_arr = [] #몇개의 단지가 있는지 담아줄 배열값

dx = [-1, 1, 0, 0] #상하좌우 표현
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: #해당 인덱스가 1이라면
            cnt += 1 #단지 집 안의 수를 1개 늘리고
            arr[i][j] = 0 #해당 인덱스 방문처리를 위해 1로 변경한다.
            q = deque([(i, j)]) #해당 인덱스 위치를 큐로 저장한다.
            house_cnt = 1 # 단지를 판별하기 위해 1로 넣어둔다.

            while q:
                x, y = q.popleft() #x,y는 저장된 인덱스를 pop시켜서 저장한다. 고로 x에는 i, y에는 j가 들어가있다.
                for z in range(4): #0~3까지 z에 넣는다.
                    nx = x + dx[z] #인덱스 번호에 상하좌우 값을 넣어서 nx,ny에다가 집어넣는다.
                    ny = y + dy[z]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1: #만약 상하좌우값이 해당 범위(설정해놓은 값의 내부)에 있고 그 값들이 1이라면
                        arr[nx][ny] = 0 #방문처리를 위해 0으로 바꾸고
                        house_cnt += 1 #
                        q.append((nx, ny))

            cnt_arr.append(house_cnt)

print('총 단지수:', cnt)
cnt_arr.sort()
for i in cnt_arr:
    print('각 집의 개수:', i)
