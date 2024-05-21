import random

def devinettes(score_jou1 : list[int], score_jou2 : list[int], score_rob1 : list[int], score_rob2 : list[int], indice : int, type : int) -> int :
    """
    #-------------------------------------------------------------------------------------
    Fonction qui va prendre en paramètre d'entrée, les scores des deux joueurs et des 
    deux machines et va les renvoyer après la fin du jeu. 
    Des possibilités de mode de jeu ainsi que des difficultés pour certains modes. Le
    mode facile et difficile pour Joueur / Machine et Machine / Machine.
    JEU DE DEVINETTE
    #-------------------------------------------------------------------------------------
    """
    
    nb_J1 : int
    nb_J2 : int
    nb_r1 : int
    nb_r2 : int
    Max : int
    tentative : int
    rejouer : str
    reponse : int

    Max = 0
    rejouer = ""
    tentative = 5
    reponse = 0
      
#-------------------------------------------------------------------------------------------------------------------------------------------------- 

    print("\n" *100)
    while True :
        print("\n" * 10)
        
        tentative = 5
        
        #règle
        print("Le joueur 1 choisi un entier et une intervalle")
        print("Le joueur 2 a 5 essais et s'il réussit à deviner l'entier, il gagne")
        print("Sinon le joueur 1 gagne")
        print("\n" *5)
        
        nb_J1 = 0
        nb_J2 = 0
        nb_r1 = 0
        nb_r2 = 0
        
        if (type == 2) :
        
            while (nb_J1 < 1 or nb_J1 > Max and Max < 1):
                Max = int(input("Joueur1, choisissez la limite maximale : "))
                nb_J1 = int(input("Choisissez votre nombre entier entre 1 et " + str(Max) + " : "))
            
            print("\n" * 100)
            while (tentative > 0) :
                
                nb_J2 = 0
                while(nb_J2 > Max or nb_J2 < 1) :
                    print("\n" * 3)
                    print("Joueur2, vous devez choisir un nombre entre 1 et "+ str(Max))
                    nb_J2 = int(input("Joueur2 choisissez un nombre : "))
                    
                    if (nb_J2 > Max or nb_J2 < 1):
                        print("Vous devez choisir un nombre dans la limite indiqué")
                    else :
                        break
                    
                tentative = tentative - 1
                
                print("\n" * 100)
                
                while reponse != 1 or reponse != 2 or reponse != 3 :
                    print("Joueur1, le nombre choisi par le Joueur2 est :", nb_J2)
                    reponse = int(input(print(nb_J2," est :"
                        "\n1. Plus petit que votre nombre"
                        "\n2. Plus grand que votre nombre"
                        "\n3. Egale à votre nombre")))

                    #réponsse du joueur 1 
                    print("\n" * 20)    
                    if reponse == 1 :                    
                        if nb_J2 < nb_J1 :
                            print("Le nombre du Joueur2 est bien trop petit")
                            break
                        else :
                            print("Menteur! Le nombre du Joueur2 n'est pas plus petit")
                    if reponse == 2 :  
                        if nb_J2 > nb_J1 :
                            print("Le nombre du Joueur2 est bien trop grand")
                            break
                        else :
                            print("Menteur! Le nombre du Joueur2 n'est pas plus grand")
                    if reponse == 3 :
                        if nb_J2 == nb_J1 :
                            print("C'est gagné !!")
                            break
                        else :
                            print("Menteur! Le Joueur2 n'a pas donné la bonne réponse")

                if nb_J2 == nb_J1:
                    break    
                print("il vous reste ",tentative, " tentatives")

                    
                
            if nb_J1 == nb_J2:
                print("Le joueur2 a remporté la partie")
                score_jou2[indice] = score_jou2[indice] + 1
            else :
                print("Le joueur 1 a remporté la partie ")
                score_jou1[indice] = score_jou1[indice] + 1
            rejouer = str(input("Voulez vous rejouer ? (oui/non) : "))
            
            if rejouer != "oui" :
                break

