colors = {"w": "blanc", "b": "noir"}
pieces = {
    "K": "Cavalier",
    "R": "Tour",
    "B": "Fou",
    "Q": "Dame",
    "K": "Roi",
    "P": "Pion"}

def creer_echiquier():
    return [["" for i in range(8)] for i in range(8)]

def imprimer_echiquier(echiquier):
    for i in echiquier:
        print(i)

def coordonnees_en_index(colonne, ligne):
    """
    colonne, ligne : sous format 'e', '4'
    retourne les index pour accéder à ces coordonnées dans l'échiquier
    """
    ligne = 8 - ligne
    colonnes = "ABCDEFGH"
    colonne = colonnes.index(colonne.upper())
    return colonne, ligne

def placer_piece(echiquier, piece, colonne, ligne, couleur):
    """
    colonne, ligne : sous format 'e', '4'
    couleur : 'w' (blanc) ou 'b' (noir)
    """
    colonne, ligne = coordonnees_en_index(colonne, ligne)
    piece = piece.upper()
    if piece in pieces.keys() and couleur in colors.keys():
        echiquier[ligne][colonne] = piece + couleur

def parser_piece(echiquier, colonne, ligne):
    colonne, ligne = coordonnees_en_index(colonne, ligne)
    piece = echiquier[ligne][colonne]
    try:
        type_piece = pieces[piece[0]]
        couleur_piece = colors[piece[1]]
        return type_piece, couleur_piece
    except KeyError:
        return None

def main():
    echiquier = creer_echiquier()
    placer_piece(echiquier, "P", "e", 4, "w") # place un pion blanc en e4
    imprimer_echiquier(echiquier)
    print(parser_piece(echiquier, "e", 4))

if __name__ == "__main__":
    main()
