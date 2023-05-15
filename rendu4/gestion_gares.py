#!/usr/bin/python3

import psycopg2 as psql
from MenuHandler import MenuHandler, UnknownMenu, QuitMenu

def afficher_gares(conn):
	cur = conn.cursor()

	#Rappel des gares dÃ©jÃ  prÃ©sentes : toujours utiles pour que l'on n'essaye pas d'ajouter une gare qui existe dÃ©jÃ
	print("Voici les gares : ")
	print("| Nom | Ville | Numero  | Rue | Code postal | zone horraire (GMT]")
	request  = "SELECT * FROM gare"#rajouter un order BY
	cur.execute(request)
	res = cur.fetchall()

	for col in res:
		print(" %s | %s | %s | %s | %s | %s " % (col[0], col[1], col[2], col[3], col[4], col[5]))

	print("-----------------------------------------------------------------------------")
	print()


def nouvelle_gare(conn):
	afficher_gares(conn)

	cur = conn.cursor()
	print("Ajouter les informations concernant la gare à  ajouter :")
	nom = (input("Quelle est le nom de la gare ? : "))
	ville = (input("Quel est le nom de la ville ? : "))
	numero = (input("Quelle est le numÃ©ro (de voie) de la gare ? : "))
	rue = (input("Quelle est le nom de rue/boulevard/impasse de la gare ? : "))
	codePostal = (input("Quelle est le code postal de la gare ? : "))
	Zonehorraire = input("Quelle est la zone horaire de la gare (GMT) ? : ")

	# ajout de la ligne
	request = "INSERT INTO gare VALUES (%s, %s, %s, %s, %s,%s);"
	cur.execute(request, (nom, ville, numero, rue, codePostal, Zonehorraire))
	conn.commit()

def modifier_gare(conn):
	afficher_gares(conn)

	cur = conn.cursor()
	nom=input("quelle est le nom de la gare dont l'adresse doit être modifier ?")
	ville=input("quelle est le nom de la ville où se situe la gare ?")
	numero = (input("Quelle est le nouveau numéro (de voie) de la gare ? : "))
	rue = (input("Quelle est le nouveau nom de rue/boulevard/impasse de la gare ? : "))
	codePostal = (input("Quelle est le nouveau code postal de la gare ? : "))
	request="UPDATE GARE SET numeroVoie=%s, nomRue='%s',codePostal=%s WHERE nom='%s' AND ville='%s' " %(numero, rue, codePostal, nom, ville)
	cur.execute(request)
	conn.commit()

def supprimer_gare(conn):
	afficher_gares(conn)

	cur = conn.cursor()
	print("ATTENTION : il ne sera pas possible de supprimer une gare qui sont censé encore être désservie par des ")
	nom=input("\n Quelle est le nom de la gare qui doit être supprimer ?")
	ville=input("\n Quelle est le nom de la ville où se situe la gare qui doit être supprimer ?")
	request="DELETE FROM gare WHERE nom='%s' AND ville='%s'" %(nom, ville)
	cur.execute(request)
	conn.commit()

def gestion_gares(conn):
	menu = MenuHandler()

	menu.addMenuOption("Ajout d'une gare", nouvelle_gare, conn)
	menu.addMenuOption("Modification d'une gare", modifier_gare, conn)
	menu.addMenuOption("Suppresion d'une gare", supprimer_gare, conn)
	menu.addQuitOption("Retour")

	menu.handle()
