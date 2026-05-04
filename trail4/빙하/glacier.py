from collections import deque

dxy =  [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
last = [[0] * M for _ in range(N)]

def deqqqq():
    deq = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    qqqq = deque([(0, 0)])

    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                qqqq.append((nx, ny))
                deq.append((nx, ny))

    return qqqq

cnt = 0
answer = float("inf")
while board != last:
    visited = [[False] * M for _ in range(N)]
    deq = deqqqq()

    num = 0
    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                board[nx][ny] = 0
                num += 1

    if 0 < num < answer:
        answer = num

    cnt += 1

print(cnt, answer)