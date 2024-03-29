def fib(n):
    if n <=2 : 
        return 1
    return fib(n-1) + fib(n-2)

def fibonacci_dynamic(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

def fib_dp(n,memo={}):
    if n in memo:
        return memo[n]
    if n <=2:
        return 1
    memo [n] = fib_dp(n-1,memo)+fib_dp(n-2,memo)
    return memo[n]

print(fib(3))
print(fib_dp(50))