#-------------------------------------------------------------------------------------------------------------------------------------------------- 

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
                    while (nb_J1 < 1 or nb_J1 > Max and Max < 1):
                        Max = int(input("Joueur1, choisissez la limite maximale : "))
                        nb_J1 = int(input("Choisissez votre nombre entier entre 1 et " + str(Max) + " : "))
                    
                    print("\n" * 100)
                    while (tentative > 0) :
                        
                        nb_r2 = random.randint(1, Max)
                                   
                        tentative = tentative - 1
                        
                        print("\n" * 100)
                        
                        while reponse != 1 or reponse != 2 or reponse != 3 :
                            print("Joueur1, le nombre choisi par la machine est :", nb_r2)
                            reponse = int(input(print(nb_J2," est :"
                                "\n1. Plus petit que votre nombre"
                                "\n2. Plus grand que votre nombre"
                                "\n3. Egale à votre nombre")))

                            print("\n" * 20)    
                            if reponse == 1 :                    
                                if nb_r2 < nb_J1 :
                                    print("Le nombre de la machine est bien trop petit")
                                    break
                                else :
                                    print("Menteur! Le nombre de la machine n'est pas plus petit")
                            if reponse == 2 :  
                                if nb_r2 > nb_J1 :
                                    print("Le nombre de la machine est bien trop grand")
                                    break
                                else :
                                    print("Menteur! Le nombre de la machine n'est pas plus grand")
                            if reponse == 3 :
                                if nb_r2 == nb_J1 :
                                    print("C'est gagné !!")
                                    break
                                else :
                                    print("Menteur! de la machine n'a pas donné la bonne réponse")

                        if nb_r2 == nb_J1:
                            break    
                        print("il vous reste ",tentative, " tentatives")

                            
                        
                    if nb_J1 == nb_r2:
                        print("La machine a remporté la partie")
                        score_rob2[indice] = score_rob2[indice] + 1
                    else :
                        print("Le joueur 1 a remporté la partie ")
                        score_jou1[indice] = score_jou1[indice] + 1
                        
                    rejouer = str(input("Voulez vous rejouer ? (oui/non) : "))
                    
                    if rejouer != "oui" :
                        break
        
