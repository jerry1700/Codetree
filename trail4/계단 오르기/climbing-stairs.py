N = int(input())

dp = [0] * 1001
dp[2] = 1
dp[3] = 1
for i in range(4, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 3]) % 10007

print(dp[N])