from collections import deque

N = int(input())

dist = [-1] * 1000001
dist[N] = 0
q = deque([N])

while q:
    x = q.popleft()

    if x == 1:
        break

    dx = [x - 1, x + 1]

    if x % 2 == 0:
        dx.append(x // 2)
    if x % 3 == 0:
        dx.append(x // 3)

    for nx in dx:
        if 0 <= nx < 1000001 and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)

print(dist[1])