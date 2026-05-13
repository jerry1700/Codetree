N = int(input())

dp = [0] * 20
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, N + 1):
    dp[i] = sum(dp[num] * dp[i - 1 - num] for num in range(i))

print(dp[N])