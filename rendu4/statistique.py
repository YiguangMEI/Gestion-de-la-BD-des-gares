#!/usr/bin/python3

import psycopg2 as psql
from MenuHandler import MenuHandler, UnknownMenu, QuitMenu

def taux_remplissage(conn) :
    cur = conn.cursor()
    print("Voici les voyages : ")
    print("| id | heure de depart | train  | ligne")
    print("-----------------------------------------------------------------------------")

    request  = "SELECT * FROM voyage order BY id_Voyage DESC"
    cur.execute(request)
    res = cur.fetchall()

    for col in res:
        print(" %s | %s | %s | %s " % (col[0], col[1], col[2], col[3]))

    print("-----------------------------------------------------------------------------")
    voyage=input("Quelle est l'identifiant du voyage dont vous voulez des statistiques ?")
    date=input("Pour quelle jour veux-tu voir les statistiques : (formalisme(AAAA-MM-JJ)")
    request = """SELECT count(*) as nombre_place_occupe,
    tp.nbPlace as nombre_place_disponible,
    tp.nbPlace-count(*) as place_disponible
    FROM trajet t
    INNER JOIN voyage v ON t.voyage=v.id_voyage
    INNER JOIN ligne l ON v.ligne=l.numero
    INNER JOIN TypeTrain tp ON l.type_train_autorise=tp.nom
    WHERE t.voyage=%s and t.date=%s
    GROUP BY (tp.nbPlace)"""
    cur.execute(request, (voyage, date))
    res = cur.fetchall()
    if res[0] is None :
        print("pas de voyage programmé ce jour là")
    else :
        placedispo=res[0][2]
        print(type(placedispo))
        placeprise=res[0][0]
        print(type(placeprise))
        placedebase=res[0][1]
        print(type(placedebase))
        taux_remplissage=placeprise/placedebase
        print(type(taux_remplissage))
        print("nb place intitialement | nb places achetés | nb places restantes | taux remplissagee")
        print(placedebase,"      |        ",placeprise,"     |      ",placedispo,"     |     ",taux_remplissage)
    
#je finis demain

def menu_statistique(conn) :
    print("A quelle type de statistique voulez-vous avoir accès")

    menu = MenuHandler()

    menu.addMenuOption("Taux de remplissage d'un voyage", taux_remplissage, conn)
    menu.addQuitOption("Retour")

    menu.handle()
