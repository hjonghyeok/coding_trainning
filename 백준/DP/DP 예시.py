def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 금액이 0일 때 필요한 동전의 개수는 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            a = dp[x]
            b = dp[x - coin] + 1
            dp[x] = min(dp[x], dp[x - coin] + 1)
            
    return dp[amount] if dp[amount] != float('inf') else -1

# 예시
coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))  # 출력: 3 (5 + 5 + 1)