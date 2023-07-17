from collections import deque

n = int(input("단지의 크기 N을 입력하세요: "))
arr = [list(map(int, input("단지 지도 세부 정보를 입력하세요: "))) for _ in range(n)]
cnt = 0
cnt_arr = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt += 1
            arr[i][j] = 0
            q = deque([(i, j)])
            house_cnt = 1

            while q:
                x, y = q.popleft()
                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                        arr[nx][ny] = 0
                        house_cnt += 1
                        q.append((nx, ny))
            
            cnt_arr.append(house_cnt)

print('총 단지수:', cnt)
cnt_arr.sort()
for i in cnt_arr:
    print('각 집의 개수:', i)
