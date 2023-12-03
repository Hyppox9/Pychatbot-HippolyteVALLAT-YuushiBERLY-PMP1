import os


def propre(repertoire):
    fichiers = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)

    for j in range(len(fichiers)):

        L1 = []

        file = open("{}\\{}".format(repertoire, fichiers[j]), "r", encoding="utf8")
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

        f = open("{}\\{}".format(repertoire, fichiers[j]), "w")
        for n, line in enumerate(lines):
            f.write("{}\n".format(L1[n]))

        f.close()

propre("speeches")