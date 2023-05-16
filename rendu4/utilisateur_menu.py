#!/usr/bin/python3

import psycopg2 as psql
from MenuHandler import MenuHandler, UnknownMenu, QuitMenu
from tabulate import tabulate

id_utilisateur = None

def inscription(conn):
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
	
	else :
		request  = "INSERT INTO voyageur(idVoyageur,nom,prenom,numeroVoie,nomRue,codePostal,tel) VALUES (%s, %s,%s,%s,%s,%s,%s)"
		cur.execute(request, (str(max+1),nom,prenom,numeroVoie,rue,codePostal,tel))
		conn.commit()

def connexion(conn):
	global id_utilisateur

	if id_utilisateur is not None:
		return

	connecte = False

	print("Veuillez vous connecter pour accéder a vos données.")

	while not connecte:
		print("Quel est votre numéro de téléphone ?")
		print("Ne rien mettre pour créer un nouvel utilisateur.")
		print("Mettre 0 pour revenir au menu principal.")
		print("> ", end="")

		inUser = input()

		if inUser == '':
			inscription(conn)
			connecte = True
		if inUser == '0':
			return
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
					connecte = True
				else:
					print("Connexion")

def deconnexion():
	global id_utilisateur
	id_utilisateur = None


def consultation_billets(conn):
	global id_utilisateur

	if id_utilisateur is not None:

		cur = conn.cursor()

		data = {}

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
			data[cursor[0]]["sousTrajets"][int(cursor[1])] += [cursor[2], cursor[3], cursor[4], cursor[5]] # [nplace, dateDep, heureDep, villeDep, gareDep]

		from pprint import pprint
		pprint(data)


def gen_menu(conn, start_idx=0):
	menu = MenuHandler(start_idx)

	# menu.addMenuOption("Réserver", reservation_trajet, conn)
	menu.addMenuOption("Consulter les réservations", consultation_billets, conn)
	# menu.addMenuOption("Modifier les réservations", modifier_reservation, conn)
	# menu.addMenuOption("Annuler les réservations", annuler_reservation, conn)
	menu.addQuitOption("Déconnexion")

	return menu

def open_user_menu(conn, start_idx=0):
	global id_utilisateur

	connexion(conn)

	if id_utilisateur is not None:

		menu = gen_menu(conn, start_idx)

		menu.handle()

		deconnexion()
