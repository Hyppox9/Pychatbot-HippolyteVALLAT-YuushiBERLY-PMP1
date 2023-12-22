import os
def propre(repertoire,clean):
    matrice_cleaned = []
    fichiers = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)



    for j in range(len(fichiers)):

        L1 = []
        file = open("{}\\{}".format(repertoire, fichiers[j]), "r",encoding="utf8")
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

        f = open("{}\\{}".format(clean, fichiers[j]), "w", encoding="utf8")
        for n, line in enumerate(lines):
            f.write("{}\n".format(L1[n]))


        L3 = []
        for i in range(len(L1)):
            L2 = L1[i].split()
            for j in range(len(L2)):
                L3.append(L2[j])
        print(L3)
        matrice_cleaned.append(L3)


        f.close()
    return matrice_cleaned

matricepropre = propre("speeches-20231215","cleaned")
print(matricepropre)


