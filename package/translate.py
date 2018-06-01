def trad(contenu, dico):
    probleme = ['\n',' ', ',', ';']
    l_traduction = []

    contenu = contenu.upper()
    contenu.upper()
    for lettre in contenu :
        if lettre not in probleme :
            l_traduction.append(dico[lettre])
        if lettre == '\n':
            l_traduction.append('\n')
    traduction = " ".join(l_traduction)

    return traduction
