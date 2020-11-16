#!/usr/bin/env python3
import sys, re
regex = re.compile('[^a-zA-Z]')


# input comes from STDIN
for line in sys.stdin:
    Nom = "1"
    TelephoneUser = "1"
    TelephoneCalls = "1"
    Duree = 0
    City = "Paris"

    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    words = line.split(",")
    
    if len(words) == 5:
        if words[4]== City:
            Nom = words[0]
            TelephoneUser = words[2]
    else :
        TelephoneCalls = words[0]
        Duree = words[2]

    print('%s;%s;%s;%s' % (Nom, TelephoneUser, TelephoneCalls, Duree))


   