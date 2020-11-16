# TPMAPREDUCE


Le but de ce TP est de maitriser la tournure d’esprit pour formuler des requêtes suivant le paradigm map/reduce. Les exemples qui suivent sont illustrés en Python. La maitrise du Python n’est pas nécessaire, les exemples ci-dessous associés aux commentaires sont suffisant pour vous permettent de comprendre et rédiger ce qu’on vous demande. Pour, le rendu, Java ou autre langage est possible.

--------->cat users.txt calls.txt | /Desktop/tpMapReduce2020/mapper.py | sort | /Desktop/tpMapReduce2020/reducer.py > resultat.txt ki@ki-ThinkPad-T440:/YEH/tpMapReduce2020$ chmod +x reducer.py ki@ki-ThinkPad-T440:/YEH/tpMapReduce2020$ chmod +x mapper.py

# Question 4: Traduire la requête suivante en un map/reduce. Moyenne des durées des appels de chaque utilisateur habitant à Paris.

SELECT nom, avg(durée) FROM calls C, users U WHERE C.de= U.tel AND ville='Paris' GROUP BY nom);
