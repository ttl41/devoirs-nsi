import csv
from collections import OrderedDict

def load_file(filename):
  container = []
  with open(filename,'r', encoding ='ISO-8859-15') as csv_file:
    lecteur = csv.DictReader(csv_file, delimiter=';')
    for ligne in lecteur:
      container.append(ligne)
    return container

def display_list(liste, n=None, from_end=False):
  if n:
    if from_end:
      print(liste[-n:])
    else:
      print(liste[:n])
  else:
    print(liste)

def filter_by_date(liste, une_seule_liste=False):
  if not une_seule_liste:
    filtered = [x for x in liste if int(x['release_year']) > 2015 or int(x['release_year']) < 1995]
  else:
    filtered1 = [x for x in liste if int(x['release_year']) > 2015]
    filtered2 = [x for x in liste if int(x['release_year']) < 1995]
    filtered = filtered1 + filtered2
  return filtered

def release_average(liste):
  release_years = [int(x['release_year']) for x in liste]
  average = sum(release_years)/len(release_years)
  return average
  
def main():
  films, reals, distrib = map(load_file, ["films.csv", "realisateurs.csv", "distribution.csv"])
  print(f"Nombre d'enregistrements dans les fichiers films, réalisateurs, et distribution : {len(films)}, {len(reals)}, {len(distrib)}")
  display_list(filter_by_date(films), 6)
  print(release_average(films))

if __name__ == "__main__":
  main()