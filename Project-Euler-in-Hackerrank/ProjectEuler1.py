#The formula key here is: Arithmetic progression

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    "number of multiples lower than n is (n-1)/3"
    n3=(n-1)//3
    "3+6+9+...+3*n3 = 3*(1+2+3+...+n3) = 3*n3(n3+1)/2"
    sum3=3*n3*(n3+1)//2
    n5=(n-1)//5
    sum5=5*n5*(n5+1)//2
    n15=(n-1)//15
    sum15=15*n15*(n15+1)//2
    
    print(sum3+sum5-sum15)
