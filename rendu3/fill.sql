/* -----------------
 Rempli notre BDD
----------------- */

-- Les gares

INSERT INTO Gare VALUES('Gare de Valence', 'Valence', 3, 'Avenue Victor Hugo', '26000', 2);
INSERT INTO Gare VALUES('Lyon Part-Dieu', 'Lyon', 6, 'Rue Christine Bravo', '69000', 2);
INSERT INTO Gare VALUES('Lyon Perrache', 'Lyon', 14, 'Avenue de la Rose', '69000', 2);
INSERT INTO Gare VALUES('Gare Pompidou', 'Compiegne', 1, 'Rue de la gare', '60000', 2);
INSERT INTO Gare VALUES('Gare du Nord', 'Paris', 18, 'Rue de Dunkerque', '75010', 2);
INSERT INTO Gare VALUES('Gare de Lyon', 'Paris', 5, 'Avenue Louis-Armand', '75010', 2);
INSERT INTO Gare VALUES('Gare Saint Charles', 'Marseille', 138,'Rue des villes','13008',2);
INSERT INTO Gare VALUES('Gare Pere Noel', 'Nuuk', 13,'Rue de la neige','13008',-1);


--Les Transports

INSERT INTO Transport VALUES( 5, 'Bus', 'Compiegne' );
INSERT INTO Transport VALUES( 2, 'Tramway', 'TParis' );
INSERT INTO Transport VALUES( 30, 'Taxi', 'Paris' );
INSERT INTO Transport VALUES( 27, 'VTC', 'Nuuk' );
INSERT INTO Transport VALUES( 34, 'Bus', 'Marseille' );


-- Les Hotels

INSERT INTO Hotel VALUES (0, 'Hotel de la gare', 5,  'Rue Gustave Pierrot', '75010', 'Paris');
INSERT INTO Hotel VALUES (1, 'Hotel de la Drome', 7, 'Boulevard Pierre Galimard', '26000', 'Valence');
INSERT INTO Hotel VALUES (2, 'Au grand dormeur', 10, 'Avenue Henry Kavill', '60200', 'Compiegne');
INSERT INTO Hotel VALUES (3, 'Le doux sommeil', 45, 'Chemin du verre', '69000', 'Lyon');
INSERT INTO Hotel VALUES (4, 'Au repos eternel', 5, 'Avenue Francoise De Busy', '69000', 'Lyon');
INSERT INTO Hotel VALUES (5, 'Chez le marchand de sable', 89, 'Rue des mysteres', '26000', 'Valence');
INSERT INTO hotel VALUES (6, 'Chez Colin', 55, 'Avenue de la comptine', '13008', 'Marseille');
INSERT INTO Hotel VALUES (7, 'Hotel 5 etoiles', 6, 'Rue du mytho', '75010', 'Paris');


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

-- Les hotels proche de gares

INSERT INTO HotelProcheDeGare VALUES (0, 'Gare de Lyon', 'Paris');
INSERT INTO HotelProcheDeGare VALUES (7, 'Gare du Nord', 'Paris');
INSERT INTO HotelProcheDeGare VALUES (4, 'Lyon Part-Dieu', 'Lyon');
INSERT INTO HotelProcheDeGare VALUES (3, 'Lyon Perrache', 'Lyon');
INSERT INTO HotelProcheDeGare VALUES (2, 'Gare Pompidou', 'Compiegne');
INSERT INTO HotelProcheDeGare VALUES (1, 'Gare de Valence', 'Valence');
INSERT INTO HotelProcheDeGare VALUES (5, 'Gare de Valence', 'Valence');
INSERT INTO HotelProcheDeGare VALUES (6, 'Gare Saint Charles', 'Marseille');
INSERT INTO HotelProcheDeGare VALUES (6, 'Gare Pere Noel', 'Nuuk');


--Les transports proche de gares

