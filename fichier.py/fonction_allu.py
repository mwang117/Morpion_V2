import random

def allumettes(score_jou1 : list[int], score_jou2 : list[int], score_rob1 : list[int], score_rob2 : list[int], indice : int, type : int) -> int :
    """
    #-------------------------------------------------------------------------------------
    Fonction qui va prendre en paramètre d'entrée, les scores des deux joueurs et des 
    deux machines et va les renvoyer après la fin du jeu. 
    Des possibilités de mode de jeu ainsi que des difficultés pour certains modes. Le
    mode facile et difficile pour Joueur / Machine et Machine / Machine.
    JEU D'ALLUMETTE
    #-------------------------------------------------------------------------------------
    """
    
    #règle
    print("Il y a 20 allumettes.")
    print("Chacun son tour attrape 1, 2 ou 3 allumettes.")
    print("Le premier qui attrape la dernière allumette a gagné !")
    print("\n" * 2)
        
    nb_allu : int
    preleve : int
    k2 : int
    k3 : int
    k : int
    nb_partie : int
    difficulte : int
    aide : list[int]                #liste des différentes possibilités du jeu
    aide_enlev : list[int]          #liste de ce qu'il faut faire dans les différents cas, par exemple, s'il reste 4 allumettes, il faut en enlever 3
    i : int
    
    k2 = 2
    k3 = 0
    k = 1
    preleve = 0
    difficulte = 0
    i = 0
    aide = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    aide_enlev = [3, 2, 1, 1, 3, 2, 1, 1, 3, 2, 1, 1, 3, 2, 1, 1, 3, 2, 1]
    nb_partie = int(input("Veuilez saisir le nombre de partie que vous voulez jouer :"))

    while (nb_partie != 0) :
        
#--------------------------------------------------------------------------------------------------------------------------------------------------        

        #une partie contre un vrai joueur
        if (type == 2) :
            nb_allu = 20
            
            #condition, le joueur qui doit retirer la dernière allumette a perdu 
            while (nb_allu != 1) :
                print("\n" * 2)
                
                print("il reste", nb_allu, "allumettes")
                print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                preleve = int(input("Votre saisi :"))
                
                #condition soit 1 ou 2 ou 3
                while (preleve != 1) and (preleve != 2) and (preleve != 3) :
                    print("Vous ne pouvez pas retirer", preleve, "allumettes")
                    print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                    preleve = int(input("Votre saisi :"))
                
                #condition pour qu'il reste 1 allumette à la fin 
                while ((nb_allu == 3) and (preleve == 3)) or (nb_allu == 2) and ((preleve == 2) or (preleve == 3)) :
                    print("Vous ne pouvez pas retirer", preleve, "allumettes")
                    print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                    preleve = int(input("Votre saisi :"))      
                nb_allu = nb_allu - preleve
                
                #pour permuter entre joueur 1 et joueur 2
                k3 = k
                k = k2
                k2 = k3
                
            print("\n" * 2)
            print("il reste", nb_allu, "allumettes")    
            print("Joueur", k, "a perdu")
            nb_partie = nb_partie - 1
            
            #le nombre 1 c'est pour le joueur 1 mais le programme fait que k permute sur l'autre chiffre à la fin
            if k == 1 :
                score_jou2[indice] = score_jou2[indice] + 1
            else: 
                score_jou1[indice] = score_jou1[indice] + 1
        
