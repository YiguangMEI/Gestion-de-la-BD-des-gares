    Notre MLD - G6 :



Par défault, tous les attributs sont NOT NULL, sauf ceux explicitement désignés par NULLABLE

Tables :

    Gare(#nom : STRING, #ville STRING, numeroVoie : SMALLINT, nomRue : STRING, codePostal : STRING[5], zoneHorraire : SMALLINT) 

avec zoneHorraire>=-12 AND zoneHorraire>=12 

    Hotel(#id_Hotel: INT ,nom: STRING, numeroVoie : SMALLINT, nomRue : STRING, codePostal : STRING[5], ville:STRING)


    Transport(#id_Transpot: INT, type: TypeTransport, ville: STRING)


    TypeTrain(#nom: STRING, nbPlace: SMALLINT, vitesseMax: INT, aPremiereClasse: BOOLEAN, coutHeure: FLOAT)

avec nbPlace>=0 AND vitesseMax>=0 AND coutHeure>0

    Ligne(#numero : INT, type=>TypeTrain(nom))

avec numero>=0

    Train(#numero: INT, type=>TypeTrain(nom))

avec numero>=0

    Voyage(#id_Voyage : INTEGER, heureDepart:TIME, train=>Train(numero), ligne=>ligne(numero))


    Plannification(#idPlanification : INT, dateDepart: DATE, dateFin: DATE, lundi: BOOLEAN, mardi: BOOLEAN, mercredi: BOOLEAN, jeudi: BOOLEAN, vendredi: BOOLEAN, samedi: BOOLEAN, dimanche: BOOLEAN)

avec dateDepart < dateFin AND (lundi OR mardi OR mercredi OR jeudi OR vendredi OR samedi OR dimanche)

    JourException(#jour: DATE, ajout: BOOLEAN)


    StatutCarte(#intitulé : string)


    Voyageur(#idVoyageur : INTEGER, nom : STRING, prenom : STRING, numeroVoie : SMALLINT, nomRue : STRING, codePostal : STRING[5], tel : string, numeroCarte: INT, statut =>StatutCarte(intitulé))

avec tel UNIQUE, numeroCarte NULLABLE UNIQUE, statut NULLABLE, ((numeroCarte IS NULL AND statut IS NULL) OR (numeroCarte IS NOT NULL AND statut IS NOT NULL))

    TypePaiment(#intitulé : STRING)


    Billet(#idBillet : INTEGER, assurance : BOOL, acheteur=> Voyageur(idVoyageur), typePaiement=> TypePaiment(intitulé)) 


    Trajet(#billet=>Billet, #numeroTrajet: INTEGER, numeroPlace: SMALLINT, prix: FLOAT)

avec numeroPlace>=0 AND numeroTrajet>=0

Tables associations : 
pour les association N:M, il nous faut créer de nouvelles tables 

    Transportdessert(#transport=>Transport, #nom_gare=>Gare.nom, #ville_gare=>Gare=>ville)


    estProche(#hotel=>Hotel, #nom_gare=>Gare(nom), #ville_gare=>Gare(ville))


    LigneDessert(#nomGare=>Gare(nom), #villeGare=>Gare(ville), #ligne=>Ligne, ordre:INTEGER)

avec ordre>=0 et UNIQUE (ligne, ordre)

    VoyageDessert(#voyage=>Voyage,#nomGare=>Gare(nom), #villeGare=>Gare(ville), ,heureDepart:TIME,heureArrivee:TIME)


    Impacte(#planification=>Planification.idPlanification, #jour=>JourException)


    Planifie(#voyage=>Voyage,#dateDepart=>Plannification.dateDepart,#dateFin=>Plannification.dateFin)


Vues : 

    VvoyageurRégylier=Projection(Restriction(Voyageur, statut IS NOT NULL) idVoyageur, nom, prenom, numeroVoie, nomRue, codePostal, tel, numeroCarte, statut)

    VvoyageurOccasionnel=Projection(Restriction(Voyageur, statut IS NOT NULL) idVoyageur, nom, prenom, numeroVoie, nomRue, codePostal, tel)


Contraintes supplémentaires : 

    {Contrainte 1:N Voyageur-Billet}

    - projection(voyageur, idVoyageur) = projection(Billet, acheteur)


    {Contrainte N:1 Voyage-Ligne}

    - projection(voyage, ligne) = projection(ligne, numero)


    {Contrainte N:1 Train-TypeTrain}

    - projection(train, type) = projection(typeTrain, nom)


    {Contrainte N:1 Ligne-TypeTrain}

    - projection(ligne, type) = projection(typeTrain, nom)


    {Contrainte N:N Gare-Hotel}

    - projection(Hotel, id_hotel) = projection(AssocGareHotel, hotel)

    - projection(Gare, nom, ville) = projection(est_proche, nom_gare, ville_gare)


    {Contrainte N:N Gare-Transport}

    - projection(Transport, id_transport) = projection(TransportDessert, transport)

    - projection(Gare, nom, ville) = projection(TransportDessert, nom_gare, ville_gare)


    {Contrainte 1:N Billet-Trajet}

    - projection(billet, idBillet) = projection(trajet, billet)


    {Contrainte N:N Ligne-Gare}

    - projection(Gare, nom, ville) = projection(LigneDessert, nomGare, villeGare)

    -projection(Ligne, numero)= projection(LigneDessert, ligne)




    Contraintes plus complexes :


    - un voyage doit être lié à au moins 2 gares (peut être représenté par 2 clés étrangères dans voyage)

    - une ligne doit desservir au moins 2 gares (peut être représenté par 2 clés étrangères dans ligne)



Justification de l'héritage
1. La classe mère n'est pas abstrait, il sera ainsi nécessaire d'instancier des voyageurs qui ne sont pas réguliers(dits occasionnels)
2. L'héritage est presque complet, la classe fille ne posède que deux attributs supplémentaires
3. La classe mère a des associations générales, la classe fille n'a pas d'association particulère

A la lumière de ces informations,  la méthode la plus satisfaisante pour un passage au MLD semble être un héritage par la classe mère. 


Justification des clefs :

    Hôtel :


    Ligne : il nous a semble cohérent que chaque ligne ait numéro unique et NOT NULL, ce n'est pas simplement une clef artificielle, car elle a aussi un rôle pour les usagers du site qui peuvent se référer au numéro de ligne.


    Transport : 


    Voyage :


    Voyageur : un numéro de téléphone est certes unique et non nulle, il n'est cependant pas immuable pour un même voyageur, la clef artificielle semble se dessiner comme la meilleur option
