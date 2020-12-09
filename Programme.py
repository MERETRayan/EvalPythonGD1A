from colorama import Fore, Back, Style

def chercheLettreCorrect(motDevine,motEcrit) :
    stockage = 0
    Vrai=False
    Milieu=0
    for j in range (len(motDevine)): 
        i=0 
        while (stockage==0):
            i=i+1
            if (motDevine[j]==motEcrit[i]):
                if (i == j ):        
                    Vrai=True
                    stockage = i 
                else:
                    stockage = i
            else:
                Milieu=1
                stockage = i
        if Vrai==True :
           print (Back.MAGENTA+motEcrit[stockage])
           Vrai=False
        else:
            print (Back.RED+motEcrit[stockage])
        if Milieu == 1 : 
            print (Back.CYAN+motEcrit[stockage])


motADeviner = 'arbres'
motEcrit = input("Quel est le mot caché en 6 lettres ?")
chercheLettreCorrect(motADeviner,motEcrit)
#chercheLettreFause(motEcris,motADeviner)

