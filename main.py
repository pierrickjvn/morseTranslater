# -*-coding:utf-8 -*

import os

from package.createD import *
from package.translate import *
from package.display import *

choix = Dintro()


if choix == 1 :
    sens = 'tvm'

    Dchoix(sens)

    again = True
    while again == True :
        nom_fichier = str(input('Quel est le nom du fichier ? '))
        try :
            fichier = open(nom_fichier + '.txt', 'r')
        except FileNotFoundError:
            print("Le nom du fichier est invalide, veuillez vérifier que le fichier est dans le même dossier que le programme et que vous n'avez pas entré l'extension.")
        else :
            again = False

    contenu = fichier.read()
    fichier.close()

    dico = create_dico('ressources/morse.txt', sens)
    traduction = trad(contenu, dico)

    with open(nom_fichier + '-TRADUIT.txt', 'w') as fichier_traduit :
       fichier_traduit.write(traduction)

    Dfin_trad()

elif choix == 2 :
    sens = 'mvt'

    Dchoix(sens)

    again = True
    while again == True :
        nom_fichier = str(input('Quel est le nom du fichier ? '))
        try :
            fichier = open(nom_fichier + '.txt', 'r')
        except FileNotFoundError:
            print("Le nom du fichier est invalide, veuillez vérifier que le fichier est dans le même dossier que le programme et que vous n'avez pas entré l'extension.")
        else :
            again = False

    contenu = fichier.read()
    fichier.close()

    dico = create_dico('ressources/morse.txt', sens)
    traduction = trad(contenu, dico)

    with open(nom_fichier + '-TRADUIT.txt', 'w') as fichier_traduit :
       fichier_traduit.write(traduction)

    Dfin_trad()
