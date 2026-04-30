from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def target(next_num):
    for i in range(N):
        for j in range(N):
            if board[i][j] == next_num:
                return i, j

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())
r, c = r - 1, c - 1

for _ in range(K):
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    cur_num = board[r][c]
    next_num = 0
    deq = deque([(r, c)])

    while deq:
        x, y = deq.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] < cur_num:
                visited[nx][ny] = True
                if board[nx][ny] > next_num:
                    next_num = board[nx][ny]
                deq.append((nx, ny))

    if next_num:
        r, c = target(next_num)
    else:
        r, c = r, c

print(r + 1, c + 1)