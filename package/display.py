import time


def Dintro():
    print(
    "\n--------------------PROJET MORSE--------------------\n",
    "\n",
    "Bonjour :)\n",
    "\n",
    "Menu :\n",
    "1 - Traduction de fichier texte en morse\n",
    "2 - Traduction de fichier morse en texte\n",
    "3 - Traduction en direct\n",
    "4 - \n",
    "5 - \n",
    "\n")

    good = False
    rep_possibles = ['1','2','3','4','5']
    while good == False :

        choix = input('Veuillez saisir votre choix : ')
        if choix in rep_possibles :
            good = True
        else :
            print('Veuillez rentrer le nombre correspondant à votre choix.')

    choix = int(choix)

    return choix

def Dchoix(sens):
    time.sleep(0.1)
    print("\n")
    time.sleep(0.1)
    if sens == 'tvm' :
        print("---Traduction de fichier texte en morse---")
    elif sens == 'mvt' :
        print("---Traduction de fichier morse en texte---")
    time.sleep(0.1)
    print("\n")

def Dfin_trad():
    i = 0
    while i < 3 :
        time.sleep(0.3)
        print('.')
        i += 1

    print('Le fichier a été traduit et un nouveau fichier a été créé.\n')
