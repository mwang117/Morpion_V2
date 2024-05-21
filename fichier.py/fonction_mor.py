import random

def morpions(score_jou1 : list[int], score_jou2 : list[int], score_rob1 : list[int], score_rob2 : list[int], indice : int, type : int) -> int :
    """
    #-------------------------------------------------------------------------------------
    Fonction qui va prendre en paramètre d'entrée, les scores des deux joueurs et des 
    deux machines et va les renvoyer après la fin du jeu. 
    Des possibilités de mode de jeu pour certains modes. Seulement la difficulté facile
    pour Joueur / Machine et Machine / Machine.
    JEU DE MORPION
    #-------------------------------------------------------------------------------------
    """

    table : list[list[str]]     #liste à double dimension afin d'avoir 3 lignes et 3 colonnes
    nb_colonne : int
    nb_ligne : int
    compteur : int
    gagne_verticale : int
    gagne_horizontale : int
    gagne_diago : int
    k2 : int
    k3 : int
    k : int
    i : int
    j : int
    nb_partie : int
    
    i = 0
    j = 0
    compteur = 0             
    gagne_verticale = 0
    gagne_horizontale = 0
    gagne_diago = 0
    
    #permuter entre joueur 1 et 2
    #joueur1 = X et joueur2 = O
    k2 = 2
    k3 = 0
    k = 1
    
    #règle
    print("Jeu de Morpion simple")
    print("X pour le joueur 1 ou machine 1")
    print("O pour le joueur 2 ou machine 2")
            
    nb_partie = int(input("\nVeuilez saisir le nombre de partie que vous voulez jouer :"))

#--------------------------------------------------------------------------------------------------------------------------------------------------   

    while nb_partie != 0 :
        nb_partie = nb_partie - 1
        table = [
          ['-', '-', '-'],
          ['-', '-', '-'],
          ['-', '-', '-']
        ]
        compteur = 0             
        gagne_verticale = 0
        gagne_horizontale = 0
        gagne_diago = 0
        
        k2 = 2
        k3 = 0
        k = 1
        
        #affichage de la matrice, pour qu'il ressemble à un morpion
        for i in range(0, 3) :
            print("\n")
            for j in range(0, 3) :
                print(table[i][j], end="  ")
        
        print("\n" * 2)
        
#--------------------------------------------------------------------------------------------------------------------------------------------------   

        #condition, joueur 1 contre joueur 2
        if (type == 2) :        
            
            #condtion pour la partie se termine   
            while (compteur != 9) and ((gagne_diago == 0) and (gagne_horizontale == 0) and (gagne_verticale == 0)) :
                print("\n" * 2, "Joueur", k,"Veuillez choisir le numéro de la ligne puis le numéro de la colonne !")
                
                
                nb_ligne = int(input("\nVeuillez saisir la ligne :"))
                #condition de la ligne, soit 1, 2 ou 3
                while (nb_ligne != 1) and (nb_ligne != 2) and (nb_ligne !=3) :
                    print("Veuillez choisir entre 1, 2 ou 3 !!!")
                    nb_ligne = int(input("Veuillez saisir la ligne :"))
                
                
                nb_colonne = int(input("\nVeuillez saisir la colonne :"))
                #condition de la colonne, soit 1, 2 ou 3
                while (nb_colonne != 1) and (nb_colonne != 2) and (nb_colonne !=3) :
                    print("Veuillez choisir entre 1, 2 ou 3 !!!")
                    nb_colonne = int(input("Veuillez saisir la colonne :"))
                
                
                #condition pour voir si la case est déjà prise ou non
                #moins 1 sur tout puisque la table commence à 0
                while (table[nb_ligne - 1][nb_colonne - 1] == "O") or (table[nb_ligne - 1][nb_colonne - 1] == "X") :
                    
                    print("\n" * 50)
                    for i in range(0, 3) :
                        print("\n")
                        for j in range(0, 3) :
                            print(table[i][j], end="  ")
                    
                            
                    print("\n" * 2, "Votre case choisie est déjà prise !!!")
                    nb_ligne = int(input("Veuillez saisir la ligne :"))
                    
                    #condition de la ligne, soit 1, 2 ou 3
                    while (nb_ligne != 1) and (nb_ligne != 2) and (nb_ligne !=3) :
                        print("Veuillez choisir entre 1, 2 ou 3 !!!")
                        nb_ligne = int(input("Veuillez saisir la ligne :"))
                
                
                    nb_colonne = int(input("Veuillez saisir la colonne :"))
                    
                    #condition de la colonne, soit 1, 2 ou 3
                    while (nb_colonne != 1) and (nb_colonne != 2) and (nb_colonne !=3) :
                        print("Veuillez choisir entre 1, 2 ou 3 !!!")
                        nb_colonne = int(input("Veuillez saisir la colonne :"))
                
                
                if (k) == 1 :
                    table[nb_ligne - 1][nb_colonne - 1] = "X"
                else : 
                    table[nb_ligne - 1][nb_colonne - 1] = "O"
                
                
                compteur = compteur + 1    
                gagne_verticale, k = gagne_vertical(table, k)
                gagne_diago, k = gagne_dia(table, k)
                gagne_horizontale, k = gagne_horizontal(table, k)
               
                #permuter entre joueur 1 et 2    
                k3 = k
                k = k2
                k2 = k3
                
                print("\n" * 50)
                for i in range(0, 3) :
                    print("\n")
                    for j in range(0, 3) :
                        print(table[i][j], end="  ")
            
            print("\n")
            
            if ((compteur == 9) and ((gagne_diago == 0) and (gagne_horizontale == 0) and (gagne_verticale == 0))) :
                print("match nul")
                break
             
            print("Joueur", k, "a perdu")

            #le nombre 1 c'est pour le joueur 1 mais le programme fait que k permute sur l'autre chiffre à la fin
            if k == 1 :
                score_jou2[indice] = score_jou2[indice] + 1
            else: 
                score_jou1[indice] = score_jou1[indice] + 1

