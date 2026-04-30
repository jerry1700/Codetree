from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
visited = [[False] * n for _ in range(n)]
starts = []
for x, y in points:
    visited[x - 1][y - 1] = True
    starts.append((x - 1, y - 1))
deq = deque(starts)

while deq:
    x, y = deq.popleft()

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
            visited[nx][ny] = True
            deq.append((nx, ny))

answer = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            answer += 1

print(answer)