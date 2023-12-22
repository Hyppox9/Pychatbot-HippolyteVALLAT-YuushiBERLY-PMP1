import os


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
        print(L3)
        matrice_cleaned.append(L3)

        f.close()
    return matrice_cleaned


matricepropre = propre("speeches", "cleaned")
print(matricepropre)