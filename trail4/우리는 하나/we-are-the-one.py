from collections import deque
from itertools import combinations

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, K, U, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

place = [(i, j) for i in range(N) for j in range(N)]
comb_place = list(combinations(place, K))

answer = 0

for comb_deq in comb_place:
    visited = [[False] * N for _ in range(N)]

    for deq in comb_deq:
        visited[deq[0]][deq[1]] = True
        d = deque([deq])

        while d:
            x, y = d.popleft()
            high = board[x][y]

            for dx, dy in dxy:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and U <= abs(board[nx][ny] - high) <= D:
                    visited[nx][ny] = True
                    d.append((nx, ny))

    result = sum([1 for i in range(N) for j in range(N) if visited[i][j]])
    answer = max(answer, result)

print(answer)