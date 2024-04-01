def gridTraveler_memoization(m,n,memo={}):
    key = f"{m},{n}"
    if key in memo :
        return memo[key]
    if m==1 and n==1:
        return 1
    if m == 0 or n == 0 :
        return 0
    memo[key]  = gridTraveler_memoization(m-1 , n ,memo) + gridTraveler_memoization(m , n-1,memo)
    return memo[key]

print(gridTraveler_memoization(18,18))