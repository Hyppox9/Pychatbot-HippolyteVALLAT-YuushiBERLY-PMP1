import Fonctions

Fonctions.extract_names("speeches")
for e in Fonctions.diconames.values():
    print(e)

import os


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    #crée une fonction qui permettra de lire directement a partir des fichiers
    return files_names



directory = "./speeches"
files_names = list_of_files(directory, "txt")
print_list(files_names)

for i in range(len(files_names)):
    files_names[i] = files_names[i].replace(".", "")
    files_names[i] = files_names[i].replace(",", "")
    files_names[i] = files_names[i].replace("'", " ")
    files_names[i] = files_names[i].replace(";", "")
    files_names[i] = files_names[i].replace("!", "")
    files_names[i] = files_names[i].replace("?", "")
    files_names[i] = files_names[i].replace("-", " ")
    files_names[i] = files_names[i].lower()
#permet de remplacer tout les points, virgule etc par des espaces
# et de tout mettre en minuscule pour chaque fichier

