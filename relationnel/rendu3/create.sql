/* --------

Supprime les tables, vues et types

-------- */

drop view if exists VvoyageurRegulier CASCADE;

drop view if exists VPrixBillet CASCADE;

drop view if exists VvoyageurOccasionnel CASCADE;

drop view if exists vNbPersParTrain CASCADE;

drop table if exists LigneDessert CASCADE;

drop table if exists VoyageDessert CASCADE;

-- drop table if exists HotelProcheDeGare CASCADE;

-- drop table if exists TransportProcheDeGare CASCADE;

-- drop table if exists ExceptionPlannification CASCADE;

-- drop table if exists VoyagePlannifie CASCADE;

-- drop table if exists Trajet CASCADE;

drop table if exists Billet CASCADE;

drop table if exists TypePaiment CASCADE;

drop table if exists Voyageur CASCADE;

drop table if exists StatutCarte CASCADE;

-- drop table if exists JourException CASCADE;

-- drop table if exists Plannification CASCADE;

drop table if exists Voyage CASCADE;

drop table if exists Train CASCADE;

drop table if exists Ligne CASCADE;

drop table if exists TypeTrain CASCADE;

-- drop table if exists Hotel CASCADE;

-- drop table if exists Transport CASCADE ;

drop table if exists Gare CASCADE;

-- drop type if exists TypeTransport CASCADE;


/* Creation des types */

-- create type TypeTransport as enum ('Bus', 'Metro', 'Tramway', 'Taxi', 'VTC');

/* Creation des tables */

/*
  La gare va dorénavant contenir deux champs JSON : Un pour les hotels à proximité et 
  un pour les transports qui deservent la gare
*/

-- CREATE TABLE Gare (
--   nom VARCHAR,
--   ville VARCHAR,
--   numeroVoie SMALLINT NOT NULL,
--   nomRue VARCHAR NOT NULL,
--   codePostal CHAR(5) NOT NULL,
--   zoneHorraire SMALLINT NOT NULL CHECK (zoneHorraire >= -12 AND zoneHorraire <= 12),
--   PRIMARY KEY (nom, ville)
-- );


/*
  On a mis les tables Hotel et Transport en JSON car ce ne sont pas des informations 
   que l'on considère comme nécéssitant une grande fiabilité.
*/

-- CREATE TABLE Hotel (
--   id_Hotel INT,
--   nom VARCHAR NOT NULL,
--   numeroVoie SMALLINT NOT NULL,
--   nomRue VARCHAR NOT NULL,
--   codePostal CHAR(5) NOT NULL,
--   ville VARCHAR NOT NULL,
--   PRIMARY KEY (id_Hotel)
-- );

-- CREATE TABLE HotelProcheDeGare (
--     hotel INT REFERENCES Hotel(id_Hotel),
--     nom_gare VARCHAR,
--     ville_gare VARCHAR,
--     FOREIGN KEY (nom_gare, ville_gare) REFERENCES Gare(nom, ville),
--     PRIMARY KEY(hotel, nom_gare, ville_gare)
-- );

-- CREATE TABLE Transport (
--   id_Transpot INT,
--   type TypeTransport NOT NULL,
--   ville VARCHAR NOT NULL,
--   PRIMARY KEY (id_Transpot)
-- );

-- CREATE TABLE TransportProcheDeGare(
--     transport INT REFERENCES Transport(id_Transpot),
--     nom_gare VARCHAR,
--     ville_gare VARCHAR,
--     FOREIGN KEY (nom_gare, ville_gare) REFERENCES Gare(nom, ville),
--     PRIMARY KEY(nom_gare, ville_gare, transport)
-- );

CREATE TABLE TypeTrain (
  nom VARCHAR,
  nbPlace SMALLINT NOT NULL CHECK (nbPlace >= 0),
  vitesseMax INT NOT NULL CHECK (vitesseMax >= 0),
  aPremiereClasse BOOLEAN NOT NULL,
  coutHeure FLOAT NOT NULL CHECK (coutHeure > 0),
  PRIMARY KEY (nom)
);

CREATE TABLE Ligne (
  numero INT,
  type_train_autorise VARCHAR NOT NULL,
  PRIMARY KEY (numero),
  FOREIGN KEY (type_train_autorise) REFERENCES TypeTrain(nom)
);


CREATE TABLE LigneDessert(
    nomGare VARCHAR,
    villeGare VARCHAR,
    ligne INT,
    ordre SMALLINT NOT NULL,
    PRIMARY KEY (nomGare,villeGare,ligne),
    FOREIGN KEY (nomGare, villeGare) REFERENCES Gare(nom, ville),
    FOREIGN KEY (ligne) REFERENCES Ligne(numero),
    UNIQUE (ligne,ordre)
);

CREATE TABLE Train (
  numero INT,
  type VARCHAR NOT NULL,
  PRIMARY KEY (numero),
  FOREIGN KEY (type) REFERENCES TypeTrain(nom)
);

