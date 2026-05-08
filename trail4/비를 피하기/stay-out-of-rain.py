from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, H, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer =[[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            visited = [[-1] * N for _ in range(N)]
            visited[i][j] = 0
            deq = deque([(i, j)])

            escape = False
            while deq:
                x, y = deq.popleft()

                if board[x][y] == 3:
                    escape = True
                    break

                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and board[nx][ny] != 1:
                        visited[nx][ny] = visited[x][y] + 1
                        deq.append((nx, ny))

            if escape:
                answer[i][j] = visited[x][y]
            else:
                answer[i][j] = -1

for row in answer:
    print(*row)