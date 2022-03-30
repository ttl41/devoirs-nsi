import csv
from pprint import pprint
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
      pprint(liste[-n:])
    else:
      pprint(liste[:n])
  else:
    pprint(liste)

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
  average = round(sum(release_years)/len(release_years))
  return average

def runtime_average(liste):
  runtimes = [int(x['runtime']) for x in liste if x != 0]
  average = round(sum(runtimes)/len(runtimes))
  return average

def runtime_average_by_year(liste):
  runtimes_year = {}
  for i in liste:
    if i['runtime'] != '0':
      try:
        runtimes_year[i['release_year']].append(int(i['runtime']))
      except KeyError:
        runtimes_year[i['release_year']] = [int(i['runtime'])]
  runtime_averages = {x[0]: round(sum(x[1])/len(x[1])) for x in runtimes_year.items()}
  runtime_averages = list(runtime_averages.items())
  runtime_averages.sort()
  return runtime_averages
      
def count_runtimes(liste):
  runtimes = [int(x['runtime']) for x in liste if x != 0]
  short, medium, long, verylong = 0, 0, 0, 0
  for i in runtimes:
    if i <= 85:
      short += 1
    elif i  <= 120:
      medium += 1
    elif i <= 145:
      long += 1
    else:
      verylong += 1
  return [short, medium, long, verylong]

def sort_movies(liste):
  valid_list = [x for x in liste if x['revenue'] != '0']
  sorted_movies = sorted(valid_list, key=lambda x: (x['release_year'], int(x['revenue'])))
  return sorted_movies

def two_best_movies(liste):
  valid_list = [x for x in liste if x['revenue'] != '0']
  profitable_movies = {}
  for i in valid_list:
    try:
      if int(i['revenue']) > int(profitable_movies[i['release_year']][0]['revenue']):
        profitable_movies[i['release_year']][0], profitable_movies[i['release_year']][1] = i, profitable_movies[i['release_year']][0],
    except (KeyError, IndexError):
      profitable_movies[i['release_year']] = [i, '']
  profitable_movies = list(profitable_movies.items())
  profitable_movies.sort()
  return profitable_movies 
    
  
  
def main():
  films, reals, distrib = map(load_file, ["films.csv", "realisateurs.csv", "distribution.csv"])
  print(f"Nombre d'enregistrements dans les fichiers films, réalisateurs, et distribution : {len(films)}, {len(reals)}, {len(distrib)}")
  print("Année moyenne de sortie d'un film:", release_average(films))
  print("Durée moyenne d'un film:", runtime_average(films), "minutes")
  print("Nombre de films courts, moyen, longs, très longs:")
  display_list(count_runtimes(films))
  display_list(runtime_average_by_year(films))
  display_list(sort_movies(films), 8, True)
  display_list(two_best_movies(films))

if __name__ == "__main__":
  main()