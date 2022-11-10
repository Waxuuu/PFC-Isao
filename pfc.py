# DEBUT

#initialiser scoreJoueur a 0 
#initialiser scoreOrdinateur a 0

#definir la fonction Tour

    #si choix joueur est égale à 0
        #si choixOrdinateur egal a 0
            #alors resultat = "egalité"
        #si choixOrdinateur egal a 1 
            #alors resultat = "perdu"
        #si choixOrdinateur = 2
            #alors resultat ="gagnée"

    #si choix joueur est égale à 1
        #si choixOrdinateur egal a 0
            #alors resultat = "gagnée"
        #si choixOrdinateur egal a 1 
            #alors resultat = "egalité"
        #si choixOrdinateur = 2
            #alors resultat ="perdu"

    #si choix joueur est égale à 2
        #si choixOrdinateur egal a 0
            #alors resultat = "perdu"
        #si choixOrdinateur egal a 1 
            #alors resultat = "gagnée"
        #si choixOrdinateur = 2
            #alors resultat ="egalité"

    #retourner resultat
#tant que scoreJoueur et scoreOrdinateur sont inferieur a 3
    #Initialiser choixOrdinateur puis assigner le valeur retourner de random(0,2)
    #Initialiser choixJoueur puis assigner le valeur input( la valeur doit etre, 0,1 ou 2)
    #Initialiser scoreTour puis assigner la valeur retourner de Tour()

    #si choixJoueur egal a 0
        #alors afficher = "le joueur a fait pierre"
    #si choixJoueur egal a 1 
        #alors afficher = "le joueur a fait feuille"
    #si choixOrdinateur egal a 2
        #alors afficher ="le joueur a fait ciseau"

    #si choixOrdinateur egal a 0
        #alors afficher "l'ordinateur a fait pierre"
    #si choixOrdinateur egal a 1 
        #alors afficher "l'ordinateur a fait feuille"
    #si choixOrdinateur a 2
        #alors afficher "l'ordinateur a fait ciseau"

    #si resultatTour est egal a gagnée 
        #alors incrementer scoreJoueur de 1
        #afficher "Tour gagnant"
    #sinon si resultat Tour est egal a perdu
        #alors incrementer scoreOrdinateur de 1
        #afficher "Tour perdant"
    #sinon si resultat Tour est egal a egalité
        #alors incrementer 0
        #afficher "Tour egalité"

    #afficher scoreJoueur et scoreOrdinateur
#afficher scoreTour