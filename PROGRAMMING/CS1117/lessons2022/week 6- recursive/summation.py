def summationR (n):
    if n == 0:
        return 0
    else:
        sum = n + summationR (n-1)
    return sum

print(summationR(2))