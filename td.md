# TD : Manipuler des données avec pandas

## Objectifs

Découvrir la librairie pandas et ses fonctionnalités

## Prérequis

Avoir suivi le cours sur les bases de Python

## Introduction

Pandas est une librairie Python qui permet de manipuler des données de manière simple et efficace. Elle est particulièrement adaptée pour le traitement de données tabulaires, comme des fichiers CSV ou des bases de données.

## Documentation utile

- [Documentation officielle](https://pandas.pydata.org/docs/)
- [Tutoriel](https://sparkbyexamples.com/pandas/pandas-dataframe-tutorial-beginners-guide/)
  
## Installation

Pour installer pandas, il suffit d'utiliser la commande pip :

```bash
pip install pandas
```

## Exercices TD

Exemple d'utilisation de pandas et basés sur un fichier CSV avec les colonnes suivantes : id, firstname, lastname, email, profession, country, city, birthday, salary.

__Exercice 1__ : Charger le fichier CSV

```Python
import pandas as p

file_path = "your_file.csv"
data = p.read_csv(file_path)
print(data.head())
```

__Exercice 2__ : Afficher les informations générales du DataFrame

```Python
data.info()
```

__Exercice 3__ : Afficher le nombre de personnes par profession

```Python
professions = data['profession'].value_counts()
print(professions)
```

__Exercice 4__ : Afficher le nombre de personnes par pays

```Python
countries = data['country'].value_counts()
print(countries)
```

__Exercice 5__ : Afficher les 10 premières personnes dont le nom de famille commence par la lettre 'D'

```Python
people_d = data[data['lastname'].str.startswith('D')].head(10)
print(people_d)
```

__Exercice 6__ : Créer un nouveau DataFrame contenant uniquement les colonnes firstname, lastname et email

```Python
contact_info = data[['firstname', 'lastname', 'email']]
print(contact_info.head())
```

__Exercice 7__ : Trier le DataFrame par ordre alphabétique croissant des noms de famille

```Python
sorted_data = data.sort_values(by=['lastname'])
print(sorted_data.head())
```

__Exercice 8__ : Sauvegarder les données triées dans un nouveau fichier CSV

```Python
sorted_data.to_csv('sorted_data.csv', index=False)
```

__Exercice 9__ : Trouver la ville la plus fréquente dans le fichier

```Python
most_common_city = data['city'].mode().iloc[0]
print("La ville la plus fréquente est :", most_common_city)
```

__Exercice 10__ : Filtrer les personnes travaillant dans une profession spécifique, par exemple "Data Scientist"

```Python
data_scientists = data[data['profession'] == "Data Scientist"]
print(data_scientists)
```

__Exercice 11__ : Calculer l'age moyen par profession

```Python
data['birthdate'] = p.to_datetime(data['birthdate'], format="%m-%d-%Y")

def calcule_age(birthdate):
    today = datetime.datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

data['age'] = data['birthdate'].apply(calcule_age)
print(data['age'])
age_par_profession = data.groupby('profession')['age'].mean()
print(age_par_profession)
```

__Exercice 12__ : Calculer le salaire moyen par profession

```Python
average_salary_by_profession = data.groupby('profession')['salary'].mean()
print(average_salary_by_profession)
```

__Exercice 13__ : Afficher les personnes ayant un salaire supérieur à un montant donné, par exemple 5000

```Python
high_salary = data[data['salary'] > 5000]
print(high_salary)
```

__Exercice 14__ : Afficher le pourcentage de personnes par pays

```Python
percentage_by_country = data['country'].value_counts(normalize=True) * 100
print(percentage_by_country)
```

__Exercice 15__ : Trouver le salaire le plus élevé et le plus bas par pays

```Python
max_salary_by_country = data.groupby('country')['salary'].max()
min_salary_by_country = data.groupby('country')['salary'].min()
print("Salaire maximum par pays :\n", max_salary_by_country)
print("Salaire minimum par pays :\n", min_salary_by_country)
```

__Exercice 16__ : Créer un nouveau DataFrame en ne gardant que les personnes ayant un certain âge, par exemple 30 ans

```Python
data['birthdate'] = p.to_datetime(data['birthdate'], format="%m-%d-%Y")

def calculate_age(birthdate):
    today = datetime.datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

data['age'] = data['birthdate'].apply(calculate_age)
age_filtre = data[data['age'] == 30]
print(age_filtre)
```

__Exercice 17__ : Afficher le nombre de personnes par tranche d'âge (par exemple, tous les 10 ans) en utilisant la fonction utilisée dans l'exercice 16

```Python
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-99']
data['age_group'] = p.cut(data['age'], bins=age_bins, labels=age_labels, include_lowest=True)
people_by_age_group = data['age_group'].value_counts()
print(people_by_age_group)
```

__Exercice 18__ : Afficher la répartition des salaires en utilisant des histogrammes

```Python
import matplotlib.pyplot as plt

salary_bins = range(0, int(data['salary'].max()), 10)
plt.hist(data['salary'], bins=salary_bins, edgecolor='black')
plt.title('Répartition des salaires')
plt.xlabel('Salaire')
plt.ylabel('Nombre de personnes')
plt.show()
```

__Exercice 19__ : Trouver les personnes avec le même nom de famille

```Python
nom_doublon = data[data['lastname'].duplicated(keep=False)].sort_values(by='lastname')
print(nom_doublon)
```

__Exercice 20__ : Afficher la répartition des professions par pays

```Python
profession_par_pays = data.groupby(['country', 'profession']).size().unstack()
print(profession_par_pays)
```