#--------------------------------------------------------------------------------------------------------------------------------------------------   

        #condition joueur 1 contre machine 2
        else :
            if (type == 1) :
                print("Veuillez choisir la difficulté de la machine")
                print("1 pour facile et 2 pour difficile")
                difficulte = int(input("Votre choix :"))
                
                while (difficulte != 1) and (difficulte != 2) :
                    print("Votre saisi est fausse !!!")
                    print("Veuillez choisir la difficulté de la machine")
                    print("1 pour facile et 2 pour difficile")
                    difficulte = int(input("Votre choix :"))
                    
                #condition, une machine avec une difficulté facile
                if (difficulte == 1) :
                    while (compteur != 9) and ((gagne_diago == 0) and (gagne_horizontale == 0) and (gagne_verticale == 0)) :
                        
                        #condition pour déterminer si c'est le joueur ou la machine qui joue, le chiffre 1 pour le joueur et 2 pour la machine
                        if (k == 1) :
                            print("\n")
                            print("C'est au tour du joueur 1 de jouer")
                            
                            nb_ligne = int(input("\nVeuillez saisir la ligne :"))
                            while (nb_ligne != 1) and (nb_ligne != 2) and (nb_ligne !=3) :
                                print("Veuillez choisir entre 1, 2 ou 3 !!!")
                                nb_ligne = int(input("Veuillez saisir la ligne :"))
                                
                            nb_colonne = int(input("\nVeuillez saisir la colonne :"))
                            while (nb_colonne != 1) and (nb_colonne != 2) and (nb_colonne !=3) :
                                print("Veuillez choisir entre 1, 2 ou 3 !!!")
                                nb_colonne = int(input("Veuillez saisir la colonne :")) 
                                  
                            while (table[nb_ligne - 1][nb_colonne - 1] == "O") or (table[nb_ligne - 1][nb_colonne - 1] == "X") :
                            
                                print("\n" * 50)
                                for i in range(0, 3) :
                                    print("\n")
                                    for j in range(0, 3) :
                                        print(table[i][j], end="  ")
    
                                print("\n" * 2, "Votre case choisie est déjà prise !!!")
                                nb_ligne = int(input("Veuillez saisir la ligne :"))

                                while (nb_ligne != 1) and (nb_ligne != 2) and (nb_ligne !=3) :
                                    print("Veuillez choisir entre 1, 2 ou 3 !!!")
                                    nb_ligne = int(input("Veuillez saisir la ligne :"))
                            
                                nb_colonne = int(input("Veuillez saisir la colonne :"))

                                while (nb_colonne != 1) and (nb_colonne != 2) and (nb_colonne !=3) :
                                    print("Veuillez choisir entre 1, 2 ou 3 !!!")
                                    nb_colonne = int(input("Veuillez saisir la colonne :"))

                            table[nb_ligne - 1][nb_colonne - 1] = "X"

                            compteur = compteur + 1    
                            gagne_verticale, k = gagne_vertical(table, k)
                            gagne_diago, k = gagne_dia(table, k)
                            gagne_horizontale, k = gagne_horizontal(table, k)

                            k3 = k
                            k = k2
                            k2 = k3
                            
                            print("\n" * 50)
                            for i in range(0, 3) :
                                print("\n")
                                for j in range(0, 3) :
                                    print(table[i][j], end="  ")    
                        else :
                            print("\n")
                            print("C'est au tour de la machine de jouer")
                            
                            nb_ligne = random.randint(1,3)
                            nb_colonne = random.randint(1,3)
                                  
                            while (table[nb_ligne - 1][nb_colonne - 1] == "O") or (table[nb_ligne - 1][nb_colonne - 1] == "X") :

                                nb_ligne = random.randint(1,3)
                                nb_colonne = random.randint(1,3)
 
                            table[nb_ligne - 1][nb_colonne - 1] = "O"

                            compteur = compteur + 1    
                            gagne_verticale, k = gagne_vertical(table, k)
                            gagne_diago, k = gagne_dia(table, k)
                            gagne_horizontale, k = gagne_horizontal(table, k)

                            k3 = k
                            k = k2
                            k2 = k3
                            
                            print("\n" * 50)
                            for i in range(0, 3) :
                                print("\n")
                                for j in range(0, 3) :
                                    print(table[i][j], end="  ")
                            
                    print("\n")
                    
                    if ((compteur == 9) and ((gagne_diago == 0) and (gagne_horizontale == 0) and (gagne_verticale == 0))) :
                        print("match nul")
                        break
                            
                    if (k == 1) :
                        print("joueur 1 a perdu")
                    else :
                        print("machine 2 a perdu")
                    
                    if k == 1 :
                        score_rob2[indice] = score_rob2[indice] + 1
                    else: 
                        score_jou1[indice] = score_jou1[indice] + 1
            
