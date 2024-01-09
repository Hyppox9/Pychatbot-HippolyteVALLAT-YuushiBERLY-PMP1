import os
import math
import Fonctions
def propre(repertoire, clean):
    matrice_cleaned = []
    fichiers = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)

    for fichier in fichiers:
        L1 = []
        file_path = os.path.join(repertoire, fichier)
        file = open(file_path, "r", encoding="utf8")

        lines = file.readlines()
        for n, line in enumerate(lines):
            L1.append(str(line).replace("\n", " "))
        file.close()
        for i in range(len(L1)):
            L1[i] = L1[i].replace("'", " ")
            L1[i] = L1[i].replace(".", "")
            L1[i] = L1[i].replace(",", "")
            L1[i] = L1[i].replace(";", "")
            L1[i] = L1[i].replace("!", "")
            L1[i] = L1[i].replace("?", "")
            L1[i] = L1[i].replace("-", " ")
            L1[i] = L1[i].lower()

        output_path = os.path.join(clean, fichier)
        with open(output_path, "w", encoding="utf8") as f:
            for line in L1:
                f.write(f"{line}\n")

        L3 = []
        for i in range(len(L1)):
            L2 = L1[i].split()
            for j in range(len(L2)):
                L3.append(L2[j])

        matrice_cleaned.append(L3)

        f.close()
    return matrice_cleaned


matricepropre = propre("speeches", "cleaned")
#print(matricepropre)


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
#print(extract_names("speeches"))


diconames = {"Macron" : "Emmanuel Macron",
             "Chirac" : "Jacques Chirac",
             "Giscard dEstaing" : "Valerie Giscard dEstaing",
             "Hollande" : "Francois Hollande",
             "Mitterrand" : "Francois Mitterrand",
             "Sarkozy" : "Nicolas Sarkozy"}


def TF(fichier: str, repertoire: str) -> dict:
    """
    Cette fonction retourne l'occurance des mots

    Paramètres :
    fichier (str) : le nom du fichier à analyser
    repertoire (str) : le nom du repertoire où se trouve le fichier
    """
    TF_dict = {}
    fichier = open(repertoire + "/" + fichier, "r", encoding="utf-8")
    fichier = fichier.read()
    fichier = fichier.lower()
    fichier = fichier.replace(",", "").replace(".", "").replace(";", "").replace(":", "").replace("?", "").replace("!",
                                                                                                                   "").replace(
        "(", "").replace(")", "").replace("\n", " ").replace("\t", " ").replace("\r", " ").replace('"', "").replace("'",
                                                                                                                    "").replace(
        "«", "").replace("»", "").replace("’", "").replace("–", "").replace("-", "").replace("—", "").replace("…", "")

    fichier = fichier.split(" ")
    for mot in fichier:
        if mot in TF_dict:
            TF_dict[mot] += 1
        else:
            TF_dict[mot] = 1

    return TF_dict


def IDF(repertoire: str) -> dict:
    """
    Cette fonction calcule le score idf de chaque mot dans tout les document contenue dans le repertoire

    Paramètres :
    repertoire (str) : le nom du repertoire où se trouve les fichiers
    """
    All_Tf = {}
    nombre_de_document = len(os.listdir(repertoire))
    for fichier in os.listdir(repertoire):
        All_Tf[fichier] = {}
        for mot in TF(fichier, repertoire):
            All_Tf[fichier][mot] = True

    IDF_dict = {}
    for fichier in All_Tf:
        for mot in All_Tf[fichier]:
            IDF_dict[mot] = 0
            for fichier2 in All_Tf:
                if mot in All_Tf[fichier2]:
                    IDF_dict[mot] += 1

    for mot in IDF_dict:
        IDF_dict[mot] = round(math.log10(nombre_de_document / IDF_dict[mot]), 2)

    return IDF_dict


def transposer(matrice):
    return [list(i) for i in zip(*matrice)]


def TF_IDF(repertoire: str) -> dict:
    """
    Cette fonction retourne le score tf-idf de chaque mot dans le fichier

    Paramètres :
    fichier (str) : le nom du fichier à analyser
    repertoire (str) : le nom du repertoire où se trouve le fichier
    """
    TF_IDF_dict = []
    mots = []
    for i in range(len(os.listdir(repertoire))):
        TF_IDF_dict.append([])
        for mot, value in IDF(repertoire).items():
            if value != 0:
                try:
                    TF_test = TF(os.listdir(repertoire)[i], repertoire)[mot]
                except:
                    TF_test = 0
            else:
                TF_test = 0
            TF_IDF_dict[i].append(TF_test * value)
            mots.append(mot)

    transposed = transposer(TF_IDF_dict)
    return transposed


def less_important_words(repertoire: str) -> list:
    """
    Cette fonction retourne la liste des mots non importants

    Paramètres :
    repertoire (str) : le nom du repertoire où se trouve le fichier
    """
    mots_non_importants = []
    for mot, value in IDF(repertoire).items():
        if value == 0:
            mots_non_importants.append(mot)
    return sorted(mots_non_importants)


def max_idf(repertoire: str) -> list:
    """
    Cette fonction retourne la liste des mots les plus importants

    Paramètres :
    repertoire (str) : le nom du repertoire où se trouve le fichier
    """
    max_idf = []
    for mot, value in IDF(repertoire).items():
        if value == max(IDF(repertoire).values()):
            max_idf.append(mot)
    return sorted(max_idf)


#print(TF("Nomination_Chirac1.txt", "cleaned"))
#print(IDF("cleaned"))
#print(TF_IDF("cleaned"))

#print(max_idf("cleaned"))

"""
le menu sert à executer ce que l'on veut faire
"""

sugemenu = 0
print("Choisissez ce que vous voulez faire:",'\n',"1: lister le noms des présidents",'\n',"2: afficher le fichier cleaned",'\n',"3: si vous voulez afficher le TF ",'\n',"4: si vous voulez afficher le IDF ",'\n',"5: si vous voulez afficher le TF-IDF ",'\n',"6: si vous voulez afficher le Max ",'\n',"7: si vous avez fini")
while sugemenu != 7:
    sugemenu = int(input())
    if sugemenu == 1:
        print(extract_names("speeches"))
    if sugemenu == 2:
        print(matricepropre)
    if sugemenu == 3:
        print("quel fichier?")
        chipichipi = input()
        print(TF(chipichipi, "cleaned"))
    if sugemenu == 4:
        print(IDF("cleaned"))
    if sugemenu == 5:
        print(TF_IDF("cleaned"))
    if sugemenu == 6:
        print(max_idf("cleaned"))


if sugemenu == 7:
    print("bye bye ! :) ")