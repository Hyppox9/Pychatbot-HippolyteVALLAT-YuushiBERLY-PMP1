import Fonctions

Fonctions.extract_names("speeches")
for e in Fonctions.diconames.values():
    print(e)

import os


def extract_names(repertoire):
    L = []
    for fichier in os.listdir(repertoire):
        if "1" in fichier and fichier.removeprefix("Nomination_").removesuffix("1.txt") not in L:
            L.append(fichier.removeprefix("Nomination_").removesuffix("1.txt"))
        elif "2" in fichier and fichier.removeprefix("Nomination_").removesuffix("2.txt") not in L:
            L.append(fichier.removeprefix("Nomination_").removesuffix("2.txt"))
        elif "1" not in fichier and "2" not in fichier and fichier.removeprefix("Nomination_").removesuffix(
                ".txt") not in L:
            L.append(fichier.removeprefix("Nomination_").removesuffix(".txt"))
    L1 : list.str = []
    for i in range(len(L)):
        if L[i] not in L1:
            L1.append(L[i])
    return L1
diconames = {"Macron" : "Emmanuel Macron",
             "Chirac" : "Jacques Chirac",
             "Giscard dEstaing" : "Valerie Giscard dEstaing",
             "Hollande" : "Francois Hollande",
             "Mitterrand" : "Francois Mitterrand",
             "Sarkozy" : "Nicolas Sarkozy"}

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