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
