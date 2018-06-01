def trad(contenu, dico, sens):
    probleme = ['\n',' ', ',', ';']
    l_traduction = []

    if sens == 'tvm' :
        contenu = contenu.upper()
    if sens == 'mvt':
        contenu = contenu.split(" ")
    for elt in contenu :
        if elt not in probleme :
            l_traduction.append(dico[elt])
        if elt == '\n':
            l_traduction.append('\n')
    traduction = " ".join(l_traduction)

    return traduction
