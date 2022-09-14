def ex1():
    n=int(input('Nr. de elemente= '))
    s=0
    for i in range(n+1):
        if i%2==0:
            s=s+0.5**i
    return(s)
print(ex1())