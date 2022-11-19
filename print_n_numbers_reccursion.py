def number(n):
    if n==0:
        return
    print(n)
    number(n-1)
    
number(5)