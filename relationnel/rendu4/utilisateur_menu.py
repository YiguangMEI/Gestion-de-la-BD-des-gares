#!/usr/bin/python3

import psycopg2 as psql
from MenuHandler import MenuHandler, UnknownMenu, QuitMenu
from tabulate import tabulate

# -----------------------
#  Utilisateur connecté
# -----------------------

id_utilisateur = None

def inscription(conn):
	global id_utilisateur

	cur = conn.cursor()
	request="SELECT idVoyageur,numeroCarte FROM voyageur"
	cur.execute(request)
	resu = cur.fetchall()
	max = 0
	maxR =0
	for col in resu:
		if max<col[0] :
			max=col[0]# on en profite pour conserver le plus grand ID, comme ça l'ID du nouveau patient sera max +1
		if col[1] is None :
			boucle=1
		else :
			if maxR<col[1] :
				maxR=col[1]

	nom = input("Quel est votre nom ? : ")
	prenom = input("Quel est votre prénom ? : ")

	print("remplir les informations suivantes sur votre adresse \n")
	numeroVoie = input("Quel est votre numéro de voie ? : ")
	rue = (input("Quelle est votre nom de rue/boulevard/impasse  ? : "))
	codePostal = (input("Quelle est le code postal ? : "))
	tel=input("Rentrez votre numéro de téléphone : ")

	regulier="jsp"
	while (regulier!="oui" and regulier!="non"):
		regulier=input("Voulez vous avoir une carte de voyageur régulier ? (oui/non) \n")
	
	if regulier=="oui" :
		print("vous démarrerez avec le statut Bronze ! \n")
		request  = "INSERT INTO voyageur(idVoyageur,nom,prenom,numeroVoie,nomRue,codePostal,tel,numerocarte,statut) VALUES (%s, %s,%s,%s,%s,%s,%s, %s,%s)"
		cur.execute(request, (str(max+1),nom,prenom,numeroVoie,rue,codePostal,tel,str(maxR+1),'Bronze'))
		conn.commit()
		id_utilisateur = max+1
	else :
		request  = "INSERT INTO voyageur(idVoyageur,nom,prenom,numeroVoie,nomRue,codePostal,tel) VALUES (%s, %s,%s,%s,%s,%s,%s)"
		cur.execute(request, (str(max+1),nom,prenom,numeroVoie,rue,codePostal,tel))
		conn.commit()
		id_utilisateur = max+1

def connexion(conn):
	global id_utilisateur

	connecte = id_utilisateur is not None

	if not connecte:
		print("Veuillez vous connecter pour accéder a vos données.")

	while not connecte:
		print("Quel est votre numéro de téléphone ?")
		print("Ne rien mettre pour créer un nouvel utilisateur.")
		print("Mettre 0 pour revenir au menu précédent.")
		print("> ", end="")

		inUser = input()

		if inUser == '':
			inscription(conn)
			connecte = id_utilisateur is not None
		if inUser == '0':
			break
		else:
			cur = conn.cursor()

			req = "select idVoyageur, nom, prenom from Voyageur where tel='%s'" % inUser

			cur.execute(req)

			nb_lignes = cur.rowcount

			if nb_lignes > 0:
				user = cur.fetchone()
				id_utilisateur = int(user[0])
				connecte = True
				print(f"\nConnecté ! Bonjour {user[2]} {user[1]}")
			else:
				print(f"Numéro de téléphone {inUser} inconnu; voulez-vous vous inscrire ? (0->non, 1->oui)")
				
				print("> ", end="")

				choix = int(input())

				if choix == 1:
					inscription(conn)
					connecte = id_utilisateur is not None
				else:
					print("Connexion")

	return connecte

def deconnexion():
	global id_utilisateur
	id_utilisateur = None


