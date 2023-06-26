#!/usr/bin/python3

import psycopg2 as psql
from MenuHandler import MenuHandler, UnknownMenu, QuitMenu

def afficher_lignes(conn):
	cur = conn.cursor()

	#Rappel des lignes dÃ©jÃ  prÃ©sentes : toujours utiles pour que l'on n'essaye pas d'ajouter une gare qui existe dÃ©jÃ
	print("Voici les lignes : ")
	print("| Numero | type de train")
	request = "SELECT * FROM ligne"#rajouter un order BY
	cur.execute(request)
	res = cur.fetchall()

	for col in res:
		print(" %s | %s " % (col[0], col[1]))

	print("-----------------------------------------------------------------------------")
	print()

def nouvelle_ligne(conn) :
	afficher_lignes(conn)
	cur = conn.cursor()
	
	print("Ajouter les informations concernant la ligne à  ajouter :")
	numero = input("Quelle est le numero de la ligne ? : ")
	request="SELECT nom FROM TypeTrain"
	cur.execute(request)
	res=cur.fetchall()
	print("Voici tous les types de train:")
	for col in res:
		print("%s " % col[0])
	typeTrain = input("choisir un type de train de saisir: ")

	# ajout de la ligne
	request = "INSERT INTO Ligne VALUES (%i, '%s');" % (int(numero), typeTrain)
	cur.execute(request)
	conn.commit()

#supprimer une ligne
def supprimer_ligne(conn):
	afficher_lignes(conn)
	cur = conn.cursor()

	print("ATTENTION!!!!!!")
	numero = input("\n Quelle est le numero de la ligne qui doit être supprimer ?")
	request = "DELETE FROM Ligne WHERE numero = %i" % (int(numero))
	cur.execute(request)
	conn.commit()
	print("Supprimé avec succès!")

def ligne_dessert(conn) :
	cur = conn.cursor()
	numero=int(input("Quelle est le numéro de la ligne auquel vous voulez lier une gare ?"))
	request = "SELECT nomGare,villeGare,ordre FROM ligneDessert ld WHERE ld.ligne=%i" %numero
	cur.execute(request)
	resu = cur.fetchall()
	print("Voici toutes les gares déjà liée à cette ligne")
	print("nom de la gare | ville | ordre de passage")
	print("-----------------------------------------------------------------------------")
	max=0
	for col in resu:
		max+=1 #on en profite pour conserver le plus grand ordre de passage
		print("%s | %s | %s" %(col[0],col[1],col[2]))
	print("-----------------------------------------------------------------------------")
	print()
	request  = "SELECT * FROM gare"
	cur.execute(request)
	res = cur.fetchall()
	print("Et voici toutes les gares ")

	for col in res:
		print(" %s | %s | %s | %s | %s | %s " % (col[0], col[1], col[2], col[3], col[4], col[5]))

	print("-----------------------------------------------------------------------------")
	print()


	gare=str(input("Quelle est le nom de la gare à lier avec la ligne ?"))
	ville=str(input("Quelle est le nom de la ville où se situer la gare à lier avec la ligne ?"))
	ordre=(input("Quelle est son ordre de passage ?"))
	if int(ordre)<=max+1 :
	    request = "INSERT INTO ligneDessert VALUES (%s,%s,%s,%s)"
	    cur.execute(request, (gare, ville, numero, ordre))
	    conn.commit()
	else :
		print("L'ordre voulue n'est pas possible")

def gestion_lignes(conn):
	menu = MenuHandler()

	menu.addMenuOption("Ajout d'une ligne", nouvelle_ligne, conn)
	menu.addMenuOption("Ajout d'une desserte de la ligne", ligne_dessert, conn)
	# menu.addMenuOption("Modification d'une ligne", modifier_ligne, conn)
	menu.addMenuOption("Suppresion d'une ligne", supprimer_ligne, conn)
	menu.addQuitOption("Retour")

	menu.handle()
