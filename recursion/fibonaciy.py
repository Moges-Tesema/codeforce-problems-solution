def fibo(n):
    assert n >= 0 and int(n) == n, "please use positive integer"
    if n in [0,1]:
        return n # return itself
    else:
        return fibo(n-2)+ fibo(n-1) # understand the logic, don't try to memoize every line of code!
    """
    what is fibonacy? 0 1 1 2, 3,5, 8 ,13,21
    """