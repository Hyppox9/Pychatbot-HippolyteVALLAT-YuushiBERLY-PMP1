import Fonctions

"""
le menu sert à executer ce que l'on veut faire
"""

sugemenu = 0
print("Choisissez ce que vous voulez faire:",'\n',"1 : lister le nom des présidents",'\n',"2 : afficher le dossier cleaned",'\n',"3 : si vous voulez afficher le TF ",'\n',"4 : si vous voulez afficher le IDF ",'\n',"5 : si vous voulez afficher le TF-IDF ",'\n',"6 : si vous voulez afficher le Max IDF ",'\n',"7 : si vous voulez afficher les mots les moins importants",'\n',"8 : si vous avez fini")

while sugemenu != 8:
    sugemenu = int(input())
    if sugemenu == 1:
        print(Fonctions.extract_names("speeches"))
    if sugemenu == 2:
        print(Fonctions.matricepropre)
    if sugemenu == 3:
        print("quel fichier?")
        calvin = input()
        print(Fonctions.TF(calvin, "cleaned"))
    if sugemenu == 4:
        print(Fonctions.IDF("cleaned"))
    if sugemenu == 5:
        print(Fonctions.TF_IDF("cleaned"))
    if sugemenu == 6:
        print(Fonctions.max_idf("cleaned"))
    if sugemenu == 7:
        print(Fonctions.less_important_words("cleaned"))


if sugemenu == 8:
    print("bye bye ! :) ")