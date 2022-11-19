
def reverse(n):
    if n%10==n:
        return str(n)
    return str(n%10)+reverse(n//10)

def reverse_num(n,res=0):
    if n%10==n:
        return res+n
    res+=n%10
    return reverse_num(n//10,res*10)
    
def rev(n):
    return n==reverse_num(n,0)
    

print(reverse(132))
print()
print(132)
#print(reverse_num(132))

print(rev(1331))