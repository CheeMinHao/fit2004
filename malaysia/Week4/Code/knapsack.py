def knapsack(N, items):
    """
    Knapsack Problem with repitition of choosing
    the weights
    """
    memo = [0] * (N + 1)
    memo[0] = 0
    for bag_weight in range(1, N + 1):
        for j in range(len(items)):
            if items[j][0] <= bag_weight:
                balance = bag_weight - items[j][0]
                profit = items[j][1] + memo[balance]
                if profit > memo[bag_weight]:
                    memo[bag_weight] = profit
        print(memo[bag_weight])
    return str(max(memo)) + "Done"

def knapsack_bound(N, items):
    """
    :complexity:
    - Time: O(NM) for filling matrix
    - Space: O(NM) for the matrix...we can reduce this however
             We realize we do not need the entire matrix! We get
             the current value by looking at the row above only.
             So we can just store the latest 2 row. Therefore
             reducing the complexity to O(2N+M)
             However, cannot do this kind of space saving, because
             we need it to reconstruct the solution (which is where
             the backtracking concept comes in)
    """
    memo = [[0 for _ in range(N+1)] for _ in range(len(items) + 1)]
    for i in range(1, len(items)+1):
        for j in range(1, N+1):
            exclude = memo[i-1][j]
            include = 0
            if items[i-1][0] <= j:
                include = items[i-1][1] + memo[i-1][j-items[i-1][0]]
            memo[i][j] = max(exclude, include)

    return memo


if __name__ == "__main__":
    print(knapsack_bound(12, [[6, 230], [1, 40], [5, 350], [9, 550]]))