/* ------------

les requêtes sympa à faire
 
------------ */

--les numeros des lignes desservant Paris : simple
SELECT l.numero 
FROM ligne l INNER JOIN lignedessert ld ON l.numero = ld.ligne
WHERE UPPER(ld.villeGare)='PARIS';

--les voyages disponibles pour faire Paris-Compiègne ainsi que les horraires correspondantes (sans tenir compte des planifications)
SELECT vg.voyage,vg.heureDepart,vd.heurearrivee
FROM voyageDessert vg INNER JOIN voyageDessert vd ON vg.voyage = vd.voyage
WHERE vg.villeGare='Paris' AND vd.villeGare='Compiegne';

--Les jours où ce voyage Paris-Compiègne est disponible d'après la planification (sans tenir compte des exceptions)
SELECT dateDepart,dateFin,lundi,mardi,mercredi,jeudi,vendredi,samedi,dimanche 
FROM plannification p INNER JOIN VoyagePlannifie vp ON p.idPlanification=vp.plannification
WHERE vp.voyage=(SELECT vg.voyage 
    FROM voyageDessert vg INNER JOIN voyageDessert vd ON vg.voyage=vd.voyage
    WHERE vg.villeGare='Paris' AND vd.villeGare='Compiegne'
);

-- Les voyages Paris-Compiègne annulés à cause d'une exception

SELECT je.jour, 'voyage annulé ce jour-là' as indication 
FROM plannification p
INNER JOIN VoyagePlannifie vp  ON p.idPlanification=vp.plannification
INNER JOIN ExceptionPlannification ep  ON ep.plannification=p.idPlanification
INNER JOIN JourException je ON ep.jour =je.jour
WHERE vp.voyage=(SELECT vg.voyage 
    FROM voyageDessert vg INNER JOIN voyageDessert vd ON vg.voyage=vd.voyage
    WHERE vg.villeGare='Paris' AND vd.villeGare='Compiegne'
) AND (je.ajout=FALSE);

-- Les voyages Paris-Compiègne ajouté à cause d'une exception

SELECT je.jour, 'voyage ajouté jour-là' as indication 
FROM plannification p
INNER JOIN VoyagePlannifie vp  ON p.idPlanification=vp.plannification
INNER JOIN ExceptionPlannification ep  ON ep.plannification=p.idPlanification
INNER JOIN JourException je ON ep.jour = je.jour
WHERE vp.voyage=(SELECT vg.voyage 
    FROM voyageDessert vg INNER JOIN voyageDessert vd ON vg.voyage=vd.voyage
    WHERE vg.villeGare='Paris' AND vd.villeGare='Compiegne'
) AND (je.ajout=TRUE);

-- Un utilisateur veut savoir quels voyages sont disponibles pour faire Paris-Compiègne le dimanche 05\03\2023
SELECT vg.voyage,vg.heureDepart,vd.heurearrivee
FROM voyageDessert vg
INNER JOIN voyageDessert vd ON vg.voyage=vd.voyage
INNER JOIN VoyagePlannifie vp ON vg.voyage=vp.voyage
INNER JOIN Plannification p ON vp.plannification=p.idPlanification
INNER JOIN ExceptionPlannification ep  ON ep.plannification=p.idPlanification
INNER JOIN JourException je ON ep.jour =je.jour
WHERE vg.villeGare='Paris' AND vd.villeGare='Compiegne' AND p.dateDepart<='2023-03-05' AND p.dateFin>='2023-03-05' AND (p.dimanche=TRUE OR (je.jour='2023-03-05' and je.ajout=TRUE)) AND NOT (je.jour='2023-03-05' and je.ajout=FALSE);

--prix moyen d'un billet acheté
SELECT AVG(PB.prixBillet)
FROM VPrixBillet PB;

--prix moyen d'un billet selon le moyen de paiement
SELECT B.typePaiement, AVG(PB.prixBillet)
FROM VPrixBillet PB
INNER JOIN Billet B ON
PB.idBillet=B.idBillet
GROUP BY(B.typePaiement);


--prix moyen d'un billet payé par statut
SELECT v.statut, AVG(PB.prixBillet)
FROM VPrixBillet PB
INNER JOIN Billet B ON
PB.idBillet=B.idBillet
INNER JOIN voyageur v ON
B.acheteur=v.idvoyageur
WHERE statut IS NOT NULL
GROUP BY (v.statut);

-- le nombre de trajet fait par des voyageur pour un voyage donné ici =1 à une date donné ici='2023-05-03' et une heure de départ ici = '08:00:00'
SELECT count(*) as nombre_place_occupe FROM trajet t
WHERE t.voyage=1 and t.date='2023-05-03' AND t.heureDepart= '08:00:00';

-- le nombre de place par voyage
SELECT v.id_voyage, tp.nbPlace FROM voyage v
INNER JOIN ligne l ON v.ligne=l.numero
INNER JOIN TypeTrain tp ON l.type_train_autorise=tp.nom;

-- le nombre de place pour un voyage donné ici =1
SELECT tp.nbPlace FROM voyage v
INNER JOIN ligne l ON v.ligne=l.numero
INNER JOIN TypeTrain tp ON l.type_train_autorise=tp.nom
WHERE v.id_voyage=1;


-- Le nombre de place restante pour un voyage donné ici =1 à une date donné ici='2023-05-03' et une heure de départ ici = '08:00:00'

SELECT count(*) as nombre_place_occupe,
 tp.nbPlace as nombre_place_disponible,
 tp.nbPlace-count(*) as place_disponible
FROM trajet t
INNER JOIN voyage v ON t.voyage=v.id_voyage
INNER JOIN ligne l ON v.ligne=l.numero
INNER JOIN TypeTrain tp ON l.type_train_autorise=tp.nom
WHERE t.voyage=1 and t.date='2023-05-03' AND v.heureDepart= '08:00:00'
GROUP BY (tp.nbPlace);

-- Les voyages d'un voyageur

SELECT voyage.heureDepart, voyage.ligne,voyage.train
From voyage
JOIN Trajet T on
T.voyage = voyage.id_voyage
JOIN Billet B on
B.idBillet = T.billet
Where B.acheteur ='1 ';   -- id de voyageur

-- Compte le nombre de trajet de un voyageur
Select count(*)
From Trajet T
JOIN Billet B on
T.billet = B.idBillet
Where B.acheteur='1' ; --id de voyageur

-- Compte le nombre de hotels  proche des gare (nombre de transport)
Select count(*)
From HotelProcheDeGare H
GROUP BY(H.nom_gare);


-- Taux de remplissage des trains

select train, (nbPersonnes::float / tt.nbPlace) as "Taux de remplissage"
from vNbPersParTrain nbP join train t on nbP.train = t.numero
    join TypeTrain tt on t.type = tt.nom;


-- Les gares par niveau de fréquentation dans l'ordre décroissant

select nomgare, villegare, count(*) as "frequentation"
from VoyageDessert vd
group by nomgare, villegare
order by count(*) desc;


-- Les lignes les plus empruntées dans l'odre décroissant

select ligne, count(*) as "nb empruntees"
from voyage
group by ligne
order by count(*) desc;

