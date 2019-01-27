def largest_prime_factor(n):  
    i = 2
    while i <= n**0.5: #smaller prime factor is smaller or equal than the square root (else n is prime)
        if n % i:
            i += 1
        else:
            n //= i
    return n

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    print(largest_prime_factor(n))