CREATE TABLE Voyage (
  id_Voyage INTEGER,
  heureDepart TIME NOT NULL,
  train INT NOT NULL,
  ligne INT NOT NULL,
  PRIMARY KEY (id_Voyage),
  FOREIGN KEY (train) REFERENCES Train(numero),
  FOREIGN KEY (ligne) REFERENCES Ligne(numero)
);


CREATE TABLE VoyageDessert(
    nomGare VARCHAR,
    villeGare VARCHAR,
    voyage INT,
    heureArrivee TIME, -- sera NULL si est depart
    heureDepart TIME, -- sera NULL si est terminus
    PRIMARY KEY (nomGare,villeGare,voyage),
    FOREIGN KEY (nomGare, villeGare) REFERENCES Gare(nom, ville),
    FOREIGN KEY (voyage) REFERENCES Voyage(id_Voyage)
);

CREATE TABLE Plannification (
  idPlanification INT,
  dateDepart DATE NOT NULL,
  dateFin DATE NOT NULL,
  lundi BOOLEAN NOT NULL,
  mardi BOOLEAN NOT NULL,
  mercredi BOOLEAN NOT NULL,
  jeudi BOOLEAN NOT NULL,
  vendredi BOOLEAN NOT NULL,
  samedi BOOLEAN NOT NULL,
  dimanche BOOLEAN NOT NULL,
  PRIMARY KEY (idPlanification),
  CHECK (dateDepart < dateFin),
  CHECK (lundi or mardi or mercredi or jeudi or vendredi or samedi or dimanche)
);


CREATE TABLE JourException (
  jour DATE,
  ajout BOOLEAN NOT NULL,
  PRIMARY KEY (jour)
);

CREATE TABLE ExceptionPlannification(
    jour DATE REFERENCES JourException(jour),
    plannification INT REFERENCES Plannification(idPlanification),
    PRIMARY KEY(jour, plannification)

);

CREATE TABLE VoyagePlannifie(
    plannification INT REFERENCES Plannification(idPlanification),
    voyage INT REFERENCES Voyage(id_Voyage),
    PRIMARY KEY (plannification, voyage)

);

CREATE TABLE StatutCarte (
  intitule VARCHAR,
  PRIMARY KEY (intitule)
);

CREATE TABLE Voyageur (
  idVoyageur INTEGER,
  nom VARCHAR NOT NULL,
  prenom VARCHAR NOT NULL,
  numeroVoie SMALLINT NOT NULL,
  nomRue VARCHAR NOT NULL,
  codePostal CHAR(5) NOT NULL,
  tel VARCHAR UNIQUE NOT NULL,
  numeroCarte INT UNIQUE,
  statut VARCHAR,
  PRIMARY KEY (idVoyageur),
  FOREIGN KEY (statut) REFERENCES StatutCarte(intitule),
  CHECK ((numeroCarte IS NULL AND statut IS NULL) OR (numeroCarte IS NOT NULL AND statut IS NOT NULL))
);

CREATE TABLE TypePaiment (
  intitule VARCHAR,
  PRIMARY KEY (intitule)
);

CREATE TABLE Billet (
  idBillet INTEGER PRIMARY KEY,
  assurance BOOLEAN NOT NULL,
  acheteur INTEGER NOT NULL,
  typePaiement VARCHAR,
  FOREIGN KEY (acheteur) REFERENCES Voyageur(idVoyageur),
  FOREIGN KEY (typePaiement) REFERENCES TypePaiment(intitule)
);

CREATE TABLE Trajet (
  billet INTEGER,
  numeroTrajet INTEGER,
  numeroPlace SMALLINT NOT NULL,
  voyage INT NOT NULL,
  prix DECIMAL(5,2) NOT NULL,
  heureDepart TIME NOT NULL,
  heureArrivee TIME NOT NULL, 
  date DATE NOT NULL, --A tester
  PRIMARY KEY (billet, numeroTrajet),
  CHECK (numeroPlace >= 0 AND numeroTrajet >= 0),
  FOREIGN KEY (billet) REFERENCES Billet(idBillet),
  FOREIGN KEY (voyage) REFERENCES Voyage(id_Voyage)
);


/* ------------

Creer les vues

------------ */


-- Vue des voyageurs réguliers

CREATE VIEW VvoyageurRegulier AS 
SELECT idVoyageur, nom, prenom, numeroVoie, nomRue, codePostal, tel, numeroCarte, statut 
FROM Voyageur 
WHERE statut IS NOT NULL;


-- Vue des voyageurs occasionnels

CREATE VIEW VvoyageurOccasionnel AS 
SELECT idVoyageur, nom, prenom, numeroVoie, nomRue, codePostal, tel 
FROM Voyageur 
WHERE statut IS NULL;


-- Vue PrixBillet

CREATE VIEW VPrixBillet AS 
SELECT idBillet, (SELECT SUM(prix) as prixBillet 
  FROM trajet 
  WHERE trajet.billet=idBillet
) 
from billet;


-- Vue du nombre de personnes par train

create view vNbPersParTrain (train, nbPersonnes) as
select t.numero, count(*)
from train t join typetrain tt on t.type = tt.nom
    join voyage v on t.numero = v.train
    join trajet tr on v.id_voyage = tr.voyage
group by t.numero;