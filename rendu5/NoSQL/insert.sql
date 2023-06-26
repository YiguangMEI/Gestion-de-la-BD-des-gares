/* -----------------
 Rempli notre BDD
----------------- */

-- Les gares


INSERT INTO Gare VALUES('Gare de Valence', 'Valence', '{"numeroVoie":3, "nomRue": "Avenue Victor Hugo", "codePostal": 26000}', 2,

    '[{

    "id_Hotel": 5,

    "nom": "Chez le marchand de sable",

     "ville": "Valence",

    "adresse":{

    "numeroVoie": 89,

    "nomRue": "Rue des mysteres",

    "codePostal": 26000

    }

    }]',

    '[{ "type":"BUS" }, { "type":"TAXI" }, { "type":"Metro" }]'

);

INSERT INTO Gare VALUES('Lyon Part-Dieu', 'Lyon', '{"numeroVoie":6, "nomRue": "Rue Christine Bravo",  "codePostal": 69000}', 2,

    ' [{"id_Hotel": 3,  "nom": "Le doux sommeil",   "ville": "Lyon","adresse":{

    "numeroVoie": 45,

    "nomRue": "Chemin du verre",

    "codePostal": 69000

    }

    },

    {"id_Hotel": 4,  "nom": "Au repos eternel", "ville": "Lyon", "adresse":{

    "numeroVoie": 5,

    "nomRue": "Avenue Francoise De Busy",

    "codePostal": 69000

    }

    }]',

    '[]'

);

INSERT INTO Gare VALUES('Lyon Perrache', 'Lyon', '{"numeroVoie":14, "nomRue": "Avenue de la Rose",  "codePostal": 69000}', 2,

    ' [{"id_Hotel": 3,  "nom": "Le doux sommeil",   "ville": "Lyon","adresse":{

    "numeroVoie": 45,

    "nomRue": "Chemin du verre",

    "codePostal": 69000

    }

    },

    {"id_Hotel": 4,  "nom": "Au repos eternel", "ville": "Lyon", "adresse":{

    "numeroVoie": 5,

    "nomRue": "Avenue Francoise De Busy",

    "codePostal": 69000

    }

    }]',

    '[{ "type":"BUS" }, { "type":"TAXI" }, { "type":"Metro" }]'

);

INSERT INTO Gare VALUES('Gare Pompidou', 'Compiegne', '{"numeroVoie":1, "nomRue": "Rue de la gare", "codePostal": 60000}', 2,

    '[{

    "id_Hotel": 2,

    "nom": "Au grand dormeur",

     "ville": "Compiegne",

    "adresse":{

    "numeroVoie": 10,

    "nomRue": "Avenue Henry Kavill",

    "codePostal": 60200

    }

    }]',

    '[{ "type":"BUS" }, { "type":"TAXI" }, { "type":"VTC" }]'

);

INSERT INTO Gare VALUES('Gare du Nord', 'Paris', '{"numeroVoie":18, "nomRue": "Rue de Dunkerque", "codePostal":75010}', 2,

    '[{

    "id_Hotel": 7,

    "nom": "Hotel 5 etoiles",

     "ville": "Paris",

    "adresse":{

    "numeroVoie": 6,

    "nomRue": "Rue du mytho",

    "codePostal": 75010

    }

    }]',

    '[{ "type":"BUS" }, { "type":"TAXI" }, { "type":"Metro" }, { "type":"Tramway" }, { "type":"VTC"}]'

);
INSERT INTO Gare VALUES('Gare Saint Charles', 'Marseille', '{"numeroVoie":138, "nomRue": "Rue des villes", "codePostal":13008}', 2,

    '[{

    "id_Hotel": 6,

    "nom": "Chez Colin",

     "ville": "Marseille",

    "adresse":{

    "numeroVoie": 55,

    "nomRue": "Avenue de la Comptine",

    "codePostal": 13008

    }

    }]',

    '[{ "type":"BUS" }]'

);

INSERT INTO Gare VALUES('Gare Pere Noel', 'Nuuk', '{"numeroVoie":13, "nomRue": "Rue de la neige", "codePostal":13008}', -1,

    '[{

    "id_Hotel": 6,

    "nom": "Chez Colin",

     "ville": "Marseille",

    "adresse":{

    "numeroVoie": 55,

    "nomRue": "Avenue de la Comptine",

    "codePostal": 13008

    }

    }]',

    '[{ "type":"VTC" }]'

);
-- Les types de trains

INSERT INTO TypeTrain VALUES('TGV',250,430,TRUE,20.3);
INSERT INTO TypeTrain VALUES('TER',250,200,FALSE,10.1);


--Les trains

INSERT INTO train VALUES (0,'TGV');
INSERT INTO train VALUES (1,'TGV');
INSERT INTO train VALUES (2,'TGV');
INSERT INTO train VALUES (3,'TGV');
INSERT INTO train VALUES (4,'TER');
INSERT INTO train VALUES (5,'TER');
INSERT INTO train VALUES (6,'TER');
INSERT INTO train VALUES (7,'TER');
INSERT INTO train VALUES (8,'TER');