#-------------------------------------------------------------------------------------------------------------------------------------------------- 

                #difficulté difficile
                else :
                    while (nb_J1 < 1 or nb_J1 > Max and Max < 1):
                        Max = int(input("Joueur1, choisissez la limite maximale : "))
                        nb_J1 = int(input("Choisissez votre nombre entier entre 1 et " + str(Max) + " : "))
                    
                    nb_r2 = 100
                    
                    print("\n" * 100)
                    while (tentative > 0) :
                        
                        if (tentative != 1) :
                            if (nb_r2 > nb_J1) :
                                nb_r2 = nb_r2 // 2
                            else :
                                nb_r2 = nb_r2 + (nb_r2 // 2)
                        else : 
                            if (nb_r2 > nb_J1) :
                                nb_r2 = random.randint(nb_J1, nb_r2)
                            else :
                                nb_r2 = random.randint(nb_r2, nb_J1)
                                   
                        tentative = tentative - 1
                        
                        print("\n" * 100)
                        
                        while reponse != 1 or reponse != 2 or reponse != 3 :
                            print("Joueur1, le nombre choisi par la machine est :", nb_r2)
                            reponse = int(input(print(nb_J2," est :"
                                "\n1. Plus petit que votre nombre"
                                "\n2. Plus grand que votre nombre"
                                "\n3. Egale à votre nombre")))

                            print("\n" * 20)    
                            if reponse == 1 :                    
                                if nb_r2 < nb_J1 :
                                    print("Le nombre de la machine est bien trop petit")
                                    break
                                else :
                                    print("Menteur! Le nombre de la machine n'est pas plus petit")
                            if reponse == 2 :  
                                if nb_r2 > nb_J1 :
                                    print("Le nombre de la machine est bien trop grand")
                                    break
                                else :
                                    print("Menteur! Le nombre de la machine n'est pas plus grand")
                            if reponse == 3 :
                                if nb_r2 == nb_J1 :
                                    print("C'est gagné !!")
                                    break
                                else :
                                    print("Menteur! de la machine n'a pas donné la bonne réponse")

                        if nb_r2 == nb_J1:
                            break    
                        print("il vous reste ",tentative, " tentatives")

                            
                        
                    if nb_J1 == nb_r2:
                        print("La machine a remporté la partie")
                        score_rob2[indice] = score_rob2[indice] + 1
                    else :
                        print("Le joueur 1 a remporté la partie ")
                        score_jou1[indice] = score_jou1[indice] + 1
                        
                    rejouer = str(input("Voulez vous rejouer ? (oui/non) : "))
                    
                    if rejouer != "oui" :
                        break
        
#-------------------------------------------------------------------------------------------------------------------------------------------------- 

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
                    while (nb_r1 < 1 or nb_r1 > Max and Max < 1):
                        Max = random.randint(80, 100)
                        nb_r1 = random.randint(1, Max)
                    
                    print("\n" * 2)
                    while (tentative > 0) :
                        
                        nb_r2 = 0
                        while(nb_r2 > Max or nb_r2 < 1) :
                            print("\n" * 3)
                            nb_r2 = random.randint(1, Max)
                                   
                        tentative = tentative - 1
                        
                        print("\n" * 2)
                        
                        print("machine 1, le nombre choisi par la machine 2 est :", nb_r2)

                        print("\n" * 2)
                                              
                        if nb_r2 < nb_r1 :
                            print("Le nombre de la machine est bien trop petit") 
                            
                        if nb_r2 > nb_r1 :
                            print("Le nombre de la machine est bien trop grand")
                            
                        if nb_r2 == nb_r1 :
                            print("C'est gagné !!")
   
                        print("il reste ",tentative, " tentatives")        
                        
                    if nb_r1 == nb_r2:
                        print("La machine 2 a remporté la partie")
                        score_rob2[indice] = score_rob2[indice] + 1
                    else :
                        print("La machine 1 a remporté la partie ")
                        score_rob1[indice] = score_rob1[indice] + 1
                        
                    rejouer = str(input("Voulez vous rejouer ? (oui/non) : "))
                    
                    if rejouer != "oui" :
                        break
#-------------------------------------------------------------------------------------------------------------------------------------------------- 

                else :
                    while (nb_r1 < 1 or nb_r1 > Max and Max < 1):
                        Max = random.randint(80, 100)
                        nb_r1 = random.randint(1, Max)
                    
                    nb_r2 = 100
                    
                    print("\n" * 2)
                    while (tentative > 0) :
                        
                        if (tentative != 1) :
                            if (nb_r2 > nb_J1) :
                                nb_r2 = nb_r2 // 2
                            else :
                                nb_r2 = nb_r2 + (nb_r2 // 2)
                        else : 
                            if (nb_r2 > nb_J1) :
                                nb_r2 = random.randint(nb_J1, nb_r2)
                            else :
                                nb_r2 = random.randint(nb_r2, nb_J1)
                                   
                        tentative = tentative - 1
                        
                        print("\n" * 2)
                        
                        print("machine 1, le nombre choisi par la machine 2 est :", nb_r2)

                        print("\n" * 2)
                                              
                        if nb_r2 < nb_r1 :
                            print("Le nombre de la machine est bien trop petit") 
                            
                        if nb_r2 > nb_r1 :
                            print("Le nombre de la machine est bien trop grand")
                            
                        if nb_r2 == nb_r1 :
                            print("C'est gagné !!")
   
                        print("il reste ",tentative, " tentatives")    

                        
                    if nb_r1 == nb_r2:
                        print("La machine 2 a remporté la partie")
                        score_rob2[indice] = score_rob2[indice] + 1
                    else :
                        print("La machine 1 a remporté la partie ")
                        score_rob1[indice] = score_rob1[indice] + 1
                        
                    rejouer = str(input("Voulez vous rejouer ? (oui/non) : "))
                    
                    if rejouer != "oui" :
                        break                  
        
    indice = 0                     
    print("le score du joueur 1 :", score_jou1[indice])
    print("le score du joueur 2 :", score_jou2[indice])
    print("le score du robot 1 :", score_rob1[indice])
    print("le score du robot 2 :", score_rob2[indice])
    
    return score_jou1, score_jou2, score_rob1, score_rob2
