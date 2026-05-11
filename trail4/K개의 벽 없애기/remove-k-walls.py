from collections import deque
from itertools import combinations

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
start = tuple(x - 1 for x in map(int, input().split()))
end = tuple(x - 1 for x in map(int, input().split()))

walls = [(i, j) for i in range(N) for j in range(N) if board[i][j] == 1]

def bfs():
    dist = [[-1] * N for _ in range(N)]
    dist[start[0]][start[1]] = 0
    q = deque([start])
    
    while q:
        x, y = q.popleft() 

        if (x, y) == end:
            return dist[x][y]

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1 and board[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return -1

result = float("inf")

for wall in combinations(walls, K):
    for r, c in wall:
        board[r][c] = 0

    answer = bfs()
    if 0 < answer < result:
        result = answer

    for r, c in wall:
        board[r][c] = 1

if result == float("inf"):
    result = -1

print(result)