def adunare_frac(n1, n2):
    n=n1[1]*n2[1]
    n1[0]=n1[0]*n/n1[1]
    n2[0]=n2[0]*n/n2[1]
    n1[1]=n2[1]=n
    suma=[n1[0]+n2[0],n]
    return(suma)

def inm_frac(n1, n2):
    num=n1[0]*n2[0]
    numit=n1[1]*n2[1]
    return(num,numit)
    
f1 = list(eval(input("Introduceti prima fractie: ")))
f2 = list(eval(input("Introduceti a doua fractie: ")))

print(adunare_frac(f1,f2))