--StatutCarte

INSERT INTO StatutCarte VALUES('Bronze');
INSERT INTO StatutCarte VALUES('Siliver');
INSERT INTO StatutCarte VALUES('Gold');
INSERT INTO StatutCarte VALUES('Platine');

-- Les voyageurs

INSERT INTO Voyageur VALUES (0,'Seuret', 'Noam',10, 'boulevard victor', '13009', '0715151515',NULL, NULL);
INSERT INTO Voyageur VALUES (1,'Carrillo', 'Gabri',11, 'boulevard victor', '13009', '0615151515',NULL, NULL);
INSERT INTO Voyageur VALUES (2,'Deforge', 'Elliot',100, 'Rue de limasse', '60200','0711111111',  NULL, NULL);
INSERT INTO Voyageur VALUES (3,'Brogi', 'eugenie',100, 'Rue de limasse', '60200', '0628187525',NULL, NULL);
INSERT INTO Voyageur VALUES (4,'Leroy', 'Mathis',22, 'boulevard des niches', '75010', '0625063626',NULL, NULL);
INSERT INTO Voyageur VALUES (5,'Brogi', 'alrick',138, 'Rue de strasse', '94001', '0607080900',11111, 'Platine');
INSERT INTO Voyageur VALUES (6,'Leroy', 'Sané',22, 'boulevard des triches', '13010', '0625063625',11112,'Bronze');

-- Les types de paiements

INSERT INTO TypePaiment VALUES('chèques');
INSERT INTO TypePaiment VALUES('carte bancaire');
INSERT INTO TypePaiment VALUES('Apple Pay');
INSERT INTO TypePaiment VALUES('Lydia');
INSERT INTO TypePaiment VALUES('Monnaie');

-- Billet

INSERT INTO Billet VALUES( 0, FALSE, 0, 'carte bancaire', '[
{"numeroTrajet" : 1, "numeroPlace" : 22, "prix": 12.5,"heureDepart": "08:00:00","heureArrivee":"11:55:00" ,"date" : "2023-05-05","voyage":1},
{"numeroTrajet" : 2, "numeroPlace": 72, "prix": 50,"heureDepart": "13:30:00","heureArrivee":"23:12:00" ,"date" : "2023-06-08","voyage":5}
     ]'  );

INSERT INTO Billet VALUES( 1, TRUE, 0, 'Apple Pay', '[
  {"numeroTrajet" : 1, "numeroPlace" : 12, "prix": 75,"heureDepart": "13:30:00","heureArrivee":"23:12:00" ,"date" : "2023-07-23","voyage":5}
     ] ' );

INSERT INTO Billet VALUES( 2, FALSE, 4, 'Monnaie', '[
{"numeroTrajet" : 1, "numeroPlace": 44, "prix": 12.5,"heureDepart": "7:00","heureArrivee":"8:00" ,"date" : "2023-02-08","voyage":3}
]'  );

INSERT INTO Billet VALUES( 3, TRUE, 3, 'Apple Pay', '[
{"numeroTrajet" : 1, "numeroPlace" : 36, "prix": 17,"heureDepart": "8:00:00","heureArrivee":"18:00:00" ,"date" : "2023-05-08","voyage":6}
]'  );


INSERT INTO Billet VALUES( 4, TRUE, 3, 'carte bancaire', '[
 {"numeroTrajet" : 1, "numeroPlace" : 46, "prix": 17,"heureDepart": "17:00:00","heureArrivee":"18:00:00" ,"date" : "2023-05-08","voyage":6}
]'  );

INSERT INTO Billet VALUES( 5, FALSE, 0, 'carte bancaire', '[
{"numeroTrajet" : 1, "numeroPlace": 44, "prix": 12.5,"heureDepart": "7:00:00","heureArrivee":"8:00:00" ,"date" : "2023-01-08","voyage":3}
]'  );


-- Ligne

INSERT INTO Ligne VALUES(1,'TGV');
INSERT INTO Ligne VALUES(2,'TER');
INSERT INTO Ligne VALUES(3,'TER');
INSERT INTO Ligne VALUES(4,'TGV');
INSERT INTO Ligne VALUES(5,'TGV');


-- Les gares desservies par les lignes

INSERT INTO LigneDessert VALUES('Lyon Part-Dieu', 'Lyon',1, 0);
INSERT INTO LigneDessert VALUES('Gare de Valence', 'Valence',1, 1);
INSERT INTO LigneDessert VALUES('Gare du Nord', 'Paris',1, 2);
INSERT INTO LigneDessert VALUES('Lyon Part-Dieu', 'Lyon',2, 0);
INSERT INTO LigneDessert VALUES('Gare Pompidou', 'Compiegne',2, 2);
INSERT INTO LigneDessert VALUES('Gare du Nord', 'Paris',4, 1);
INSERT INTO LigneDessert VALUES('Gare du Nord', 'Paris',5, 1);

