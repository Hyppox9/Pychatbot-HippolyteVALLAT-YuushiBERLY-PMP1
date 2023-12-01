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
    for e in L:
        print(e)

extract_names("./speeches")
