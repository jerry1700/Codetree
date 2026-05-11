from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * N for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            visited[i][j] = 0
            q.append((i, j))

while q:
    x, y = q.popleft()

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and board[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

for i in range(N):
    for j in range(N):
        if visited[i][j] == -1 and board[i][j] == 1:
            visited[i][j] = -2

for row in visited:
    print(*row)