#--------------------------------------------------------------------------------------------------------------------------------------------------
            
            #condtion, machine 1 contre machine 2
            else :
                print("Veuillez choisir la difficulté de la machine")
                print("1 pour facile et 2 pour difficile")
                difficulte = int(input("Votre choix :"))
                
                while (difficulte != 1) and (difficulte != 2) :
                    print("Votre saisi est fausse !!!")
                    print("Veuillez choisir la difficulté de la machine")
                    print("1 pour facile et 2 pour difficile")
                    difficulte = int(input("Votre choix :"))
                    
                #condition, une machine avec une difficulté facile
                if (difficulte == 1) :
                    while (compteur != 9) and ((gagne_diago == 0) and (gagne_horizontale == 0) and (gagne_verticale == 0)) :
                        
                        #condition pour déterminer si c'est le joueur ou la machine qui joue, le chiffre 1 pour le joueur et 2 pour la machine
                        if (k == 1) :
                            print("\n")
                            print("C'est au tour du machine 1 de jouer")
                            
                            nb_ligne = random.randint(1,3)
                            nb_colonne = random.randint(1,3)
                                  
                            while (table[nb_ligne - 1][nb_colonne - 1] == "O") or (table[nb_ligne - 1][nb_colonne - 1] == "X") :

                                nb_ligne = random.randint(1,3)
                                nb_colonne = random.randint(1,3)
 
                            table[nb_ligne - 1][nb_colonne - 1] = "X"

                            compteur = compteur + 1    
                            gagne_verticale, k = gagne_vertical(table, k)
                            gagne_diago, k = gagne_dia(table, k)
                            gagne_horizontale, k = gagne_horizontal(table, k)

                            k3 = k
                            k = k2
                            k2 = k3
                            
                            print("\n" * 50)
                            for i in range(0, 3) :
                                print("\n")
                                for j in range(0, 3) :
                                    print(table[i][j], end="  ")    
                        else :
                            print("\n")
                            print("C'est au tour de la machine 2 de jouer")
                            
                            nb_ligne = random.randint(1,3)
                            nb_colonne = random.randint(1,3)
                                  
                            while (table[nb_ligne - 1][nb_colonne - 1] == "O") or (table[nb_ligne - 1][nb_colonne - 1] == "X") :

                                nb_ligne = random.randint(1,3)
                                nb_colonne = random.randint(1,3)
 
                            table[nb_ligne - 1][nb_colonne - 1] = "O"

                            compteur = compteur + 1    
                            gagne_verticale, k = gagne_vertical(table, k)
                            gagne_diago, k = gagne_dia(table, k)
                            gagne_horizontale, k = gagne_horizontal(table, k) 

                            k3 = k
                            k = k2
                            k2 = k3
                            
                            print("\n" * 50)
                            for i in range(0, 3) :
                                print("\n")
                                for j in range(0, 3) :
                                    print(table[i][j], end="  ")
                    
                    print("\n")
                    
                    if ((compteur == 9) and ((gagne_diago == 0) and (gagne_horizontale == 0) and (gagne_verticale == 0))) :
                        print("match nul")
                        break
                    
                    if (k == 1) :
                        print("machine 1 a perdu")
                    else :
                        print("machine 2 a perdu")
                    
                    if k == 1 :
                        score_rob2[indice] = score_rob2[indice] + 1
                    else: 
                        score_rob1[indice] = score_rob1[indice] + 1
                
