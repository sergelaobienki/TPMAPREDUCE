#!/usr/bin/env python3

import sys, re
regex = re.compile('[^a-zA-Z]')
from collections import defaultdict

current_Nom = None
TelephoneUser = None
TelephoneCalls = None
Duree = None
#Dictionnaire des Utilisateur
User = {}
# Dictionnaire des appelle de l'utlisateur
call = defaultdict(list)
# input comes from STDIN
for line in sys.stdin:
# remove  and trailing whitespace
    line = line.strip()
    
    try :
        current_Nom,TelephoneUser,TelephoneCalls,Duree = line.split(";")
        if TelephoneUser  != "1":
#Ajout des utilisateur dans le dictionnaire
            User[TelephoneUser] = current_Nom
        elif TelephoneCalls != "1":
#Ajout des valeurs des appelles dans le dic appelle
            call[TelephoneCalls].append(Duree)
    except:
        pass
CallTotale = 0
#Creation de la boucle pour parcourir le dictionnaire des users
for TelUser,NomUser in User.items():
#creation de la boucle pour parcourir le dic des appels
    for telCall,DureeCall in call.items():
#verification des la conformites des numeros et les appels users
        if TelUser == telCall :
#Parcours de la liste pour la recuperation des valeurs
            for i in range(len(DureeCall)):
                CallTotale = CallTotale + int(DureeCall[i])
            print('%s/%s/%s' %(NomUser,CallTotale,len(DureeCall)))
            CallTotale = 0




