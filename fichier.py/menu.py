from fonction_mor import morpions
from fonction_allu import allumettes
from fonction_dev import devinettes
from fonction_puiss import puissance
from fonction_tri import tri_bulle

if __name__ == "__main__" :
    """
    #-------------------------------------------------------------------------------------
    Fonction : fonction morpions, fonction allumettes, fonction devinettes et fonction
    puissance 4
    Programme qui va faire office de menu afin d'accéder aux différents jeux comme le 
    morpion, la devinette, les allumettes ou bien le puissance quatre.
    #-------------------------------------------------------------------------------------
    """
    
    saisi : int
    jouer : int
    type : int              #entier pour déterminer si le joueur veut jouer contre une machine ou non
    liste : list[int]       #liste du joueur gagnant avec les scores de manière croissante
    liste_nom : list[str]   #liste qui regroupe le nom des jeux Devinette, Allumettes, Morpion puis Puissance 4
    score_jou1 : list[int]  #liste des scores des différents jeux pour le joueur 1
    score_jou2 : list[int]  #même joueur 2
    score_rob1 : list[int]  #même robot 1
    score_rob2 : list[int]  #même robot 2
    list_final : list[int]  #liste qui va contenir le score total de chaque joueur en commençant par le joueur 1 puis 2 puis les robots
    indice : int            #indice pour déterminer le jeux, 0 pour devinette puis allumettes, puis morpion et puissance 4
    
    jouer = 1
    indice = 0
    liste = [0, 0, 0, 0]
    score_jou1 = [0, 0, 0, 0]
    score_jou2 = [0, 0, 0, 0]
    score_rob1 = [0, 0, 0, 0]
    score_rob2 = [0, 0, 0, 0]
    list_final = [0, 0, 0, 0]
    liste_nom = ["Devinette", "Allumette", "Morpion", "Puissance 4"]
    score1_final = 0
    score2_final = 0
    type = 0
    
    print("\nMenu")
    
    #permet de savoir si l'utilisateur veut encore jouer ou non, on part du principe que l'utilisateur joue à au moins un jeu 
    while jouer == 1 :
        score1 = 0
        score2 = 0
        
        print("\n- Taper 1 pour jouer au Devinette")
        print("- Taper 2 pour jouer à l'Allumettes")
        print("- Taper 3 pour jouer au Morpion")
        print("- Taper 4 pour jouer au Puissance Quatre")
        saisi = int(input("Votre saisi :"))

        #condition pour les choix des jeux, soit 1, 2, 3 ou 4
        while (saisi != 1) and (saisi != 2) and (saisi != 3) and (saisi != 4):
            print("\n" * 50, "Votre saisi est fausse")
            print("- Taper 1 pour jouer au Devinette")
            print("- Taper 2 pour jouer à l'Allumettes")
            print("- Taper 3 pour jouer au Morpion")
            print("- Taper 4 pour jouer au Puissance Quatre")
            saisi = int(input("Votre saisi :"))
        
        #choix entre un joueur ou une machine, 1 pour une machine et 2 pour un joueur et 3 pour machine/machine
        print("\n- Veuillez saisir 1 pour jouer contre une machine")
        print("\n- Veuillez saisir 2 pour jouer contre un autre joueur")
        print("\n- Veuillez saisir 3 pour voir un match entre machine")
        type = int(input("Votre choix :"))
        
        #condition pour que le choix soit bien entre le chiffre 1, 2 ou 3
        while (type != 1) and (type != 2) and (type != 3) :
            print("\n" * 50, "Votre saisi est fausse")
            print("\n- Veuillez saisir 1 pour jouer contre une machine")
            print("\n- Veuillez saisir 2 pour jouer contre un autre joueur")
            print("\n- Veuillez saisir 3 pour voir un match entre machine")
            type = int(input("Votre choix :"))
        
        #choix des jeux avec 
        if saisi == 1 :
            indice = 0
            score_jou1, score_jou2, score_rob1, score_rob2 = devinettes(score_jou1, score_jou2, score_rob1, score_rob2, indice, type)
        else :
            if saisi == 2 :
                indice = 1
                score_jou1, score_jou2, score_rob1, score_rob2 = allumettes(score_jou1, score_jou2, score_rob1, score_rob2, indice, type)
            else :
                if saisi == 3 :
                    indice = 2
                    score_jou1, score_jou2, score_rob1, score_rob2 = morpions(score_jou1, score_jou2, score_rob1, score_rob2, indice, type)
                else : 
                    if saisi == 4 :
                        indice = 3                 
                        score_jou1, score_jou2, score_rob1, score_rob2 = puissance(score_jou1, score_jou2, score_rob1, score_rob2, indice, type)
        
        #score final
        list_final[0] = score_jou1[0] + score_jou1[1] + score_jou1[2] + score_jou1[3]
        list_final[1] = score_jou2[0] + score_jou2[1] + score_jou2[2] + score_jou2[3]
        list_final[2] = score_rob1[0] + score_rob1[1] + score_rob1[2] + score_rob1[3]
        list_final[3] = score_rob2[0] + score_rob2[1] + score_rob2[2] + score_rob2[3]
        
        print("\n" * 3, "Taper 1 pour si vous voulez continuer à jouer")
        print("Taper 2 pour si vous ne voulez plus jouer")
        jouer = int(input("Votre saisi :"))
    
        #condition l'utilisateur doit taper 1 ou 2, 1 s'il veut continuer à jouer et 2 s'il veut arrêter 
        while (jouer != 1) and (jouer != 2) :
            print("\n" * 50, "Votre saisi est fausse")
            print("Taper 1 pour si vous voulez jouer")
            print("Taper 2 pour si vous ne voulez plus jouer")
            jouer = int(input("Votre saisi :"))
     
    #tri de la liste finale afin de trouver celui qui est le meilleur
    indice = 0
    for i in range(0, 3) :
        if (list_final[indice] < list_final [i + 1]) :
            indice = i + 1
    
    #attribution de la liste du gagnant en fonction de l'indice
    #puis affichage de score du joueur ou machine gagnant en fonction de chaque jeux de façon croissante
    if (indice == 0) :
        for i in range(0, 4) :
            liste[i] = score_jou1[i]
        liste, liste_nom = tri_bulle(liste, liste_nom)
        print("\nLe classement du joueur 1")
        print("\n" * 3, "classement", 4,":", liste_nom[0], ":", liste[0])
        print("classement", 3,":", liste_nom[1], ":", liste[1])
        print("classement", 2,":", liste_nom[2], ":", liste[2])
        print("classement", 1,":", liste_nom[3], ":", liste[3])
    else :
        if (indice == 1) :
            for i in range(0, 4) :
                liste[i] = score_jou2[i]
            liste, liste_nom = tri_bulle(liste, liste_nom)
            print("\nLe classement du joueur 2")
            print("\n" * 3, "classement", 4,":", liste_nom[0], ":", liste[0])
            print("classement", 3,":", liste_nom[1], ":", liste[1])
            print("classement", 2,":", liste_nom[2], ":", liste[2])
            print("classement", 1,":", liste_nom[3], ":", liste[3])
        else : 
            if (indice == 2) :
                for i in range(0, 4) :
                    liste[i] = score_rob1[i]
                liste, liste_nom = tri_bulle(liste, liste_nom)
                print("\nLe classement de la machine 1")
                print("\n" * 3, "classement", 4,":", liste_nom[0], ":", liste[0])
                print("classement", 3,":", liste_nom[1], ":", liste[1])
                print("classement", 2,":", liste_nom[2], ":", liste[2])
                print("classement", 1,":", liste_nom[3], ":", liste[3])
            else :
                for i in range(0, 4) :
                    liste[i] = score_rob2[i]
                liste, liste_nom = tri_bulle(liste, liste_nom)
                print("\nLe classement de la machine 2")
                print("\n" * 3, "classement", 4,":", liste_nom[0], ":", liste[0])
                print("classement", 3,":", liste_nom[1], ":", liste[1])
                print("classement", 2,":", liste_nom[2], ":", liste[2])
                print("classement", 1,":", liste_nom[3], ":", liste[3])
    
