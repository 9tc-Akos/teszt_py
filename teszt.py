def osszegzes(l):
    sum=0
    for szam in l:
        sum+=szam
    return sum
        
def filet_beolvas():
    with open("adatok.txt", "r", encoding="UTF-8") as fm:
        lista=[]
        for sor in fm:
            lista.append(int(sor.strip()))
    return lista
    
szamok=filet_beolvas()
osszeg = osszegzes(szamok)
print(osszeg)        

