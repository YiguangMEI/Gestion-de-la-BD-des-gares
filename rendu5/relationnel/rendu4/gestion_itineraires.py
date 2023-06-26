#!/usr/bin/python3

import psycopg2 as psql
from MenuHandler import MenuHandler, UnknownMenu, QuitMenu

def afficher_voyages(conn):
	cur = conn.cursor()
	print("Voici les voyage : ")
	print("| id_voyage | heuredepart | train | ligne |")
	request = "SELECT * FROM Voyage"
	cur.execute(request)
	res = cur.fetchall()
	for col in res :
		print("|     %s     |   %s  |   %s   |   %s   |"%(col[0],col[1],col[2],col[3]))
	print("-----------------------------------------------------------------------------")
	print()

#ajouter un voyage
def nouveau_voyage(conn):
	afficher_voyages(conn)
	cur = conn.cursor()

	print("Ajouter les informations concernant le voyage à  ajouter :")
	id = int(input("Quelle est le id du voyage? : "))
	heureDepart = input("Quelle est le heureDepart du voyage? : ")
	request = "SELECT numero, type FROM Train"
	cur.execute(request)
	res = cur.fetchall()
	print("Voici tous les trains:")
	for col in res:
		print("%s | %s" % (col[0], col[1]))
	numerotrain = int(input("choisir un numero de train de saisir: "))

	request = "SELECT type FROM Train t WHERE t.numero = %i" %(numerotrain)
	cur.execute(request)
	res = cur.fetchall()
	typetrain=res[0]

	request = "SELECT * FROM Ligne WHERE Ligne.type_train_autorise = '%s'" %(typetrain)
	cur.execute(request)
	res = cur.fetchall()
	print("Voici tous les lignes que vous pouvez choisir:")
	for col in res:
		print("%s | %s" % (col[0], col[1]))
	numeroligne = int(input("choisir un numero de ligne de saisir: "))

	# ajout de le voyage
	request = "INSERT INTO Voyage VALUES (%i, '%s', %i, %i);" % (id, heureDepart, numerotrain, numeroligne)
	cur.execute(request)
	conn.commit()

def modifier_voyage(conn):
	afficher_voyages(conn)
	cur = conn.cursor()

	numero = input("quelle est le numero de la train dont la type doit être modifier ?")
	heure=input("enter the time comme (08:00:00):")
	id_train=input("enter the id_train:")
	id_ligne=input("enter the id_ligen:")
	request = "UPDATE Voyage SET heuredepart='%s',train=%i,ligne=%i WHERE id_voyage=%i" % (heure,id_train,id_ligne,int(numero))
	cur.execute(request)
	conn.commit()

def supprimer_voyage(conn):
	afficher_voyages(conn)
	cur = conn.cursor()

	print("ATTENTION!!!!!!")
	numero = input("\n Quelle est le numero de la Voyage qui doit être supprimer ?")
	request = "DELETE FROM Voyage WHERE id_voyage = %i" % (int(numero))
	cur.execute(request)
	conn.commit()

def voyage_dessert(conn):
	afficher_voyages(conn)
	cur = conn.cursor()

	print("Quelle est l'identifiant de la ligne auquel vous voulez ajouter un arrêt ?")
	id=input()
	request  = "SELECT nomgare,villegare, heureArrivee, heureDepart FROM voyageDessert WHERE voyage=%s" %id
	cur.execute(request)
	res = cur.fetchall()
	print("Voici les informations sur les gares déjà desservies : \n")
	print("Nom de la gare | Ville de la gare | heure entrée en gare | heure départ en gare")
	print("-----------------------------------------------------------------------------")
	garedep=0
	garearr=0
	for col in res :
		print(" %s | %s | %s | %s" % (col[0], col[1], col[2], col[3]))
		if col[2] is None :
			garedep=1
		if col[3] is None :
			garearr=1	
	request  = "SELECT ld.nomgare,ld.villegare FROM LigneDessert ld INNER JOIN voyage v ON v.ligne=ld.ligne WHERE id_voyage=%s EXCEPT SELECT nomgare,villegare FROM voyageDessert WHERE voyage=%s" %(id,id)
	cur.execute(request)
	res = cur.fetchall()
	print()
	print("Voici les gares que vous pouvez desservir en plus : \n")
	print("Nom de la gare | Ville de la gare | ordre de passage")
	print("-----------------------------------------------------------------------------")
	for col in res :
		print(" %s | %s " % (col[0], col[1]))
	print()
	gare=input("Quel est le nom de la Gare qui doit être desservie par le voyage : \n")
	ville=input("Quel est le nom de la ville de la Gare qui doit être desservie par le voyage : \n")
	heureArr=input("Quel est l'heure d'arrivé à cette gare (ATTENTION au formalisme  : HH:MM:SS) : \n")
	heureDep=input("Quel est l'heure de départ de cette gare (ATTENTION au formalisme  : HH:MM:SS) : \n")
	if heureArr=='' :
		print("vous tentez de créer la gare de départ")
		if garedep==0 : #c'est ok, il n'y a pas déjà de gare de départ
			request="SELECT heureDepart FROM voyage WHERE id_voyage=%s" %id
			cur.execute(request)
			res = cur.fetchall()
			if str(res[0][0])==str(heureDep) : #on vérifie que heure de départ du voyage corresponde
				request  = "INSERT INTO voyagedessert(nomgare,villegare,voyage,heuredepart) VALUES (%s,%s,%s,%s)"
				cur.execute(request, (gare, ville,id, heureDep))
				conn.commit()
			else :
				print("Ajout annulé, ne correspond pas avec heure de départ du voyage")
		else :
			print("Ajout annulé, il y a déjà une gare de départ")
	elif heureDep=='' :
		print("vous tentez de créer une gare de terminus")
		if garearr==0 : #c'est ok, il n'y a pas déjà de gare de terminus
			request  = "INSERT INTO voyagedessert(nomgare,villegare,voyage,heurearrivee) VALUES (%s,%s,%s)"
			cur.execute(request, (gare, ville,id,heureArr))
			conn.commit()
		else :
			print("Ajout annulé, il y a déjà une gare de terminus")
	else :
		request  = "INSERT INTO voyagedessert VALUES (%s,%s,%s,%s,%s)"
		cur.execute(request, (gare, ville,id, heureArr, heureDep))
		conn.commit()


def gestion_itineraires(conn):
	menu = MenuHandler()

	menu.addMenuOption("Ajout d'un voyage", nouveau_voyage, conn)
	menu.addMenuOption("Ajout d'une desserte d'un voyage", voyage_dessert, conn)
	menu.addMenuOption("Modification d'un voyage", modifier_voyage, conn)
	menu.addMenuOption("Suppresion d'un voyage", supprimer_voyage, conn)
	menu.addQuitOption("Retour")

	menu.handle()