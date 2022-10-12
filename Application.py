import Program as p

def choixRequete():
 
    print("")
    print("1 : Influence de la luminosité sur la gravité d’un accident")
    print("2 : Quelle est la cause principale d’accident de nuit ou de jour peu éclairées")
    print("3 : Les types de déplacement les plus impliqués en fonction du moment de la journée")
    print("4 : Taux d’accident selon de jour ou de nuit entre 1984 et 1997")
    
    choix = int(input(" quelle requête voulez-vous exécuter : "))
    
    print("")
    
    if choix == 1:
        p.gravite()
         
    if choix == 2:
        p.cause()
            
            
    if choix == 3:
        p.implication()
            
    if choix == 4:
        p.date()


choixRequete()