-- Voyages

INSERT INTO Voyage VALUES(1,'08:00:00',0,1, '[ {
	    "dateDepart" : "2023-01-01",
	    "dateFin": "2023-06-01",
	    "lundi": true,
	    "mardi": true,
	    "mercredi": true,
		"jeudi": true,
		"vendredi": true,
		"samedi": true,
	  	"dimanche": true,
	    "exception": [ { "jour": "2023-05-01", "ajout": false }]
    },
    {
    	    "dateDepart" : "2023-06-02",
    	    "dateFin": "2023-12-31",
    	    "lundi": true,
    	    "mardi": true,
    	    "mercredi": true,
    		"jeudi": true,
    		"vendredi": true,
    		"samedi": true,
    	  	"dimanche": true,
    	    "exception": [ { "jour": "2023-07-03", "ajout": false }]
        }
]');

INSERT INTO Voyage VALUES(2,'08:30:00',1,1, '[
	{
		"dateDepart" : "2023-01-01",
	    "dateFin": "2023-06-01",
	    "lundi": false,
	    "mardi": false,
	    "mercredi": false,
		"jeudi": false,
		"vendredi": true,
		"samedi": true,
	  	"dimanche": true,
	    "exception": [ { "jour": "2023-05-01", "ajout": false }]
	}
]');

INSERT INTO Voyage VALUES(3,'09:00:00',3,2, '[
	{
		"dateDepart" : "2023-06-02",
	    "dateFin": "2023-12-31",
	    "lundi": false,
	    "mardi": false,
	    "mercredi": false,
		"jeudi": false,
		"vendredi": true,
		"samedi": true,
	  	"dimanche": true,
	    "exception": [
	    	{ "jour": "2023-08-04", "ajout": true },
	    	{ "jour": "2023-07-03", "ajout": false }
	    ]
	}
]');

INSERT INTO Voyage VALUES(4,'10:00:00',4,3, '[
    {
	    "dateDepart" : "2023-01-01",
	    "dateFin": "2023-06-01",
	    "lundi": true,
	    "mardi": true,
	    "mercredi": true,
		"jeudi": true,
		"vendredi": true,
		"samedi": true,
	  	"dimanche": true,
	    "exception": [ { "jour": "2023-05-01", "ajout": false }]
    }
]');

INSERT INTO Voyage VALUES(5,'11:00:00',5,4, '[
    {
	    "dateDepart" : "2023-01-01",
	    "dateFin": "2023-06-01",
	    "lundi": true,
	    "mardi": true,
	    "mercredi": true,
		"jeudi": true,
		"vendredi": true,nom
		"samedi": true,
	  	"dimanche": true,
	    "exception": [ { "jour": "2023-05-01", "ajout": false }]
    },
    {
          "dateDepart" : "2023-06-02",
          "dateFin": "2023-12-31",
          "lundi": true,
          "mardi": true,
          "mercredi": true,
        "jeudi": true,
        "vendredi": true,
        "samedi": true,
          "dimanche": true,
          "exception": [ { "jour": "2023-07-03", "ajout": false }]
        }
]');

INSERT INTO Voyage VALUES(6,'17:00:00',6,2, '[
	{
		"dateDepart" : "2023-01-01",
	    "dateFin": "2023-06-01",
	    "lundi": false,
	    "mardi": false,
	    "mercredi": false,
		"jeudi": false,
		"vendredi": true,
		"samedi": true,
	  	"dimanche": true,
	    "exception": [ { "jour": "2023-05-01", "ajout": false }]
	}
]');

-- Les gares desservies par les voyages

/* ------------
ATTENTION :
CONTRAINTE 1 : les gares desservies par des voyages doivent être desservies par la ligne auquel appartient un voyage
CONTRAINTE 2 : les heure de départ de la gare de départ doit correspondre avec l'heure de départ du voyage
CONTRAINTE 3 : faire coïncider heure de départ et ordre de passage
(A gérer en applicatif)
------------ */

INSERT INTO VoyageDessert VALUES('Lyon Part-Dieu', 'Lyon',1,NULL,'08:00:00');
INSERT INTO VoyageDessert VALUES('Gare de Valence', 'Valence',1,'10:20:00','10:23:00');
INSERT INTO VoyageDessert VALUES('Gare du Nord', 'Paris',1,'11:55:00',NULL);
INSERT INTO VoyageDessert VALUES('Gare du Nord', 'Paris',5, '13:20:00','13:30:00');
INSERT INTO VoyageDessert VALUES('Gare du Nord', 'Paris',6,NULL,'17:00:00');
INSERT INTO VoyageDessert VALUES('Gare Pompidou', 'Compiegne',6,'18:00:00',NULL);
