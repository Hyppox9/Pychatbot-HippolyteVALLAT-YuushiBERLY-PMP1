import os


def propre(repertoire):
    fichiers = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
###crée une fonction qui permettra de lire directement a partir des fichier
    for j in range(len(fichiers)):

        txt1 = []

        file = open("{}\\{}".format(repertoire, fichiers[j]), "r", encoding="utf8")
        lines = file.readlines()
        for n, line in enumerate(lines):
            txt1.append(str(line).replace("\n", " "))
        file.close()
        for i in range(len(L1)):
            txt1[i] = txt1[i].replace(".", " ")
            txt1[i] = txt1[i].replace(",", "")
            txt1[i] = txt1[i].replace("'", "")
            txt1[i] = txt1[i].replace(";", "")
            txt1[i] = txt1[i].replace("!", "")
            txt1[i] = txt1[i].replace("?", "")
            txt1[i] = txt1[i].replace("-", " ")
            txt1[i] = txt1[i].lower()
###permet de remplacer tout les points, virgule etc par des espaces et de tout mettre en minuscule
        f = open("{}\\{}".format(repertoire, fichiers[j]), "w")
        for n, line in enumerate(lines):
            f.write("{}\n".format(txt1[n]))

        f.close()
###permet aussi d'écrire dans les fichiers

propre("speeches")
