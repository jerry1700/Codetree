n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = [[False] * m for _ in range(n)]
visited[0][0] = True
deq = deque([(0, 0)])

answer = False
while deq:
    x, y = deq.popleft()

    if x == n - 1 and y == m - 1:
        answer = True

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and a[nx][ny] == 1:
            visited[nx][ny] = True
            deq.append((nx, ny))

if answer:
    print(1)
else:
    print(0)