#!/usr/bin/python3

import psycopg2 as psql
from MenuHandler import MenuHandler, UnknownMenu, QuitMenu
from tabulate import tabulate

def consultation_horaire_train(conn):
	print("Consulter les horaires des trains :")
	print("- Partant de quelle gare ?", end="\n> ")

	nom_gare = input()

	print("- Dans quelle ville ?", end="\n> ")

	ville_gare = input()

	print("- Quand ? aaaa-mm-jj", end="\n> ")

	date = input()

	cur = conn.cursor()
	req = """
		select vd.heureDepart, v.train
		from VoyageDessert vd join Voyage v on vd.voyage = v.id_Voyage join VoyagePlannifie vp on v.id_Voyage = vp.voyage join plannification p on vp.plannification = p.idPlanification
		where vd.nomGare=%s and vd.villeGare=%s and %s between p.dateDepart and p.dateFin and vd.heureDepart is not null
	"""

	cur.execute(req, (nom_gare,ville_gare, date))

	nb_lignes = cur.rowcount

	if nb_lignes > 0:
		data = []
		for cursor in cur:
			data.append([f"{cursor[0].hour}:{cursor[0].minute}", cursor[1]])
		print("\n", tabulate(data, headers=["Horaire (h:m)", "numero de train"]), "\n")

	else:
		print(f"\nPas d'horaire pour {nom_gare}[{ville_gare}] a partir du {date}.\n")

def recherche_trajet(conn):
	nom_champs = ["*Ville de depart", "*Ville d'arrivee", "Date de depart (aaaa-mm-jj)", "Prix minumum", "Prix maximum"]
	champs = [None] * len(nom_champs)

	print("Rechercher les trajets")

	active = True
	while active:
		for idx_champ, nom_champ in enumerate(nom_champs):
			print(f"{idx_champ} - {nom_champ}[{'' if champs[idx_champ] is None else champs[idx_champ]}]")
		if champs[0] is not None and champs[1] is not None:
			print(f"{len(champs)} - Rechercher")

		print("> ", end="")

		try:
			choix = int(input())

			if choix >= 0 and choix <= len(champs) :
				if choix == len(champs) and (champs[0] is None or champs[1] is None):
					print("Il n'est pas possible de rechercher un trajet tant que le depart et la destination ne sont pas renseignes")
					continue
				if choix == len(champs):
					active = False
					continue

				print(f"Entrez la donnee : {nom_champs[choix]}")
				print("> ", end="")

				champs[choix] = input()

		except ValueError:
			print("Entree utilisateur n'est pas un nombre entier")

	print("---------")

	cur = conn.cursor()

	req = """
		SELECT vg.nomGare, vd.nomGare, vg.heureDepart, vd.heurearrivee, t.prix, p.dateDepart, p.dateFin
		FROM voyageDessert vg
		INNER JOIN voyageDessert vd ON vg.voyage=vd.voyage
		INNER JOIN VoyagePlannifie vp ON vg.voyage=vp.voyage
		INNER JOIN Plannification p ON vp.plannification=p.idPlanification
		INNER JOIN ExceptionPlannification ep  ON ep.plannification=p.idPlanification
		INNER JOIN JourException je ON ep.jour =je.jour
		INNER JOIN trajet t on vg.voyage = t.voyage
		WHERE vg.villeGare='%s' AND vd.villeGare='%s' """ % (champs[0], champs[1])

	if champs[2]:
		req += " AND p.dateDepart<='%s' AND p.dateFin>='%s' AND (p.dimanche=TRUE OR (je.jour='%s' and je.ajout=TRUE)) AND NOT (je.jour='%s' and je.ajout=FALSE)" % (champs[2], champs[2], champs[2], champs[2])

	if champs[3]:
		req += " AND t.prix>=%f" % (float(champs[3]))

	if champs[4]:
		req += " AND t.prix<=%f" % (float(champs[4]))

	cur.execute(req)

	nb_lignes = cur.rowcount

	if nb_lignes > 0:
		data = []
		for cursor in cur:
			data.append([
				f"{champs[0]}[{cursor[0]}]", 
				f"{cursor[2].hour}:{cursor[2].minute}",
				f"{champs[0]}[{cursor[1]}]", 
				f"{cursor[3].hour}:{cursor[3].minute}",
				f">={cursor[5]} et <={cursor[6]}",
				cursor[4]
				])
		print("\n", tabulate(data, headers=["Depart", "Heure depart", "Arrivee", "Heure arrivee", "Jour", "Prix"]), "\n")

	else:
		print(f"\nPas de trajets pour les infos suivantes :.\n")
		for idx_champ, nom_champ in enumerate(nom_champs):
			print(f"{idx_champ} - {nom_champ}[{'' if champs[idx_champ] is None else champs[idx_champ]}]")

def gen_menu(conn, start_idx):
	menu = MenuHandler(start_idx)

	menu.addMenuOption("Consulter les horaires des trains", consultation_horaire_train, conn)
	menu.addMenuOption("Chercher des trajets", recherche_trajet, conn)
	menu.addQuitOption("Retour")

	return menu

def open_default_user_menu(conn, start_idx=0):
	menu = gen_menu(conn, start_idx)

	menu.handle()

