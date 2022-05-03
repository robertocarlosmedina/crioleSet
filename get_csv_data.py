import enum
import pandas 

data = pandas.read_csv('CVEN-Dataset.csv')
cv_file_writer = open("train.cv", "w")
pt_file_writer = open("train.pt", "w")

pt_translations = []
cv_translations = []

[pt_translations.append(row["Portuguese"]) for _ , row in data.iterrows()]
[cv_translations.append(row["Capverdian Creole"]) for _ , row in data.iterrows()]

index = 1
for pt, cv in zip(pt_translations, cv_translations):
    print(f"{index}: {cv}: {pt}")
    cv_file_writer.write(f"{cv}\n")
    pt_file_writer.write(f"{pt}\n")
    index += 1

cv_file_writer.close()
pt_file_writer.close()
# print(pt_translations[0])
# print(cv_translations[0])