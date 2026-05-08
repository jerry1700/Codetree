from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dist = [[-1] * M for _ in range(N)]
dist[0][0] = 0
deq = deque([(0, 0)])

while deq:
    x, y = deq.popleft()

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1 and board[nx][ny] == 1:
            dist[nx][ny] = dist[x][y] + 1
            deq.append((nx, ny))

print(dist[N - 1][M - 1])