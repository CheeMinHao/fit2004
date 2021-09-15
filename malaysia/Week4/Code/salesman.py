def salesman(houses, profits):
    # memo = [0 for _ in range(houses + 1)]
    memo = [0 for _ in range(houses + 1)]
    last_houses = [None for _ in range(houses + 1)]

    for i in range(1, len(profits) + 1, 2):
        for j in range(1, houses + 1):
            exclude = memo[i-1][j]
            include = 0
            if profits[i-1] > j:
                include = profits[i-1] + memo[i-1][j-profits[i-1]]
                print(include)
            memo[i][j] = max(exclude, include)

    return memo