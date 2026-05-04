from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def backtracking(start, depth):
    global answer
    global board

    if depth == M:
        for s in sequence:
            rx, ry = rock_place[s]
            board[rx][ry] = 0
        
        visited = [[False] * N for _ in range(N)]
        for x, y in startxy:
            visited[x][y] = 1
        deq = deque(startxy)

        while deq:
            x, y = deq.popleft()

            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 0:
                    visited[nx][ny] = True
                    deq.append((nx, ny))

        cnt = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j]:
                    cnt += 1

        if cnt > answer:
            answer = cnt

        board = [row[:] for row in temp]

        return
    
    for i in range(start, rock_cnt):
        sequence.append(i)
        backtracking(i + 1, depth + 1)
        sequence.pop()

N, K, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
temp = [row[:] for row in board]
startxy = [tuple(map(int, input().split())) for _ in range(K)]
startxy = [(x - 1, y - 1) for x, y in startxy]

rock_cnt = 0
rock_place = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            rock_cnt += 1
            rock_place.append((i, j))

sequence = []
answer = 0
backtracking(0, 0)
print(answer)