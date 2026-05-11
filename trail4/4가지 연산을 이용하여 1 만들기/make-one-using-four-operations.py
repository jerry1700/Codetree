from collections import deque

N = int(input())

dist = [-1] * 1000001
dist[N] = 0
q = deque([(N)])

while q:
    x = q.popleft()

    if x == 1:
        break

    if x % 2 == 0 and x % 3 == 0:
        for nx in [x - 1, x + 1, x // 2, x // 3]:
            if 0 <= nx < 1000001 and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append((nx))
    elif x % 2 == 0:
        for nx in [x - 1, x + 1, x // 2]:
            if 0 <= nx < 1000001 and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append((nx))
    elif x % 3 == 0:
        for nx in [x - 1, x + 1, x // 3]:
            if 0 <= nx < 1000001 and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append((nx))
    else:
        for nx in [x - 1, x + 1]:
            if 0 <= nx < 1000001 and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append((nx))

print(dist[1])