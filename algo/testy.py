from math import sqrt

def distance(x1: float, x2: float) -> float:
    """Retourne la différence (toujours positive) entre 2 nombres, 2 chiffres après virgule"""
    d=round(abs(x1-x2),2)
    return d

def distance_vectorielle(x1, x2, y1, y2) -> float:
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def Kvoisins(L: list, k: int, x: float) -> list:
    """Retourne k index de nombres de L, pour lesquels l'écart avec x et le plus faible"""
    listeDistanceIndice = []
    # On fait une liste avec les écarts des nombres à x, et les nombres en question...
    for i in range(len(L)):
        d=distance(x,L[i])
        listeDistanceIndice.append([d,i])
    listeDistanceIndice.sort() # On trie selon les écarts les plus petits
    Voisins = []
    for i in range(k):
        Voisins.append(listeDistanceIndice[i][1])
    # On met les k index pour lesquels les écarts sont les plus petits dans Voisins
    return Voisins

def predire_classe(L,Classes,k,x):
    Voisin = Kvoisins (L,k,x)
    ClassesPossibles=['C','T']
    decompte= [0,0]
    for v in Voisin: # v == index de L
        if Classes[v] == 'C':
            decompte[0] += 1
        else:
            decompte [1] += 1
    # le décompte est une liste avec des compteurs de classes (C,T)
    plusGrandDecompte = decompte [0]
    indice = 0
    if decompte [1] > plusGrandDecompte:
        indice = 1
    # on retourne "C" si il y a plus de nombres qui sont sur C... etc
    return ClassesPossibles[indice]

L=[0.5,1.0,2.0,3.7,5.1,6.0,7.0]
Classes = ['T','C','C','T','T','C','C']
x=3.0
k=3

print(Kvoisins(L,k,x))
print([L[i] for i in Kvoisins(L,k,x)]) 
print(predire_classe(L,Classes,k,x))
