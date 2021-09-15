def coin_change(N, coins):
    """
    N -> amount to obtain from coin combination
    coins -> available coin amounts in a list
    """

    # Initialize memoization
    memo = [10**99] * (N+1)

    last_coins = [None] * (N+1)

    # initialize base
    memo[0] = 0

    # fill memo until max reached
    for value in range (1, N+1):
        # for each value, iterate through each coin
        for j in range(len(coins)):
            if coins[j] <= value:
                # Figure out how many coins to exhaust value
                balance = value - coins[j]
                count = 1 + memo[balance]
                # If found more optimal solution, replace it
                if count < memo[value]:
                    memo[value] = count
                    last_coins[value] = coins[j]

    # Most optimal number of coins needed to exhaust value
    res = memo[N]

    # Backtrack coins used for exhausting value
    coins_used = []
    while N > 0:
        current_coin = last_coins[N]
        coins_used.append(current_coin)
        N -= current_coin


    return res, coins_used


def coin_change_top(N, coins):
    """
    N -> amount to obtain from coin combination
    coins -> available coin amounts in a list
    """
    if N == 0:
        return 0
    else:
        for item in coins:
            # if coin is lesser than value
            if item <= N:
                # Recurse
                tmp = coin_change_top(N-item, coins)
                # Check if there is more optimal minimum, if yes, replace and add respective coin
                if tmp + 1 < memo[N]:
                    memo[N] = tmp + 1
                    put_coins[N] = item

        return memo[N]

def backtrack(N, last_coins):
    """
    N -> amount to obtain from coin combination
    last_coins -> newly append coin list
    """
    # Initialise coins used to exhause value
    coins_used = []
    # Find which coins exhaust the value through backtracking
    while N:
        current_coin = last_coins[N]
        coins_used.append(current_coin)
        N -= current_coin
    return coins_used

    


if __name__ == "__main__":
    # Global Variables
    coins = [1, 5, 6, 9]
    N = 12
    memo = [10**99 for _ in range(N+1)]
    memo[0] = 0
    put_coins = [None] * (N + 1)

    # Obtain optimal number of coins used and the denominations used
    minimum = coin_change_top(N, coins)
    print((minimum, backtrack(N, put_coins)))

    print(coin_change(N, coins))
