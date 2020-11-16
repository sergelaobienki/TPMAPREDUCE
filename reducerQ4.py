#!/usr/bin/env python3

import sys, re
regex = re.compile('[^a-zA-Z]')
from collections import defaultdict

current_Nom = None
TelephoneUser = None
Duree = None
#Dictionnaire d'utilisateur
user = defaultdict(list)

# input comes from STDIN
for line in sys.stdin:
    CallTotale = 0
    # remove  and trailing whitespace
    line = line.strip()
    Nom,Duree,Nombre_Appel = line.split("/")
    print('%s %s' %(Nom,int(Duree)/int(Nombre_Appel) ))

    