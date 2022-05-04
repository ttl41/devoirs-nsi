import csv

def charger_csv(filename="donnees.csv"):
    """
    Retourne une liste de listes contenant les données du fichier csv.
    """
    with open(filename, "r", encoding="utf-8") as f:
        fcontents = f.readlines()
        reader = csv.reader(fcontents)
        donnees = [i for i in reader]
    return donnees

def afficher_entier() -> None:
    """
    Affiche les données du csv en entier.
    """
    donnees = charger_csv()
    print(donnees)

def afficher_descripteurs() -> None:
    """
    Affiche tous les descripteurs du csv.
    """
    donnees = charger_csv()
    print(donnees[0])

def afficher_enregistrement(ligne=3) -> None:
    """
    Affiche un enregistrement du csv, par défaut le 3ème.
    """
    donnees = charger_csv()
    print(donnees[ligne])

def afficher_colonne(col=2) -> None:
    """
    Permet d'afficher une colonne entière d'un champ, ici la 2ème.
    """
    donnees = charger_csv()
    col -= 1 # On enlève 1, car Python compte à partir de 0
    donnees_col = [i[col] for i in donnees] # cela inclut le descripteur...
    # donnees_col = [i[col] for i in donnees[1:]] # si on ne veut pas le descripteur
    print(donnees_col)

def main():
    afficher_entier()
    afficher_descripteurs()
    afficher_enregistrement()
    afficher_colonne()

if __name__ == "__main__":
    main()
