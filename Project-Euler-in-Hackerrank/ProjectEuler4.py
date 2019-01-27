def is_palindrome(n):
    num = str(n)
    if num == num[::-1] and len(num) == 6:
        return True
    else:
        return False

def find_palindromes():
    temp = set()
    for i in range(100,1000):
        for j in range(100000//i +1,1000): 
            num = i*j
            if is_palindrome(num):
                temp.add(num)
    return temp
    
#We generate all the possible palindromes
palindromes = find_palindromes()     
        

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n -= 1
    cont = True
    while cont:
        if n in palindromes:
            print(n)
            cont = False
        n -=1
