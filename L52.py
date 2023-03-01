def perfect_number(n):
    divisor_sum=0
    for x in range(1,n):
        if n%x==0:
            divisor_sum +=x
        if divisor_sum==n:
            return True
        else:
            return False

print(perfect_number(1000))
print(perfect_number(10000))
