def possibleSums(coins, quantity):
    maximum = sum((map(lambda t: t[0] * t[1], zip(coins, quantity))))

    dp = [False] * (maximum + 1)
    dp[0] = True
    for coin,q in zip(coins,quantity):
        for b in range(coin):
            num = -1
            for i in range(b,maximum+1,coin):
                if dp[i]:
                    num = 0
                elif num>=0:
                    num += 1
                dp[i] = 0 <= num <= q

    return sum(dp) - 1