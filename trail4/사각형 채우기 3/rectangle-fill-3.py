N = int(input())

dp = [0] * 1001
dp[1] = 2
dp[2] = 7
dp[3] = dp[1] * 3 + dp[2] * 2 + 2
for i in range(4, N + 1):
    dp[i] = (dp[i - 1] * 3 + dp[i - 2] - dp[i - 3]) % 1000000007

print(dp[N])