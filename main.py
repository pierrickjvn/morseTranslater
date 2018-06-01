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
    traduction = trad(contenu, dico)

    with open(nom_fichier + '-TRADUIT.txt', 'w') as fichier_traduit :
       fichier_traduit.write(traduction)

    Dfin_trad()

elif choix == 2 :
    sens = 'mvt'

    Dchoix(sens)

    contenu, nom_fichier = getData()

    dico = create_dico('ressources/morse.txt', sens)
    traduction = trad(contenu, dico)

    with open(nom_fichier + '-TRADUIT.txt', 'w') as fichier_traduit :
       fichier_traduit.write(traduction)

    Dfin_trad()
