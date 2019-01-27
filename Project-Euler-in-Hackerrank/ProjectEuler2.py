#For this problem I just noticed that the even numbers follow:
# a(n) = 4*a(n-1)+a(n-2)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a1 = 2
    a2 = 8
    total = 2 + 8
    temp = 0
    while temp < n:
        total += temp
        temp = a2*4 + a1              
        a1 = a2
        a2 = temp
        
    print(total)