def consultation_billets(conn):
	global id_utilisateur

	if id_utilisateur is not None:

		cur = conn.cursor()

		data = {}

		# ------
		# Récupère dans un premier temps les informations sur le départ des trajets de l'utilisateur

		req_dep = """
			select idBillet, assurance, numeroTrajet, numeroPlace, t.heureDepart, t.date, t.prix, vd.villeGare, vd.nomGare
			from billet 
			join trajet t on billet.idBillet = t.billet
			join voyageDessert vd on t.voyage = vd.voyage
			where acheteur = %i and t.heureDepart = vd.heureDepart
			order by idBillet, numeroTrajet
		""" % id_utilisateur

		cur.execute(req_dep)

		nb_lignes = cur.rowcount

		if nb_lignes == 0:
			print("Vous n'avez réservé aucun billet.")
			return

		for cursor in cur:
			if cursor[0] not in data:
				data[cursor[0]] = {
				"assure": cursor[1],
				"sousTrajets" : [],
				"prixTot" : 0.0,
				"depart": [cursor[5], cursor[4], cursor[7], cursor[8]] # [date, heure, ville, gare]
				}
			data[cursor[0]]["prixTot"] += float(cursor[6])
			data[cursor[0]]["sousTrajets"].append([cursor[3], cursor[5], cursor[4], cursor[7], cursor[8]]) # [nplace, dateDep, heureDep, villeDep, gareDep]

		# ------
		# Récupère dans un deuxième temps les informations sur l'arrivée des trajets de l'utilisateur

		req_arr = """
			select idBillet, numeroTrajet, t.date, t.heureArrivee, vd.villeGare, vd.nomGare
			from billet 
			join trajet t on billet.idBillet = t.billet
			join voyageDessert vd on t.voyage = vd.voyage
			where acheteur = %i and t.heureArrivee = vd.heureArrivee
			order by idBillet, numeroTrajet desc
		""" % id_utilisateur

		cur.execute(req_arr)

		nb_lignes = cur.rowcount

		for cursor in cur:
			if "arrivee" not in data[cursor[0]]:
				data[cursor[0]]["arrivee"] = [cursor[2], cursor[3], cursor[4], cursor[5]] # [date, heure, ville, gare]
			data[cursor[0]]["sousTrajets"][int(cursor[1])] += [cursor[2], cursor[3], cursor[4], cursor[5]] # [dateArr, heureArr, villeArr, gareArr]

		# ------
		# Avec toutes les infos récoltées sur les départs et les arrivées, on peut rendre quelque chose à l'écran

		from pprint import pprint
		pprint(data)

		print("Réservations : ")
		for billet in data:
			info = data[billet]
			print("------")
			print(tabulate([[billet, info["depart"][0], f"{info['depart'][3]}[{info['depart'][2]}]", f"{info['arrivee'][3]}[{info['arrivee'][2]}]", info["assure"], info["prixTot"]]], headers=["Billet", "Date", "Départ", "Arrivée", "Assuré", "Prix"], tablefmt="plain"))
			
			print("\t ------ Détails ------ ")
			for sousTrajetIdx, sousTrajet in enumerate(info["sousTrajets"]):
				print(f"\t {sousTrajetIdx} : ", end="")
				print(f"Le {sousTrajet[1]}({sousTrajet[2]}) à ", end="")
				print(f"{sousTrajet[3]}({sousTrajet[4]}) -> {sousTrajet[7]}({sousTrajet[8]}) ", end="")
				print(f"le {sousTrajet[5]}({sousTrajet[6]}) | ", end="")
				print(f"Place : {sousTrajet[0]}")

			print()

def reserver_trajet(conn, data, voyage_id):
	global id_utilisateur

	cur = conn.cursor()

	print(f"Réservation du voyage {voyage_id}")

	if connexion(conn):

		# Récupération des données nécessaires

		## -- Info générales
		prix = data[-1]

		heureSplit = data[2].split(":")
		heureDep = f"{heureSplit[0]}:{heureSplit[1]}:00"

		heureSplit = data[4].split(":")
		heureArr = f"{heureSplit[0]}:{heureSplit[1]}:00"

		date = data[5]

		## -- Assurance
		assurance = False
		print("Voulez-vous assurer votre voyage (+5%) ? (0 -> non | 1 -> oui)")
		print("> ", end="")
		choix = input()

		if choix != '0':
			prix += 0.05 * prix
			assurance = True

		## -- Paiement
		moyenPaiement = None
		print("Comment voulez-vous payer le billet ?")
		req = "select intitule from typePaiment"
		cur.execute(req)

		info_paiment = []

		for idx, typep in enumerate(cur):
			info_paiment.append(typep)
			print(f"{idx} - {typep}")

		while moyenPaiement is None:
			print("> ", end="")

			try:
				choix = int(input())
				if choix >= 0 and choix < len(info_paiment):
					moyenPaiement = info_paiment[choix]
				else:
					print("La valeur donnée n'est pas correcte.")
			except ValueError:
				print("La valeur donnée n'est pas un nombre entier.")

		## -- génération du numéro de la place
		numero_place = 1
		req = "select numeroPlace from trajet where voyage = %i" % (voyage_id)
		cur.execute(req)
		places = []
		for cursor in cur:
			places.append(int(cursor[0]))

		while numero_place in places:
			numero_place += 1

		## -- Génération du numéro de billet
		id_billet = 1
		req = "select idBillet from billet"
		cur.execute(req)
		billets = []
		for cursor in cur:
			billets.append(int(cursor[0]))

		while id_billet in billets:
			id_billet += 1

		# Création du billet associé

		cmd = "insert into billet values (%s, %s, %s, %s)"
		cur.execute(cmd, (id_billet, assurance, int(id_utilisateur), moyenPaiement,))

		# Création du trajet
		cmd = "insert into trajet values (%s, 0, %s, %s, %s, %s, %s, %s)"
		cur.execute(cmd, (id_billet, numero_place, voyage_id, prix, heureDep, heureArr, date,))

		# Validation des modification
		conn.commit()

	return True

def gen_user_menu(conn, start_idx=0):
	menu = MenuHandler(start_idx)

	menu.addMenuOption("Réserver", recherche_trajet, conn)
	menu.addMenuOption("Consulter les réservations", consultation_billets, conn)
	# menu.addMenuOption("Modifier les réservations", modifier_reservation, conn)
	# menu.addMenuOption("Annuler les réservations", annuler_reservation, conn)
	menu.addQuitOption("Déconnexion")

	return menu

