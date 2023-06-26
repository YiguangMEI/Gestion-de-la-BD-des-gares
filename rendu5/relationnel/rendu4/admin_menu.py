#!/usr/bin/python3

import psycopg2 as psql
from MenuHandler import MenuHandler, UnknownMenu, QuitMenu
from gestion_gares import gestion_gares
from gestion_trains import gestion_trains
from gestion_lignes import gestion_lignes
from gestion_itineraires import gestion_itineraires
from statistique import menu_statistique

def gen_menu(conn, start_idx=0):
	menu = MenuHandler(start_idx)

	menu.addMenuOption("Gestion des gares", gestion_gares, conn)
	menu.addMenuOption("Gestion des lignes", gestion_lignes, conn)
	menu.addMenuOption("Gestion des trains", gestion_trains, conn)
	menu.addMenuOption("Gestion des itineraires", gestion_itineraires, conn)
	menu.addMenuOption("Statistiques", menu_statistique, conn)
	menu.addQuitOption("Retour")

	return menu

def open_admin_menu(conn, start_idx=0):
	menu = gen_menu(conn, start_idx)

	menu.handle()
