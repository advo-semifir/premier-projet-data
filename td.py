import pandas as p
import matplotlib.pyplot as plt

file_path = "clients.csv"
data = p.read_csv(file_path)



salary_bins = range(0, int(data['salary'].max()), 10)
plt.hist(data['salary'], bins=salary_bins, edgecolor='black')
plt.title('Répartition des salaires')
plt.xlabel('Salaire')
plt.ylabel('Nombre de personnes')
plt.show()