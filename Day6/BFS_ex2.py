from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start]=True
    
    while queue :
        v = queue.popleft()
        print('BFS 탐색 노드 : ',v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                print('새로운 노드 발견 : ',[i],queue)
                visited[i]=True
graph = [
    [],
    [2,3],
    [1,8],
    [1,4,5],
    [3,5],
    [3,4],
    [7,8],
    [6,8],
    [2,6,8]
    
]

visited = [False] * 9

bfs(graph,1,visited)