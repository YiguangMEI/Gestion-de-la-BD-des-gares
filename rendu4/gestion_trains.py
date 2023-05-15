#!/usr/bin/python3

import psycopg2 as psql
from MenuHandler import MenuHandler, UnknownMenu, QuitMenu

def afficher_trains(conn):
	cur = conn.cursor()
	print("Voici les train : ")
	print("| Numero | Type |")
	request = "SELECT * FROM Train"
	cur.execute(request)
	res = cur.fetchall()
	for col in res :
		print("|   %s    | %s  |"%(col[0],col[1]))
	print("-----------------------------------------------------------------------------")
	print()

def nouveau_train(conn):
	afficher_trains(conn)
	cur = conn.cursor()
	
	print("Ajouter les informations concernant le train à  ajouter :")
	numero = input("enter the numero of the train:")
	typetrain = input("entre the typedetrain(TGV OR TER):")
	while typetrain!="TGV" and typetrain!="TER":
		typetrain = input("entre the typedetrain(TGV OR TER):")

	request = "INSERT INTO Train VALUES (%i, '%s')" % (int(numero),typetrain)
	cur.execute(request)
	conn.commit()

def modifier_train(conn):
	afficher_trains(conn)
	cur = conn.cursor()

	numero = input("quelle est le numero de la train dont la type doit être modifier ?")
	typetrain = input("entre the typedetrain(TGV OR TER):")
	while typetrain!="TGV" and typetrain!="TER":
		typetrain = input("entre the typedetrain(TGV OR TER):")
	request = "UPDATE Train SET type='%s' WHERE numero=%i" % (typetrain,int(numero))
	cur.execute(request)
	conn.commit()

def supprimer_train(conn):
	afficher_trains(conn)
	cur = conn.cursor()

	print("ATTENTION!!!!!!")
	numero=input("\n Quelle est le numero de la train qui doit être supprimer ?")
	request="DELETE FROM Train WHERE numero = %i"%(int(numero))
	cur.execute(request)
	conn.commit()

def gestion_trains(conn):
	menu = MenuHandler()

	menu.addMenuOption("Ajout d'un train", nouveau_train, conn)
	menu.addMenuOption("Modification d'un train", modifier_train, conn)
	menu.addMenuOption("Suppresion d'un train", supprimer_train, conn)
	menu.addQuitOption("Retour")

	menu.handle()