INSERT INTO TransportProcheDeGare VALUES(5,'Gare Pompidou', 'Compiegne');
INSERT INTO TransportProcheDeGare VALUES(2,'Gare du Nord', 'Paris');
INSERT INTO TransportProcheDeGare VALUES(30,'Gare de Lyon', 'Paris');
INSERT INTO TransportProcheDeGare VALUES(27,'Gare Pere Noel', 'Nuuk');
INSERT INTO TransportProcheDeGare VALUES(34,'Gare Saint Charles', 'Marseille');


--StatutCarte

INSERT INTO StatutCarte VALUES('Bronze');
INSERT INTO StatutCarte VALUES('Siliver');
INSERT INTO StatutCarte VALUES('Gold');
INSERT INTO StatutCarte VALUES('Platine');


-- Les voyageurs

INSERT INTO Voyageur VALUES (0,'Seuret', 'Noam',10, 'boulevard victor', 13009, 0715151515,NULL, NULL);
INSERT INTO Voyageur VALUES (1,'Carrillo', 'Gabri',11, 'boulevard victor', 13009, 0615151515,NULL, NULL);
INSERT INTO Voyageur VALUES (2,'Deforge', 'Elliot',100, 'Rue de limasse', 60200,0711111111,  NULL, NULL);
INSERT INTO Voyageur VALUES (3,'Brogi', 'eugenie',100, 'Rue de limasse', 60200, 0628187525,NULL, NULL);
INSERT INTO Voyageur VALUES (4,'Leroy', 'Mathis',22, 'boulevard des niches', 75010, 0625063626,NULL, NULL);
INSERT INTO Voyageur VALUES (5,'Brogi', 'alrick',138, 'Rue de strasse', 94001, 0607080900,11111, 'Platine');
INSERT INTO Voyageur VALUES (6,'Leroy', 'Sané',22, 'boulevard des triches', 13010, 0625063625,11112,'Bronze');


-- Les types de paiements

INSERT INTO TypePaiment VALUES('chèques');
INSERT INTO TypePaiment VALUES('carte bancaire');
INSERT INTO TypePaiment VALUES('Apple Pay');
INSERT INTO TypePaiment VALUES('Lydia');
INSERT INTO TypePaiment VALUES('Monnaie');


-- Les billets

INSERT INTO Billet VALUES (0, FALSE, 0, 'carte bancaire');
INSERT INTO Billet VALUES (1, TRUE, 0, 'Apple Pay');
INSERT INTO Billet VALUES (2, TRUE, 3, 'Apple Pay');
INSERT INTO Billet VALUES (3, FALSE, 4, 'Monnaie');
INSERT INTO Billet VALUES (4, TRUE, 3, 'carte bancaire');
INSERT INTO Billet VALUES (5, FALSE, 0, 'carte bancaire');


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
INSERT INTO LigneDessert VALUES('Gare de Lyon', 'Paris',2, 1);
INSERT INTO LigneDessert VALUES('Gare Pompidou', 'Compiegne',2, 2);
INSERT INTO LigneDessert VALUES('Lyon Perrache', 'Lyon', 3, 0);
INSERT INTO LigneDessert VALUES('Gare Saint Charles', 'Marseille', 3, 1);
INSERT INTO LigneDessert VALUES('Gare Saint Charles', 'Marseille', 4, 0);
INSERT INTO LigneDessert VALUES('Gare du Nord', 'Paris',4, 1);
INSERT INTO LigneDessert VALUES('Gare Pere Noel', 'Nuuk',4, 2);
INSERT INTO LigneDessert VALUES('Gare Saint Charles', 'Marseille',5 , 2);
INSERT INTO LigneDessert VALUES('Gare du Nord', 'Paris',5, 1);
INSERT INTO LigneDessert VALUES('Gare Pere Noel', 'Nuuk',5, 0);


-- Voyage

