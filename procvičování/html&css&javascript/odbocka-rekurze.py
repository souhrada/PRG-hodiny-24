def facto(n):
    res = 1
    for i in range(n):
        res *= i

    print(res)
    return res

facto(5)

















def facto_recursion(n):

    if n <= 1:
        return 1

    return n * facto_recursion(n-1)

print(facto_recursion(5))