def open_user_menu(conn, start_idx=0):
	global id_utilisateur

	connexion(conn)

	if id_utilisateur is not None:

		menu = gen_user_menu(conn, start_idx)

		menu.handle()

		deconnexion()

# --------------------------
#  Utilisateur non connecté
# --------------------------


def reserver(conn, data, voyages_id):
	print(" ---- ")
	print("Souhaitez-vous réserver l'un de ces voyages ?")
	print("Entrez la valeur du champ 'Idx' pour choisir un voyage ou q pour quitter")

	active = True
	while active:
		print("> ", end="")

		choix = input()

		if choix != 'q':
			try:
				voyage_id = int(choix)

				if voyage_id >= 0 and voyage_id < len(data):
					active = not reserver_trajet(conn, data[voyage_id], voyages_id[voyage_id])
				else:
					print("L'indice donné ne correspond pas à un voyage proposé.")
			except ValueError as ex:
				print("La valeur entrée n'est pas un entier.")
				print(ex)
		else:
			active = False

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
	nom_champs = ["*Ville de depart", "*Ville d'arrivee", "*Date de depart (aaaa-mm-jj)", "Prix minumum", "Prix maximum"]
	champs = [None] * len(nom_champs)

	print("Rechercher les trajets")

	active = True
	while active:
		print("Rentrez la valeur q pour quitter ce menu.")
		for idx_champ, nom_champ in enumerate(nom_champs):
			print(f"{idx_champ} - {nom_champ}[{'' if champs[idx_champ] is None else champs[idx_champ]}]")
		if champs[0] is not None and champs[1] is not None and champs[2] is not None:
			print(f"{len(champs)} - Rechercher")

		print("> ", end="")

		choix = input()

		try:
			choix = int(choix)

			if choix >= 0 and choix <= len(champs) :
				if choix == len(champs) and (champs[0] is None or champs[1] is None or champs[2] is None):
					print("Il n'est pas possible de rechercher un trajet tant que le départ, la destination et la date ne sont pas renseignes")
					continue
				if choix == len(champs):
					active = False
					continue

				print(f"Entrez la donnée : {nom_champs[choix]}")
				print("> ", end="")

				champs[choix] = input()

		except ValueError:
			if choix == "q":
				return
			else:
				print("Entree utilisateur n'est pas un nombre entier")

	print("---------")

	cur = conn.cursor()

	req = """
		SELECT vg.nomGare, vd.nomGare, vg.heureDepart, vd.heurearrivee, p.dateDepart, p.dateFin, vg.voyage
		FROM voyageDessert vg
		INNER JOIN voyageDessert vd ON vg.voyage=vd.voyage
		INNER JOIN VoyagePlannifie vp ON vg.voyage=vp.voyage
		INNER JOIN Plannification p ON vp.plannification=p.idPlanification
		INNER JOIN ExceptionPlannification ep  ON ep.plannification=p.idPlanification
		INNER JOIN JourException je ON ep.jour =je.jour
		WHERE vg.villeGare='%s' AND vd.villeGare='%s' AND vg.heureDepart is not NULL and vd.heureArrivee is not NULL """ % (champs[0], champs[1])

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
		voyages_id = []
		times = []
		for idx, cursor in enumerate(cur):
			data.append([
				idx,
				f"{champs[0]}[{cursor[0]}]", 
				f"{cursor[2].hour}:{cursor[2].minute}",
				f"{champs[0]}[{cursor[1]}]", 
				f"{cursor[3].hour}:{cursor[3].minute}",
				f"{champs[2]}"
				])
			voyages_id.append(cursor[6])
			times.append(cursor[3].hour - cursor[2].hour)
	
		req = """
			select v.id_voyage, tt.coutheure
			from voyage v 
			join train t on v.train = t.numero
			join typetrain tt on t.type = tt.nom
		"""

		cur.execute(req)

		for cursor in cur:
			for data_idx in range(len(data)):
				if voyages_id[data_idx] == cursor[0]:
					data[data_idx] += [float(cursor[1]) * times[data_idx]]

		print("\n", tabulate(data, headers=["Idx", "Depart", "Heure depart", "Arrivee", "Heure arrivee", "Jour", "Prix"]), "\n")

		reserver(conn, data, voyages_id)

	else:
		print(f"\nPas de trajets pour les infos suivantes :.\n")
		for idx_champ, nom_champ in enumerate(nom_champs):
			print(f"{idx_champ} - {nom_champ}[{'' if champs[idx_champ] is None else champs[idx_champ]}]")

def gen_defaut_user_menu(conn, start_idx):
	menu = MenuHandler(start_idx)

	menu.addMenuOption("Consulter les horaires des trains", consultation_horaire_train, conn)
	menu.addMenuOption("Chercher des trajets", recherche_trajet, conn)
	menu.addQuitOption("Retour")

	return menu

def open_default_user_menu(conn, start_idx=0):
	menu = gen_defaut_user_menu(conn, start_idx)

	menu.handle()

