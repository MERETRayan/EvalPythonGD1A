from colorama import Fore, Back, Style

def chercheLettreCorrect(motEcrit,motDevine) :
    i = 0 
    j = 0
    for j in range (0,5):  
        for i in range (0,5):
            if motDevine[j]==motEcrit[i]:
               print (Back.RED+motEcrit[i])

def chercheLettreFause(motEcrit,motDevine) :
    i = 0 
    j = 0
    for j in range (0,5):  
        for i in range (0,5):
            if motDevine[i]!=motEcrit[j]:
               print (Back.BLUE+motEcrit[j])

def chercheLettreMalPlacé(motEcrit,motDevine) :
    i = 0 
    j = 0
    for j in range (0,5):  
        for i in range (0,5):
            if motDevine[j]==motEcrit[i]:
               print (Back.YELLOW+motEcrit[i])

motADeviner=['a','r','b','r','e','s']
motEcris=input("Quel est le mot caché en 6 lettres ?")
print ( motEcris)
print (motADeviner)
