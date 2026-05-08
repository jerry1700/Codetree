from collections import deque

dxy = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

dist = [[-1] * N for _ in range(N)]
dist[r1][c1] = 0
deq = deque([(r1, c1)])

while deq:
    x, y = deq.popleft()

    if x == r2 and y == c2:
        break

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            deq.append((nx, ny))

print(dist[r2][c2])