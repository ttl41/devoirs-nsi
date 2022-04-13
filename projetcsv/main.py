import csv
from pprint import pprint

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

def sort_by_last_digit(liste):
  liste.sort(key=lambda x: x['release_year'][3])
  return liste

def jointure_films_acteurs(films, distribution):
  films_acteurs = []
  for act in distribution:
    for film in films:
      if act["movie_id"] == film["movie_id"]:
        films_acteurs.append({"movie_id": film["movie_id"], "title": film["title"], "cast": act["cast"]})
  return films_acteurs

def get_cast(films_acteurs, movie_id):
  cast = [x["cast"] for x in films_acteurs if x["movie_id"] == movie_id]
  return cast

def get_movies(films_acteurs, cast):
  movies = [x["title"] for x in films_acteurs if x["cast"] == cast]
  return movies

def jointure_films_realisateurs(films, realisateurs):
  films_realisateurs = []
  for film in films:
    found = False
    for real in realisateurs:
      if real["movie_id"] == film["movie_id"]:
        films_realisateurs.append({"movie_id": film["movie_id"], "title": film["title"], "director": real["director"]})
        found = True
    if not found:
      films_realisateurs.append({"movie_id": film["movie_id"], "title": film["title"], "director": ""})
  return films_realisateurs
  
def jointure_films_acteurs_complete(films, acteurs):
  films_acteurs = []
  found_cast = []
  for film in films:
    film["cast"] = ""
    for act in acteurs:
      if act["movie_id"] == film["movie_id"]:
        film["cast"] += act["cast"] + ","
        found_cast.append(act["cast"])
    films_acteurs.append(film)
  for act in acteurs:
    if act["cast"] not in found_cast: 
      films_acteurs.append({"movie_id": act["movie_id"], "cast": act["cast"]})
  return films_acteurs

def films_sans_acteurs(films_acteurs):
  films_sans_acteurs = []
  for film in films_acteurs:
    if film["cast"] == "":
      films_sans_acteurs.append(film)
  return films_sans_acteurs

def acteurs_sans_film(films_acteurs):
  acteurs_sans_film = []
  for film in films_acteurs:
    try:
      assert film["title"] == film["title"]
    except KeyError:
      acteurs_sans_film.append({"cast": film["cast"], "movie_id": film["movie_id"]})
  return acteurs_sans_film

  
def main():
  films, reals, distrib = map(load_file, ["films.csv", "realisateurs.csv", "distribution.csv"])
  print(f"Nombre d'enregistrements dans les fichiers films, réalisateurs, et distribution : {len(films)}, {len(reals)}, {len(distrib)}")
  print("Année moyenne de sortie d'un film:", release_average(films))
  print("Durée moyenne d'un film:", runtime_average(films), "minutes")
  print("Nombre de films courts, moyen, longs, très longs:")
  display_list(count_runtimes(films))
  display_list(runtime_average_by_year(films))
  display_list(sort_movies(films), 1, True)
  display_list(two_best_movies(films), 7)
  display_list(sort_by_last_digit(films), 1)
  #display_list(jointure_films_acteurs(films, distrib), 20)
  #display_list(jointure_films_realisateurs(films, reals), 20)
  #display_list(jointure_films_acteurs_complete(films, distrib), 20)
  films_acteurs = jointure_films_acteurs_complete(films, distrib)
  display_list(acteurs_sans_film(films_acteurs), 10)
  display_list(films_sans_acteurs(films_acteurs), 10)

if __name__ == "__main__":
  main()