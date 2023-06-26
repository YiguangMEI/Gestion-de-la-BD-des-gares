# Application de gestion de trains

## Auteurs - Groupe 6
- Litchi Liang
- Yiguang Mei
- Nathan Menny
- Noam Seuret

## Utilisation

Afin de lancer l'application, il suffit d’exécuter le script `main.py` avec Python3 et en ayant au préalable installé la bibliothèque psycopg2 qui permet d'établir une connexion avec une base de données postgresql.   

❗Il faut être connecté au réseau de l'UTC afin de pouvoir utiliser l'application ! En effet, la base de données est stockée sur un serveur local à l'UTC ce qui la rend inaccessible de l’extérieur sans l'utilisation du VPN.    
Toutefois, il est possible d'utiliser l'application en local en changeant la configuration de psycopg2 dans le fichier main.py et en exécutant les scripts `create.sql` et `fill.sql` rangés dans le dossier *rendu3* dans votre propre BD.

Commande :    
```
python3 main.py
```

Le programme établira ainsi une connexion avec la base de données à l'UTC, permettant ainsi la bonne utilisation du programme.

Ensuite, pour utiliser l'application, il suffit de rentrer au clavier la valeur qui correspond au menu afficher et de donner les informations que l'application demande.

## Exemples

Afin de reserver des trajets, il faut que l'utilisateur se connecter en donnant son numero de telephone. On pourrait imaginer dans une version plus avancée de l'application l'ajout de mot de passes.    
Par exemple, un utilisateur a le numero de telephone suivant : `0715151515`.