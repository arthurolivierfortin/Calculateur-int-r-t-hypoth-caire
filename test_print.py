PrixLogement = float(214000)#float(input("Entrez le prix du logement (sans le signe de dollars)\n"))
        MiseDeFond = float(75000)#float(input("Entrez la mise de fond (sans le signe de dollars)\n"))
        Hypothèque=(PrixLogement)-MiseDeFond
        HypothèqueDébut = Hypothèque
        intérêts = float(5.89)#float(input("Entré le pourcentage d'intérêts (sans le signe de %)\n"))
        intérêts /= 10
        ammortissement = int(25)#int(input("Entrez le nombre d'années d'ammortissement\n"))
        hydro = float(800)#float(input("Entrez les frais annuels d'hydro (sans le signee de dollars)\n"))
        taxes = float(1545)#float(input("Entrez les frais annuels de taxes (sans le signe de dollars)\n"))
        autres = float(2012)#float(input('''Entrez les frais annuels "autres" (sans le signee de dollars)\n'''))
        fraisAnnuelsHypothèque = (Hypothèque/25)
        fraisTotaux = (Hypothèque+(hydro+taxes+autres)*ammortissement)
        adresse = "225 Avenue Godefroy"#input("Entrez l'adresse du bâtiment\n")
        typeBâtiment = "maison"#input("Entrez le type du bâtiment\n")
 