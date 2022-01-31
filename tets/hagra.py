#### Importation des modules ####
from Tkinter import *

#################################
#### Fonctions de conversion ####
#################################
listehexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
listebinaire=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

def binairedecimal(string):
    x=len(string)-1
    n=0
    res=0
    while x!=-1:
        if string[x]=="1":
            res=res+2**n
        n=n+1
        x=x-1
    return res

def decimalbinaire(string):
    quotient=int(string)
    liste=[]
    res=""
    while quotient!=1:
        liste=liste+[quotient%2]
        quotient=quotient/2
    liste=liste+[1]
    while liste!=[]:
        res=res+str(liste[-1])
        liste=liste[:-1]
    return res

def binairehexa(string):
    liste=[]
    res=""
    while len(string)>4:
        liste=liste+[string[-4:]]
        string=string[:-4]
    liste=liste+[string]
    while len(liste[-1])!=4:
        liste[-1]="0"+liste[-1]
    for x in range(len(liste)):
        i=listebinaire.index(liste[x])
        liste[x]=listehexa[i]
    while liste!=[]:
        res=res+liste[-1]
        liste=liste[:-1]
    return res

def hexabinaire(string):
    res=""
    for x in range(len(string)):
        i=listehexa.index(string[x])
        res=res+listebinaire[i]
    return res

def decimalhexa(string):
    return binairehexa(decimalbinaire(string))

def hexadecimal(string):
    return binairedecimal(hexabinaire(string))