#--------------------------------------------------------------------------------------------------------------------------------------------------        
        
        #une partie contre une machine 
        else :
            if (type == 1) :
                nb_allu = 20
                
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
                    
                    while (nb_allu != 1) :
                        print("\n" * 2)
                        
                        print("il reste", nb_allu, "allumettes")
                        
                        #condition pour déterminer si c'est le joueur ou la machine qui joue, le chiffre 1 pour le joueur et 2 pour la machine
                        if (k == 1) :
                            print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3")
                            preleve = int(input("Votre saisi :"))
                        else :
                            print("C'est au tour de la machine de jouer")
                            preleve = random.randint(1, 3)
                        
                        while (preleve != 1) and (preleve != 2) and (preleve != 3) :
                            print("Vous ne pouvez pas retirer", preleve, "allumettes")
                            print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                            preleve = int(input("Votre saisi :"))
                        
                        while ((nb_allu == 3) and (preleve == 3)) or (nb_allu == 2) and ((preleve == 2) or (preleve == 3)) :
                            if (k == 1) :
                                print("Vous ne pouvez pas retirer", preleve, "allumettes")
                                print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                                preleve = int(input("Votre saisi :"))   
                            else :
                                preleve = random.randint(1, 3)
                                
                        nb_allu = nb_allu - preleve
                        
                        k3 = k
                        k = k2
                        k2 = k3
                    
                    print("\n" * 2)
                    print("il reste", nb_allu, "allumettes")    
                    
                    if (k == 1) :
                        print("joueur 1 a perdu")
                    else :
                        print("machine 2 a perdu")
                    
                    nb_partie = nb_partie - 1
                    
                    if (k == 1) :
                        score_rob2[indice] = score_rob2[indice] + 1
                    else: 
                        score_jou1[indice] = score_jou1[indice] + 1
                        
#-------------------------------------------------------------------------------------------------------------------------------------------------- 
            
                #difficulté difficle 
                else :
                    while (nb_allu != 1) :
                        print("\n" * 2)
                        
                        print("il reste", nb_allu, "allumettes")

                        if (k == 1) :
                            print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3")
                            preleve = int(input("Votre saisi :"))
                        else :
                            print("C'est au tour de la machine de jouer")
                            
                            #boucle for pour traverser la liste "aide"
                            for i in range(0, 19) :
                                
                                #condition dans quelle possibilité on se trouve actuellement 
                                if (nb_allu == aide[i]) :
                                    preleve = aide_enlev[i]
                                    
                        while (preleve != 1) and (preleve != 2) and (preleve != 3) :
                            print("Vous ne pouvez pas retirer", preleve, "allumettes")
                            print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                            preleve = int(input("Votre saisi :"))
                        
                        while ((nb_allu == 3) and (preleve == 3)) or (nb_allu == 2) and ((preleve == 2) or (preleve == 3)) :
                            if (k == 1) :
                                print("Vous ne pouvez pas retirer", preleve, "allumettes")
                                print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                                preleve = int(input("Votre saisi :"))   
                            else :
                                for i in range(0, 19) : 
                                    if (nb_allu == aide[i]) :
                                        preleve = aide_enlev[i]
                                
                        nb_allu = nb_allu - preleve
                        
                        k3 = k
                        k = k2
                        k2 = k3
                    
                    print("\n" * 2)
                    print("il reste", nb_allu, "allumettes")    
                    
                    if (k == 1) :
                        print("joueur 1 a perdu")
                    else :
                        print("machine 2 a perdu")
                        
                    nb_partie = nb_partie - 1
                    
                    if k == 1 :
                        score_rob2[indice] = score_rob2[indice] + 1
                    else: 
                        score_jou1[indice] = score_jou1[indice] + 1
                
