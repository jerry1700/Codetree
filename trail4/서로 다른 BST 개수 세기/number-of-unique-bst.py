N = int(input())

dp = [0] * 20
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, N + 1):
    dp[i] = 0
    for num in range(i):
        dp[i] += dp[num] * dp[i - num - 1]

print(dp[N])