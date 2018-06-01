# -*-coding:utf-8 -*

import os

from package.datafiles import *
from package.translate import *
from package.display import *

choix = Dintro()


if choix == 1 :
    sens = 'tvm'

    Dchoix(sens)

    contenu, nom_fichier = getData()

    dico = create_dico('ressources/morse.txt', sens)
    traduction = trad(contenu, dico, sens)

    with open(nom_fichier + '-TRADUIT.txt', 'w') as fichier_traduit :
       fichier_traduit.write(traduction)

    Dfin_trad(nom_fichier)

elif choix == 2 :
    sens = 'mvt'

    Dchoix(sens)

    contenu, nom_fichier = getData()

    dico = create_dico('ressources/morse.txt', sens)
    traduction = trad(contenu, dico, sens)

    with open(nom_fichier + '-TRADUIT.txt', 'w') as fichier_traduit :
       fichier_traduit.write(traduction)

    Dfin_trad(nom_fichier)

# elif choix == 3 :
#     sens = '3'
#
#     Dchoix(sens)
#
#     choi = int(input(
#     "1 - Traduction de texte en morse\n",
#     "2 - Traduction de morse en texte\n",
#     '\n',
#     "Veuillez choisir le sens de votre traduction "))
#
#     if choi == 1 :
#         sens = tvm
#     elif choi == 2 :
#         sens = mvt
#
#     dico = create_dico('ressources/morse.txt', sens)
#     contenu = input("")
