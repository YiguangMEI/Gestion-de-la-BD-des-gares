#!/usr/bin/python3

from MenuHandler import MenuHandler, UnknownMenu, QuitMenu

def call_option1(p1, p2):

	def f0(p1, p2):
		print(p1, p2)

	def f1(p1, p2):
		print(p1 - p2)

	def f2(p1, p2):
		print(p1 + p2)

	print("Bonjour dans l'option 1, que souhaitez vous faire ?...")

	menu2 = MenuHandler(5)

	menu2.addMenuOption("afficher", f0, p1, p2)
	menu2.addMenuOption("additioner", f2, p1, p2)
	menu2.addMenuOption("soustraire", f1, p1, p2)
	menu2.addQuitOption("Retour au menu principal")

	# Gere automatiquement les interactions avec l'utilisateur
	menu2.handle()

	print("Au revoir de option 1")

def call_option2(v):
	print(v)


if __name__ == "__main__":
	print("Bienvenu dans la demo de menu handler...")

	menu1 = MenuHandler()

	menu1.addMenuOption("Option 1", call_option1, 15, 60)

	menu1Bis = MenuHandler(6)
	menu1Bis.addMenuOption("Option 2", call_option2, 7)

	menu1 += menu1Bis
	
	menu1.addQuitOption("Quitter")

	# Gestion manuelle des interactions utilisateur

	active = True

	while active:
		menu1.show()

		inUser = int(input())

		try:
			menu1.openMenu(inUser)
		except UnknownMenu as err:
			print("Menu inconnu...")
		except QuitMenu:
			active = False

	print("Au revoir...")
