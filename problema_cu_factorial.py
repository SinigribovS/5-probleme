def ex2(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return(fact)

n=int(input("Introducet numarul n: "))
m=int(input("Introducet numarul m: "))
if n>m:
x=n-m
print(ex2(n))
print(ex2(m))
print(ex2(x))