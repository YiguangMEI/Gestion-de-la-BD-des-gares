import sys


class UnknownMenu(Exception):
	def __init__(self, msg=""):
		super().__init__(msg)


class QuitMenu(Exception) :
	def __init__(self, msg=""):
		super().__init__(msg)

# Permet de gérer les menus
class MenuHandler:

	# Initialise un nouveau menu
	# params:
	#  start_index : indice de départ des options du menu (optionnel)
	def __init__(self, start_index=0):
		self.menu = {}
		self.start_index = start_index
		self.quit_index = -1

	# Donne le nombre d'options de menus définis
	def __len__(self):
		return len(self.menu)

	# Convertit le menu en 1 chaîne de caractères
	def __str__(self):	
		s = ""
		for option in self.menu:
			s += f"{option} - {self.menu[option][0]}\n"
		return s

	# Ajout d'une nouvelle option de menu
	# params:
	#  menu_name : le nom de l'option a afficher
	#  menu_function : la fonction à appeler lors ce que l'option est choisie
	#  params : la liste des paramètres à donner à la fonction lors de son appel
	def addMenuOption(self, menu_name, menu_function, *params):
		self.menu[len(self)+self.start_index] = [menu_name, menu_function, params]

	# Ajout d'une option pour quitter le menu
	# params:
	#  title : le titre à afficher lors de la présentation des options
	def addQuitOption(self, title):
		self.quit_index = len(self) + self.start_index
		self.addMenuOption(title, None)

	# Ouvre une option du menu
	# params:
	#  menu_index : l'indice de l'option à ouvrir
	#  params : les paramètres à donner à la fonction associé à l'option (optionnel)
	#             => Si paramètres fournies : surchargent les paramètres donnés dans addMenuOption()
	# exceptions:
	#  UnknownMenu : Si l'indice du menu demandé ne correspond pas à une option de menu ajoutée
	#  QuitMenu : Si l'indice de menu demandé correspond à celui de l'option pour quitter le menu
	def openMenu(self, menu_index, *params):
		if menu_index >= len(self) + self.start_index or menu_index < self.start_index:
			raise UnknownMenu(f"Le menu n°{menu_index} n'existe pas.")

		if menu_index == self.quit_index:
			raise QuitMenu()

		if params:
			return self.menu[menu_index][1](*params)
		else:
			return self.menu[menu_index][1](*self.menu[menu_index][2])

	# Gère les interactions entre l'utilisateur et le menu
	def handle(self):
		active = True

		while active:
			self.show()

			print("> ", end="")

			try:
				choix = int(input())

				try:
					self.openMenu(choix)
				except UnknownMenu:
					print(f"Le menu n°{choix} n'existe pas.")
				except QuitMenu:
					active = False

			except ValueError:
				print("Entree utilisateur n'est pas un nombre entier")

	# Montre le menu à l'écran
	def show(self, file=sys.stdout):
		print("------", file=file)
		print(self, file=file)

	