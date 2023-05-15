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
	tel=input("Rentrez votre numéro de telephone : ")

	regulier="jsp"
	while (regulier!="oui" and regulier!="non"):
		regulier=input("Voulez vous avoir une carte de voyageur régulier ? (oui/non) \n")
	
	if regulier=="oui" :
		print("vous démarerrez avec le statut Bronze ! \n")
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

	print("Veuillez vous connecter pour acceder a vos donnees.")

	while not connecte:
		print("Quel est votre numero de telephone ? (Ne rien mettre pour creer un nouvel utilisateur)")
		print("> ", end="")

		inUser = input()

		if inUser == '':
			inscription(conn)
			connecte = True
		else:
			cur = conn.cursor()

			req = "select idVoyageur, nom, prenom from Voyageur where tel=%s"
			print(req)
			cur.execute(req, (inUser[1:] if inUser[0] == '0' else inUser,))

			nb_lignes = cur.rowcount

			if nb_lignes > 0:
				user = cur.fetchone()
				id_utilisateur = user[0]
				connecte = True
				print(f"Connecte ! Bonjour {user[2]} {user[1]}")
			else:
				print(f"Numero de telephone {inUser} inconnu; voulez-vous vous inscrire ? (0->non, 1->oui)")
				
				print("> ", end="")

				choix = int(input())

				if choix == 1:
					inscription(conn)
					connecte = True
				else:
					print("Connexion")


def consultation_billets(conn):
	pass

def gen_menu(conn, start_idx=0):
	menu = MenuHandler(start_idx)

	# menu.addMenuOption("Reserver", reservation_trajet, conn)
	# menu.addMenuOption("Consulter les reservations", consultation_billets, conn)
	# menu.addMenuOption("Modifier les reservations", modifier_reservation, conn)
	# menu.addMenuOption("Annuler les reservations", annuler_reservation, conn)
	menu.addQuitOption("Deconnexion")

	return menu

def open_user_menu(conn, start_idx=0):
	global id_utilisateur

	connexion(conn)

	menu = gen_menu(conn, start_idx)

	menu.handle()

	id_utilisateur = None
