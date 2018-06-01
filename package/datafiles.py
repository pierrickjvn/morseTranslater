def getData():
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

    return contenu, nom_fichier

def create_dico(fichier, sens):
    with open(fichier, 'r') as base :
        donnees = base.read()

    l_donnees = donnees.split()

    dico = {}
    for donnee in l_donnees :
        lettre, morse = donnee.split(':')
        if sens == 'tvm' :
            dico[lettre] = morse
        elif sens == 'mvt' :
            dico[morse] = lettre

    return dico
