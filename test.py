def climbingStairs(n):
    # dynamic programming
    # seperate problem into similiar sub problems
    # keep interim results

    # Bottom up, constant space

    if n == 1:
        return 1

    # steps
    first, second = 1, 2

    for i in range(n - 2):

        # Fibonacci
        sum = first + second
        first = second
        second = sum
    print(x + 1, "-", second, "\n")
    
    return second

for x in range(10):
    climbingStairs(x + 1)
