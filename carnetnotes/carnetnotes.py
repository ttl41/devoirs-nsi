from typing import List

def create_grades() -> List[float]:
  return []

def create_weights() -> List[float]:
  return []

def add_grade(grades: List, weights: List, grade: float, weight=1.0):
  return grades.append(grade), weights.append(weight)

def edit_grade(grades: List, rank: int, new_grade: float):
  grades[rank] = new_grade
  return grades

def edit_weight(weights: List, rank: int, new_weight: float):
  weights[rank] = new_weight
  return weights

def remove_grade(grades: List, weights: List, rank: int):
  grades.pop(rank)
  weights.pop(rank)

def get_average(grades: List, weights: List):
  numerateur = 0
  for grade in grades:
    rank = 0
    numerateur += grade * weights[rank]
    rank += 1
  average = numerateur / sum(weights)
  return average

def count_grades(grades: List, threshold=10.0) -> int:
  grades_counted = 0
  for grade in grades:
    if grade < 10:
      grades_counted += 1
  return grades_counted

def delete_list(any_list: List):
  del any_list

def give_mentions(grades: List[float]):
  mentions = []
  for grade in grades:
    if grade >= 16.0:
      mentions.append("TB")
    elif grade >= 14.0:
      mentions.append("B")
    elif grade >= 12.0:
      mentions.append("AB")
    else:
      mentions.append("Aucune")
  return mentions

def save_list():
  pass

def save_everything(grades, weights):
  save_list(grades)
  save_list(weights)
  
    