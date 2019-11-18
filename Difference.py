import math
def Square_Diff(n):

    l = (n * (n + 1) * (2 * n + 1)) // 6
    k = pow((n * (n + 1)) // 2,2)
    m = abs(l - k)

    return m

print(Square_Diff(int(input("enter a number: "))))
