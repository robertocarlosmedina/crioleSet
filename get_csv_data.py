import enum
import pandas 

data = pandas.read_csv('CVEN-Dataset.csv')
cv_file_writer = open("train.cv", "w")
pt_file_writer = open("train.pt", "w")
en_file_writer = open("train.en", "w")

pt_translations = []
cv_translations = []
en_translations = []

[pt_translations.append(row["Portuguese"]) for _ , row in data.iterrows()]
[cv_translations.append(row["Capverdian Creole"]) for _ , row in data.iterrows()]
[en_translations.append(row["English"]) for _ , row in data.iterrows()]

index = 1
print(cv_translations)
for pt, cv, en in zip(pt_translations, cv_translations, en_translations):
    print(f"{index}: {cv}: {pt}")
    cv_file_writer.write(f"{cv}\n")
    pt_file_writer.write(f"{pt}\n")
    en_file_writer.write(f"{en}\n")
    index += 1

cv_file_writer.close()
pt_file_writer.close()
en_file_writer.close()
# print(pt_translations[0])
# print(cv_translations[0])