INSERT INTO Voyage VALUES(1,'08:00:00',0,1);
INSERT INTO Voyage VALUES(2,'08:30:00',1,1);
INSERT INTO Voyage VALUES(3,'09:00:00',3,2);
INSERT INTO Voyage VALUES(4,'10:00:00',4,3);
INSERT INTO Voyage VALUES(5,'11:00:00',5,4);
INSERT INTO Voyage VALUES(6,'17:00:00',6,2);


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
INSERT INTO VoyageDessert VALUES('Gare Saint Charles', 'Marseille', 5,NULL,'11:00:00');
INSERT INTO VoyageDessert VALUES('Gare du Nord', 'Paris',5, '13:20:00','13:30:00');
INSERT INTO VoyageDessert VALUES('Gare Pere Noel', 'Nuuk',5, '23:12:00',NULL);
INSERT INTO VoyageDessert VALUES('Gare du Nord', 'Paris',6,NULL,'17:00:00');
INSERT INTO VoyageDessert VALUES('Gare Pompidou', 'Compiegne',6,'18:00:00',NULL);

/* ------------
ATTENTION :
CONTRAINTE 1 : les heures de départ\arrivé des trajets doivent correspondre aux heures de départ\arrivé de VoyageDessert du voyage auquel appartient le trajet
CONTRAINTE 2 : 
CONTRAINTE 3 : La date du trajet doit correspondre à la planification du voyage auquel il appartient 
(A gérer en applicatif)     
------------ */


-- Trajet

INSERT INTO Trajet VALUES (0,0, 1,1,38, '08:00:00','11:55:00','2023-05-03');
INSERT INTO Trajet VALUES (0,1, 23,5,89,'13:30:00','23:12:00','2023-05-03');
INSERT INTO Trajet VALUES (1,0, 13,5,89, '13:30:00','23:12:00','2023-04-04');
INSERT INTO Trajet VALUES (2,0, 23,1,25,'08:00:00','10:20:00','2023-02-23');  
INSERT INTO Trajet VALUES (3,0, 8,6, 14, '17:00:00','18:00:00','2023-03-05');
INSERT INTO Trajet VALUES (4,0, 7,6,14, '17:00:00','18:00:00','2023-04-30');
INSERT INTO Trajet VALUES (5,0, 1,1,38, '08:00:00','11:55:00','2023-05-03');


-- Plannification

INSERT INTO Plannification VALUES(1,'2023-01-01','2023-06-01',TRUE,TRUE,TRUE,TRUE,TRUE,TRUE,TRUE);
INSERT INTO Plannification VALUES(2,'2023-01-01','2023-06-01',FALSE,FALSE,FALSE,FALSE,TRUE,TRUE,TRUE);
INSERT INTO Plannification VALUES(3,'2023-06-02','2023-12-31',TRUE,TRUE,TRUE,TRUE,TRUE,TRUE,TRUE);
INSERT INTO Plannification VALUES(4,'2023-06-02','2023-12-31',FALSE,FALSE,FALSE,FALSE,TRUE,TRUE,TRUE);


-- JourException

INSERT INTO JourException VALUES('2023-05-01',FALSE);
INSERT INTO JourException VALUES('2023-06-02',TRUE);
INSERT INTO JourException VALUES('2023-07-03',FALSE);
INSERT INTO JourException VALUES('2023-08-04',TRUE);


-- Les plannifications impactées par des jours d'exception

INSERT INTO ExceptionPlannification VALUES ('2023-05-01', 1);
INSERT INTO ExceptionPlannification VALUES ('2023-05-01', 2);
INSERT INTO ExceptionPlannification VALUES ('2023-08-04', 3);
INSERT INTO ExceptionPlannification VALUES ('2023-07-03', 3);


-- Les voyages impacté par une plannification

INSERT INTO VoyagePlannifie VALUES(1,1);
INSERT INTO VoyagePlannifie VALUES(2,2);
INSERT INTO VoyagePlannifie VALUES(3,3);
INSERT INTO VoyagePlannifie VALUES(1,4);
INSERT INTO VoyagePlannifie VALUES(1,5);
INSERT INTO VoyagePlannifie VALUES(2,6);

