#!/usr/bin/python3

import psycopg2 as psql
from MenuHandler import MenuHandler, UnknownMenu, QuitMenu
from admin_menu import open_admin_menu
from utilisateur_menu import open_user_menu, open_default_user_menu

# A modifier pour votre propre configuration 
HOST = "tuxa.sme.utc"
USER = "nf18p090"
DB = "dbnf18p090"
PWD = "ZlEDjy6c0wV4"

# HOST = "localhost"
# USER = "postgres"
# DB = "nf18_projet"
# PWD = ""

if __name__ == "__main__":
	conn = psql.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DB, USER, PWD))

	m = MenuHandler()

	# Ajouter les options pour les différents types d'utilisateurs ici
	m.addMenuOption("Utilisateur non connecté", open_default_user_menu, conn)
	m.addMenuOption("Connexion", open_user_menu, conn)
	m.addMenuOption("Admin", open_admin_menu, conn)
	m.addQuitOption("Quitter l'application")

	m.handle()

	print("Au revoir, et à bientôt sur les lignes.")

	conn.close()
