def divisorSum( n ):
    sum = 0
    for i in range(1, n + 1):
        sum += int(n / i) * i
        kk=int(n / i)
        print(int(n/i))
    return int(sum)
        
        


print(divisorSum(4))


