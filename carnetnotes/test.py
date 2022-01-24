from carnetnotes import *
running = True

print("pro carnet de notes 2.0.69 dank memes edition ")

while running:

  try:
    print("Etat actuel du carnet de notes : ", grades, "avec les coefficients", weights)
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

  print("Que souhaitez-vous faire ?w?")
  menu = """
1/ Ajouter une note avec coeff
2/ Modifier une note
3/ Modifier un coeff
4/ Enlever une note
5/ Obtenir la moyenne
6/ Donner les mentions
7/ TOUT DETRUIRE !
Q/ rien, je vais m'en aller !
  """
  print(menu)
  choice = input("")
  if choice == "1":
    note = float(input("Note : "))
    weight = float(input("Coefficient : "))
    add_grade(grades, weights, note, weight)

  if choice == "4":
    rang = int(input("Rang de la note : ")) - 1
    remove_grade(grades, weight, rang)
  
