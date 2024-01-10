import os
import math
def propre(repertoire, clean):
    """
    :param repertoire: là où nous avons les docs de base
    :param clean: le dossier dans lequel on va mettre les docs cleaned
    :return: les documents épurés, où les mots sont séparés dans des listes
    """
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

        """ pour faire une matrice, il faut une liste remplie de listes, alors nous avons fait une liste L2 qui sépare L1(le fichier)
        puis on met tout ça dans L3 et enfin L3 va dans la matrice"""
        L3 = []
        for i in range(len(L1)):
            L2 = L1[i].split()
            for j in range(len(L2)):
                L3.append(L2[j])

        matrice_cleaned.append(L3)

        f.close()
    return matrice_cleaned


matricepropre = propre("speeches", "cleaned")


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
    Cette fonction calcule le score idf de chaque mot dans tous les documents contenus dans le repertoire

    Paramètres :
    repertoire (str) : le nom du repertoire où se trouvent les fichiers
    """
    All_Tf = {}
    nombre_de_documents = len(os.listdir(repertoire))
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
        IDF_dict[mot] = round(math.log10(nombre_de_documents / IDF_dict[mot]), 2)

    return IDF_dict

"""transpose les lignes de la matrice en colonnes"""
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
