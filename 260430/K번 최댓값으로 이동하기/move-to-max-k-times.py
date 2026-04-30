from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r - 1, c - 1

def rxcy(rc):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == rc:
                return i, j

# Please write your code here.
for _ in range(k):
    visited = [[False] * n for _ in range(n)]
    visited[r][c] = True
    deq = deque([(r, c)])

    while deq:
        x, y = deq.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] < grid[r][c]:
                visited[nx][ny] = True
                deq.append((nx, ny))

    rc = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                if rc < grid[i][j] < grid[r][c]:
                    rc = grid[i][j]
                    
    if rc == 0:
        break
    else:
        r, c = rxcy(rc)

print(r + 1, c + 1)