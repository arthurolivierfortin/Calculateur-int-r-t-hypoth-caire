
import time
import keyboard

class Immeuble:

    dicNom = []
    def __init__(self, PrixLogement, MiseDeFond, Hypothèque, HypothèqueDébut, intérêts, ammortissement, hydro, taxes, autres, fraisAnnuelsHypothèque, fraisTotaux, fraisAnnuels, adresse, typeBâtiment):
        self.PrixLogement = PrixLogement
        self.MiseDeFond = MiseDeFond
        self.Hypothèque = Hypothèque
        self.HypothèqueDébut = HypothèqueDébut
        self.intérêts = intérêts
        self.amortissement = ammortissement
        self.hydro = hydro
        self.taxes = taxes
        self.autres = autres
        self.fraisAnnuelHypothèque = fraisAnnuelsHypothèque
        self.fraisTotaux = fraisTotaux
        self.fraisAnnuels = fraisAnnuels
        self.adresse = adresse
        self.typeBâtiment = typeBâtiment

####### PAGE INITIAL #######

print("===============================================================")
print("$$$ Calculateur d'Hypothèque -- Par Arthur-Olivier Fortin $$$\n")
print("          pesez sur la barre d'espace pour commencer ")
print("============================================================= \n")


debut = True
while True:
    nom = 'pas correct'
    pasOk = True
    i = 0
    if debut:
        while True:
            
            if i ==0:
                dots="...."
            if i ==1:
                dots="...°"
            if i ==2:
                dots="..°°"
            if i ==3:
                dots=".°°."
            if i ==4:
                dots="°°.."
            if i ==5:
                dots="°..."
            if i ==6:
                dots="...."
            if i ==7:
                dots="...."
            if i ==8:
                dots="...."
            if keyboard.is_pressed("space"):
                time.sleep(0.2)
                break
            if i==8:
                i=0
            
            print( dots, end="\r")
            time.sleep(0.1)
            i+=1

        i=0
        debut=False


    def calculer():
        PrixLogement = float(214000)#float(input("Entrez le prix du logement (sans le signe de dollars)\n"))
        MiseDeFond = float(75000)#float(input("Entrez la mise de fond (sans le signe de dollars)\n"))
        Hypothèque=(PrixLogement)-MiseDeFond
        HypothèqueDébut = Hypothèque
        intérêts = float(5.89)#float(input("Entré le pourcentage d'intérêts (sans le signe de %)\n"))
        intérêts /= 10
        ammortissement = int(25)#int(input("Entrez le nombre d'années d'ammortissement\n"))
        hydro = float(2012)#float(input("Entrez les frais annuels d'hydro (sans le signee de dollars)\n"))
        taxes = float(1545)#float(input("Entrez les frais annuels de taxes (sans le signe de dollars)\n"))
        autres = float(500)#float(input('''Entrez les frais annuels "autres" (sans le signee de dollars)\n'''))
        fraisAnnuelsHypothèque = (Hypothèque/25)
        fraisTotaux = (Hypothèque+(hydro+taxes+autres)*ammortissement)
        adresse = "1110 Rue de paris"#input("Entrez l'adresse du bâtiment\n")
        typeBâtiment = "Maison"#input("Entrez le type du bâtiment\n")

        print(f"............\n")
        print()
        print(f"Hypothèque = || {Hypothèque}$ ||\n")
        print(f"intérêt = || {intérêts}$ ||\n")
        print(f"ammortissement = || {ammortissement}$ ||\n")
        print(f"frais hydro annuel = || {hydro}$ ||\n")
        print(f"taxes annuel = || {taxes}$ ||\n")
        print(f"autres frais annuel = || {autres}$ ||\n")



        sommeTotale = 0
        fraisAnnuels = (((Hypothèque/ammortissement)+hydro+taxes+autres))
        intérêtsTotale = 0

        print(f"Frais Annuels (sans les intérêts)  = || {fraisAnnuels}$ ||\n")
        print(f"Frais Mensuels (sans les intérêts)  = || {fraisAnnuels/12}$ ||\n")
        print(f".............\n")


        for années in range(ammortissement):
            print(f"====== Année {années+1} ======")
            intérêtsAnnuels = (Hypothèque*intérêts)/(ammortissement)
            print(f" IntérêtsAnnuels = || {intérêtsAnnuels}$ ||\n")
            sommeTotale+=((fraisAnnuels)+intérêtsAnnuels)
            print(f" sommeTotale déboursé à date = || {sommeTotale}$ ||\n")
            fraisTotaux-=(fraisAnnuels)
            intérêtsTotale += intérêtsAnnuels
            Hypothèque-=(fraisAnnuelsHypothèque)
            print(f"Somme des intérêts payé à date = || {intérêtsTotale}$ ||")
            print(f"Les intérêts payés lors de l'année {années+1} = || {intérêtsAnnuels}$ ||")
            print(f"Les frais totaux lors de l'année {années+1} = || {(fraisAnnuels)+intérêtsAnnuels}$ ||")
            print(f"Frais restant à payer ((Hypothèque+intérêts Totaux) - montant payé) = || {fraisTotaux}$ ||")

        print(" ======== Résultats : ")
        print(f"type du Bâtiment: {typeBâtiment}")
        print(f"Adresse: {adresse}\n")
        print(f"Pour un immeuble de || {PrixLogement}$ || avec une mise de fond de || {MiseDeFond}$ ||:")
        print(f"L'hypothèque sera de || {HypothèqueDébut}$ ||")
        print(f"Les payements mensuels sans intérêts seraient d'une somme de ||{fraisAnnuels/12}$||")
        print(f"somme totale à rembourser (intérêt + Hypothèque) = || {sommeTotale}$ ||")
        print(f"somme totale des intérêts sur {ammortissement} ans d'ammortissement à rembourser = || {intérêtsTotale}$ ||")
        print("===========")
        return(PrixLogement, MiseDeFond, Hypothèque, HypothèqueDébut, intérêts, ammortissement, hydro, taxes, autres, fraisAnnuelsHypothèque, fraisTotaux, fraisAnnuels, adresse, typeBâtiment)
        
    def transcrireFichier(self, fichier):
                PrixLogement = self.PrixLogement
                MiseDeFond = self.MiseDeFond
                Hypothèque = self.Hypothèque
                HypothèqueDébut = self.HypothèqueDébut
                intérêts = self.intérêts 
                ammortissement = self.ammortissement
                hydro = self.hydro
                taxes = self.taxes 
                autres = self.autres
                fraisAnnuelsHypothèque = self.fraisAnnuelsHypothèque
                fraisTotaux = self.fraisTotaux
                fraisAnnuels = self.fraisAnnuels
                adresse = self.adresse
                typeBâtiment = self.typeBâtiment

                
                sommeTotale = 0
                intérêtsTotale = 0

                with open(fichier, "w") as fichier:
                    fichier.write(f"............\n")
                    fichier.write(f"Hypothèque = || {Hypothèque}$ ||\n")
                    fichier.write(f"intérêt = || {intérêts}$ ||\n")
                    fichier.write(f"ammortissement = || {ammortissement}$ ||\n")
                    fichier.write(f"frais hydro annuel = || {hydro}$ ||\n")
                    fichier.write(f"taxes annuel = || {taxes}$ ||\n")
                    fichier.write(f"autres frais annuel = || {autres}$ ||\n")


                    fichier.write(f"Frais Annuels (sans les intérêts)  = || {fraisAnnuels}$ ||\n")
                    fichier.write(f"Frais Mensuels (sans les intérêts)  = || {fraisAnnuels/12}$ ||\n")
                    fichier.write(f".............\n")


                    for années in range(ammortissement):
                        fichier.write(f"====== Année {années+1} ======")
                        intérêtsAnnuels = (Hypothèque*intérêts)/(ammortissement)
                        fichier.write(f" IntérêtsAnnuels = || {intérêtsAnnuels}$ ||\n")
                        sommeTotale+=((fraisAnnuels)+intérêtsAnnuels)
                        fichier.write(f" sommeTotale déboursé à date = || {sommeTotale}$ ||\n")
                        fraisTotaux-=(fraisAnnuels)
                        intérêtsTotale += intérêtsAnnuels
                        Hypothèque-=(fraisAnnuelsHypothèque)
                        fichier.write(f"Somme des intérêts payé à date = || {intérêtsTotale}$ ||")
                        fichier.write(f"Les intérêts payés lors de l'année {années+1} = || {intérêtsAnnuels}$ ||")
                        fichier.write(f"Les frais totaux lors de l'année {années+1} = || {(fraisAnnuels)+intérêtsAnnuels}$ ||")
                        fichier.write(f"Frais restant à payer ((Hypothèque+intérêts Totaux) - montant payé) = || {fraisTotaux}$ ||")

                    fichier.write(" ======== Résultats : ")
                    fichier.write(f"type du Bâtiment: {typeBâtiment}")
                    fichier.write(f"Adresse: {adresse}\n")
                    fichier.write(f"Pour un immeuble de || {PrixLogement}$ || avec une mise de fond de || {MiseDeFond}$ ||:")
                    fichier.write(f"L'hypothèque sera de || {HypothèqueDébut}$ ||")
                    fichier.write(f"Les payements mensuels sans intérêts seraient d'une somme de ||{fraisAnnuels/12}$||")
                    fichier.write(f"somme totale à rembourser (intérêt + Hypothèque) = || {sommeTotale}$ ||")
                    fichier.write(f"somme totale des intérêts sur {ammortissement} ans d'ammortissement à rembourser = || {intérêtsTotale}$ ||")
                    fichier.write("===========")
                    fichier.close()




    def Q_sauvegarder():

        ####### Sauvegarder le fichier dans un fichier texte #######

        def nommerFichier():
            nomFichier = str(input("Quel est le nom que vous voulez donner à votre fichier?\n"))
            return nomFichier
        
        nomFichier = nommerFichier()

        def vérifNomFichier(nomFichier):
            try:
                with open(nomFichier, "x") as fichier:
                    fichier.close()
                pasOk = False
                transcrireFichier(Immeuble, nomFichier)
                
                    
            except(FileExistsError):
                pasOk = True
                print(f"Un fichier est déjà exsitant au nom de {nomFichier}, voulez-vous:"
                    "1 - Écraser le fichier existant\n"
                    "2 - Changer le nom du fichier\n")
                
                while True:
                    if keyboard.is_pressed("1"):
                            transcrireFichier(Immeuble, nomFichier)
                    if keyboard.is_pressed("2"):
                        nomFichier = nommerFichier()
                        vérifNomFichier(nomFichier)
        if pasOk:
            vérifNomFichier(nomFichier)

            
    ####### Choix d'actions à faire #######

    print("Voulez vous:\n"
          "1 - Calculer l'hypothèque d'un bâtiment\n"
          "2 - Calculer...\n"
          "ESCAPE - Quitter l'application\n")
    
    while True:
        
        if i ==0:
            dots="...."
        if i ==1:
            dots="...°"
        if i ==2:
            dots="..°°"
        if i ==3:
            dots=".°°."
        if i ==4:
            dots="°°.."
        if i ==5:
            dots="°..."
        if i ==6:
            dots="...."
        if i ==7:
            dots="...."
        if i ==8:
            dots="...."
    
        if keyboard.is_pressed("1"):
            print("\n")
            nomBâtiment = input("Quel est le nom du bâtiment?")
            
            def verifNomClasse(nomBâtiment):
                for i in range(len(Immeuble.dicNom)):
                    for nom in Immeuble.dicNom:
                        if nom == nomBâtiment:
                            print(f"Un bâtiment se nomme déjà {nomBâtiment}\n")
            if nom != 'correct':
                verifNomClasse(nomBâtiment)

            PrixLogement, MiseDeFond, Hypothèque, HypothèqueDébut, intérêts, ammortissement, hydro, taxes, autres, fraisAnnuelsHypothèque, fraisTotaux, fraisAnnuels, adresse, typeBâtiment = calculer()
            nomBâtiment  = Immeuble(PrixLogement, MiseDeFond, Hypothèque, HypothèqueDébut, intérêts, ammortissement, hydro, taxes, autres, fraisAnnuelsHypothèque, fraisTotaux, fraisAnnuels, adresse, typeBâtiment)

            print("Voulez-vous enregistrez le document?\n"
                  "ENTER - Oui\n"
                  "ESC - Non\n")
            if keyboard.is_pressed("ENTER"):
                print("\n")
                Q_sauvegarder()
            if keyboard.is_pressed("ESC"):
                break
            break

        if i==8:
            i=0
        
        print( dots, end="\r")
        time.sleep(0.1)
        i+=1

    i=0

    

            
    

