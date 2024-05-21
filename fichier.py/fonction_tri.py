def tri_bulle(liste : list[int], liste_nom : list[str]) -> list[int] :
    """
    #-------------------------------------------------------------------------------------
    Fonction qui va prendre en paramètre d'entrée, la liste des scores des joueurs. Et
    va renvoyer en paramètre de sortie, la liste triée. Fonction de tri à bulle
    #-------------------------------------------------------------------------------------
    """
    i : int
    reserve : int
    reserve_str : str
    verite : bool
    nb_entier : int
    
    i = 0
    reserve = 0
    verite = True
    nb_entier = len(liste)
    
    while (verite) and (nb_entier > 0) :
        
        #si rien ne s'exécute, la boucle sera terminé
        verite = False
        
        #condition nb_entier qui doit toujours être inférieur à sa taille
        #va rechercher dans tous le tableau
        for i in range(0, nb_entier-1) :
            
            #condition pour l'échange entre les deux valeurs consécutifs
            if liste[i] > liste[i+1] :
                reserve = liste[i]
                reserve_str = liste_nom[i]
                
                liste[i] = liste[i+1]
                liste_nom[i] = liste_nom[i+1]
                
                liste_nom[i+1] = reserve_str
                liste[i+1] = reserve
                
                verite = True
        nb_entier = nb_entier - 1
    
    return(liste, liste_nom)
