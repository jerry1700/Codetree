from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

def rxcy(rc):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == rc:
                return i, j

# Please write your code here.
for _ in range(k):
    visited = [[False] * n for _ in range(n)]
    visited[r - 1][c - 1] = True
    deq = deque([(r - 1, c - 1)])

    while deq:
        x, y = deq.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] < grid[r - 1][c - 1]:
                visited[nx][ny] = True
                deq.append((nx, ny))

    rc = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                if rc < grid[i][j] < grid[r - 1][c - 1]:
                    rc = grid[i][j]

    r, c = rxcy(rc)
    r, c = r + 1, c + 1

print(r, c)