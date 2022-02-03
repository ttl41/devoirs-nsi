from carnetnotes import *

running = True

print("Carnet de Notes NSI")

while running:

  try:
    print("""
    
Etat actuel du carnet de notes :""", grades, "avec les coefficients", weights)
  except NameError:
    print("Vous n'avez pas encore créé de carnet de notes. En créer un maintenant ? [Y/n]")
    choice = input("")
    if choice == "n" or choice == "N":
      print("Vous ne pouvez rien faire sans carnet de note ! Au revoir...")
      exit()
    else:
      grades = create_grades()
      weights = create_weights()
      print("Carnet de notes créé !")

  print("\nQue souhaitez-vous faire ?w?")
  menu = """
1/ Ajouter une note avec coeff
2/ Modifier une note
3/ Modifier un coeff.
4/ Enlever une note
5/ Obtenir la moyenne
6/ Donner les mentions
7/ Obtenir la couleur du carnet
8/ TOUT DETRUIRE !
Q/ rien, je vais m'en aller !
  """
  print(menu)
  choice = input("")
  if choice == "1":
    note = float(input("Note : "))
    weight = float(input("Coefficient : "))
    add_grade(grades, weights, note, weight)
  
  if choice == "2":
    rang = int(input("Rang de la note : ")) - 1
    nouvelle_note = float(input("Nouvelle note : "))
    edit_grade(grades, rang, nouvelle_note)

    
  if choice == "3":
    rang = int(input("Rang du coeff. : ")) - 1
    nouveau_coeff = float(input("Nouveau coeff. : "))
    edit_weight(weights, rang, nouveau_coeff)


  if choice == "4":
    rang = int(input("Rang de la note : ")) - 1
    remove_grade(grades, weight, rang)
  
  if choice == "5":
    moyenne = get_average(grades, weights)
    print("La moyenne est ", moyenne)

  if choice == "6":
    mentions = give_mentions(grades)
    print("Les mentions associées aux notes sont :", mentions)

  if choice == "7":
    couleur = give_color(grades, weights)
    print("La couleur hexadécimale du carnet est", couleur)

  if choice == "8":
    del grades
    del weights # je ne sais pas pourquoi,
    # ça ne marche pas quand je fais sur une fonction
    print("Carnet de notes supprimé !") 
    
  if choice == "q" or choice == "Q" :
    running = False 

