from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
temp = [row[:] for row in board]
start = tuple(map(int, input().split()))
start = (start[0] - 1, start[1] - 1)
end = tuple(map(int, input().split()))
end = (end[0] - 1, end[1] - 1)

walls = [(i, j) for i in range(N) for j in range(N) if board[i][j] == 1]
length = len(walls)

def bfs():
    dist = [[-1] * N for _ in range(N)]
    dist[start[0]][start[1]] = 0
    q = deque([start])
    
    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1 and board[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return dist[end[0]][end[1]]

def backtracking(start, depth):
    global result
    global board

    if depth == K:
        for se in sequence:
            board[walls[se][0]][walls[se][1]] = 0

        answer = bfs()
        if 0 < answer < result:
            result = answer

        board = [row[:] for row in temp]

        return
    
    for i in range(start, length):
        sequence.append(i)
        backtracking(i + 1, depth + 1)
        sequence.pop()

result = float("inf")
sequence = []
backtracking(0, 0)

if result == float("inf"):
    print(-1)
else:
    print(result)