#--------------------------------------------------------------------------------------------------------------------------------------------------                                
                       
        indice = 2                 
        print("le score du joueur 1 :", score_jou1[indice])
        print("le score du joueur 2 :", score_jou2[indice])
        print("le score du robot 1 :", score_rob1[indice])
        print("le score du robot 2 :", score_rob2[indice])
    
    return(score_jou1, score_jou2, score_rob1, score_rob2)
        
     
     
     
        
def gagne_vertical(table : list[list[str]], k : int) -> int :
    """
    #-------------------------------------------------------------------------------------
    Paramètre d'entrée : la liste à double dimension
    Paramètre de sortie : entier positif, valid, 0 ou 1
    Fonction qui va prendre en paramètre d'entrée la liste à double dimension et
    va envoyer un entier, soit 0, soit 1. 0 pour non valide et 1 pour valide. Une fonction 
    pour savoir si le joueur a gagné de manière verticale.
    #-------------------------------------------------------------------------------------
    """
    
    valid : int
    i : int
    
    i = 0
    valid = 0  
    
    for i in range(0, 3) :
        valid = 0
        if (table[0][i] == table[1][i]) and (table[1][i] == table[2][i]) and table[0][i] != "-" :
            valid = valid + 1 
            return valid, k
        
    return valid, k
            
            
            
            
            
def gagne_horizontal(table : list[list[str]], k : int) -> int :
    """
    #-------------------------------------------------------------------------------------
    Paramètre d'entrée : la liste à double dimension
    Paramètre de sortie : entier positif, valid, 0 ou 1
    Fonction qui va prendre en paramètre d'entrée la liste à double dimension et
    va envoyer un entier, soit 0, soit 1. 0 pour non valide et 1 pour valide. Une fonction 
    pour savoir si le joueur a gagné de manière horzontale.
    #-------------------------------------------------------------------------------------
    """
    
    valid : int
    i : int
    
    i = 0
    valid = 0
    
    for i in range(0, 3) :
        valid = 0
        if ((table[i][0] == table[i][1]) and (table[i][1] == table[i][2]) and table[i][0] != "-") :
            valid = valid + 1
            return valid, k
        
    return valid, k
      
      
      
      
      
def gagne_dia(table : list[list[str]], k : int) -> int :
    """
    #-------------------------------------------------------------------------------------
    Paramètre d'entrée : la liste à double dimension
    Paramètre de sortie : entier positif, valid, 0 ou 1
    Fonction qui va prendre en paramètre d'entrée la liste à double dimension et
    va envoyer un entier, soit 0, soit 1. 0 pour non valide et 1 pour valide. Une fonction 
    pour savoir si le joueur a gagné de manière diagonale.
    #-------------------------------------------------------------------------------------
    """
    
    valid : int
    i : int
    
    i = 0
    valid = 0
    
    for i in range(0, 1) :
        valid = 0
        if ((table[i][0] == table[1][1]) and (table[1][1] == table[2][2]) and (table[i][0] != "-")) or (
            (table[i][2] == table[1][1]) and (table[1][1] == table[2][0]) and (table[i][2] != "-")) :
            valid = valid + 1
            return valid, k
        
    return valid, k