#-------------------------------------------------------------------------------------------------------------------------------------------------- 
            
            #condition, machine contre machine
            else :
                nb_allu = 20
                
                print("Veuillez choisir la difficulté de la machine")
                print("1 pour facile et 2 pour difficile")
                difficulte = int(input("Votre choix :"))
                
                while (difficulte != 1) and (difficulte != 2) :
                    print("Votre saisi est fausse !!!")
                    print("Veuillez choisir la difficulté de la machine")
                    print("1 pour facile et 2 pour difficile")
                    difficulte = int(input("Votre choix :"))
                    
                    
                #difficulté facile
                if (difficulte == 1) :
                    
                    while (nb_allu != 1) :
                        print("\n" * 2)
                        
                        print("il reste", nb_allu, "allumettes")
                        
                        #condition, le chiffre 1 pour la machine 1 pour le chiffre 2 pour la machine 2
                        if (k == 1) :
                            print("C'est au tour de la machine 1 de jouer")
                            preleve = random.randint(1, 3)
                        else :
                            print("C'est au tour de la machine 2 de jouer")
                            preleve = random.randint(1, 3)
                        
                        while (preleve != 1) and (preleve != 2) and (preleve != 3) :
                            print("Vous ne pouvez pas retirer", preleve, "allumettes")
                            print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                            preleve = int(input("Votre saisi :"))
                        
                        while ((nb_allu == 3) and (preleve == 3)) or (nb_allu == 2) and ((preleve == 2) or (preleve == 3)) :
                            if (k == 1) :
                                print("Vous ne pouvez pas retirer", preleve, "allumettes")
                                print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                                preleve = int(input("Votre saisi :"))   
                            else :
                                preleve = random.randint(1, 3)
                                
                        nb_allu = nb_allu - preleve
                        
                        k3 = k
                        k = k2
                        k2 = k3
                        
                    print("\n" * 2)    
                    print("il reste", nb_allu, "allumettes")    
                    
                    if (k == 1) :
                        print("machine 1 a perdu")
                    else :
                        print("machine 2 a perdu")
                    
                    nb_partie = nb_partie - 1
                    
                    if k == 1 :
                        score_rob2[indice] = score_rob2[indice] + 1
                    else: 
                        score_rob1[indice] = score_rob1[indice] + 1
                        
#-------------------------------------------------------------------------------------------------------------------------------------------------- 

                #difficulté difficle 
                else :
                    while (nb_allu != 1) :
                        print("\n" * 2)
                        
                        print("il reste", nb_allu, "allumettes")
                        
                        if (k == 1) :
                            print("C'est au tour de la machine 1 de jouer")
                            for i in range(0, 19) :
                                if (nb_allu == aide[i]) :
                                    preleve = aide_enlev[i]
                        else :
                            print("C'est au tour de la machine 2 de jouer")
                            for i in range(0, 19) :
                                if (nb_allu == aide[i]) :
                                    preleve = aide_enlev[i]
                                    
                        while (preleve != 1) and (preleve != 2) and (preleve != 3) :
                            print("Vous ne pouvez pas retirer", preleve, "allumettes")
                            print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                            preleve = int(input("Votre saisi :"))
                        
                        while ((nb_allu == 3) and (preleve == 3)) or (nb_allu == 2) and ((preleve == 2) or (preleve == 3)) :
                            if (k == 1) :
                                print("Vous ne pouvez pas retirer", preleve, "allumettes")
                                print("Joueur", k, "veuillez saisir un chiffre entre 1, 2 ou 3 :")
                                preleve = int(input("Votre saisi :"))   
                            else :
                                for i in range(0, 19) : 
                                    if (nb_allu == aide[i]) :
                                        preleve = aide_enlev[i]
                                
                        nb_allu = nb_allu - preleve
                        
                        k3 = k
                        k = k2
                        k2 = k3
                        
                    print("\n" * 2)
                    print("il reste", nb_allu, "allumettes")    
                    
                    if (k == 1) :
                        print("machine 1 a perdu")
                    else :
                        print("machine 2 a perdu")
                    
                    nb_partie = nb_partie - 1
                    
                    if k == 1 :
                        score_rob2[indice] = score_rob2[indice] + 1
                    else: 
                        score_rob1[indice] = score_rob1[indice] + 1
                    
#--------------------------------------------------------------------------------------------------------------------------------------------------             
        
        print("\n" * 2)
        indice = 1                       
        print("le score du joueur 1 :", score_jou1[indice])
        print("le score du joueur 2 :", score_jou2[indice])
        print("le score du robot 1 :", score_rob1[indice])
        print("le score du robot 2 :", score_rob2[indice])

    return score_jou1, score_jou2, score_rob1, score_rob2