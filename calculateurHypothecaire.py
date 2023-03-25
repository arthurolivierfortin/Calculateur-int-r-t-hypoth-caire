
import time
import keyboard

class Immeuble:

    def __init__(self, PrixLogement, MiseDeFond, Hypothèque, HypothèqueDébut, intérêts, ammortissement, hydro, taxes, autres, fraisAnnuelsHypothèque, fraisTotaux, fraisAnnuels):
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

####### PAGE INITIAL #######

print("===============================================================")
print("$$$ Calculateur d'Hypothèque -- Par Arthur-Olivier Fortin $$$\n")
print("          pesez sur la barre d'espace pour commencer ")
print("============================================================= \n")

debut = True
while True:
    
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
                break
            if i==8:
                i=0
            
            print( dots, end="\r")
            time.sleep(0.1)
            i+=1

        i=0


    def calculer():
        PrixLogement = float(input("Entrez le prix du logement (sans le signe de dollars)\n"))
        MiseDeFond = float(input("Entrez la mise de fond (sans le signe de dollars)\n"))
        Hypothèque=(PrixLogement)-MiseDeFond
        HypothèqueDébut = Hypothèque
        intérêts = float(input("Entré le pourcentage d'intérêts (sans le signe de %)\n"))
        intérêts /= 10
        ammortissement = int(input("Entrez le nombre d'années d'ammortissement\n"))
        hydro = float(input("Entrez les frais annuels d'hydro (sans le signee de dollars)\n"))
        taxes = float(input("Entrez les frais annuels de taxes (sans le signe de dollars)\n"))
        autres = float(input('''Entrez les frais annuels "autres" (sans le signee de dollars)\n'''))
        fraisAnnuelsHypothèque = (Hypothèque/25)
        fraisTotaux = (Hypothèque+(+hydro+taxes+autres)*ammortissement)

        print(f"............\n")
        print(f"Hypothèque = || {Hypothèque}$ ||\n")
        print(f"intérêt = || {intérêts}$ ||\n")
        print(f"ammortissement = || {ammortissement}$ ||\n")
        print(f"hydro = || {hydro}$ ||\n")
        print(f"taxes = || {taxes}$ ||\n")
        print(f"autres = || {autres}$ ||\n")



        sommeTotale = 0
        fraisAnnuels = (((Hypothèque/ammortissement)+hydro+taxes+autres))
        intérêtsTotale = 0

        print(f"Frais Annuels (sans les intérêts)  = || {fraisAnnuels}$ ||\n")
        print(f"Frais Mensuels (sans les intérêts)  = || {fraisAnnuels/12}$ ||\n")
        print(f".............\n")


        for i in range(ammortissement):
            print(f"====== Année {i+1} ======")
            intérêtsAnnuels = (Hypothèque*intérêts)/(ammortissement)
            print(f" IntérêtsAnnuels = || {intérêtsAnnuels}$ ||\n")
            sommeTotale+=((fraisAnnuels)+intérêtsAnnuels)
            print(f" sommeTotale déboursé à date = || {sommeTotale}$ ||\n")
            fraisTotaux-=(fraisAnnuels)
            intérêtsTotale += intérêtsAnnuels
            Hypothèque-=(fraisAnnuelsHypothèque)
            print(f"Somme des intérêts payé à date = || {intérêtsTotale}$ ||")
            print(f"Les intérêts payés lors de l'année {i+1} = || {intérêtsAnnuels}$ ||")
            print(f"Les frais totaux lors de l'année {i+1} = || {(fraisAnnuels)+intérêtsAnnuels}$ ||")
            print(f"Frais restant à payer ((Hypothèque+intérêts Totaux) - montant payé) = || {fraisTotaux}$ ||")

        print(" ======== Résultats : ")
        print(f"Pour un immeuble de || {PrixLogement}$ || avec une mise de fond de || {MiseDeFond}$ ||:")
        print(f"L'hypothèque sera de || {HypothèqueDébut}$ ||")
        print(f"Les payements mensuels sans intérêts seraient d'une somme de ||{fraisAnnuels/12}$||")
        print(f"somme totale à rembourser (intérêt + Hypothèque) = || {sommeTotale}$ ||")
        print(f"somme totale des intérêts sur {ammortissement} ans d'ammortissement à rembourser = || {intérêtsTotale}$ ||")
        print("===========")
        return(PrixLogement, MiseDeFond, Hypothèque, HypothèqueDébut, intérêts, ammortissement, hydro, taxes, autres, fraisAnnuelsHypothèque, fraisTotaux, fraisAnnuels)
        
    def transcrireFichier(fichier, PrixLogement, MiseDeFond, Hypothèque, HypothèqueDébut, intérêts, ammortissement, hydro, taxes, autres, fraisAnnuelsHypothèque, fraisTotaux, fraisAnnuels):
                sommeTotale = 0
                intérêtsTotale = 0

                fichier.write(f"............\n")
                fichier.write(f"Hypothèque = || {Hypothèque}$ ||\n")
                fichier.write(f"intérêt = || {intérêts}$ ||\n")
                fichier.write(f"ammortissement = || {ammortissement}$ ||\n")
                fichier.write(f"hydro = || {hydro}$ ||\n")
                fichier.write(f"taxes = || {taxes}$ ||\n")
                fichier.write(f"autres = || {autres}$ ||\n")


                fichier.write(f"Frais Annuels (sans les intérêts)  = || {fraisAnnuels}$ ||\n")
                fichier.write(f"Frais Mensuels (sans les intérêts)  = || {fraisAnnuels/12}$ ||\n")
                fichier.write(f".............\n")


                for i in range(ammortissement):
                    fichier.write(f"====== Année {i+1} ======")
                    intérêtsAnnuels = (Hypothèque*intérêts)/(ammortissement)
                    fichier.write(f" IntérêtsAnnuels = || {intérêtsAnnuels}$ ||\n")
                    sommeTotale+=((fraisAnnuels)+intérêtsAnnuels)
                    fichier.write(f" sommeTotale déboursé à date = || {sommeTotale}$ ||\n")
                    fraisTotaux-=(fraisAnnuels)
                    intérêtsTotale += intérêtsAnnuels
                    Hypothèque-=(fraisAnnuelsHypothèque)
                    fichier.write(f"Somme des intérêts payé à date = || {intérêtsTotale}$ ||")
                    fichier.write(f"Les intérêts payés lors de l'année {i+1} = || {intérêtsAnnuels}$ ||")
                    fichier.write(f"Les frais totaux lors de l'année {i+1} = || {(fraisAnnuels)+intérêtsAnnuels}$ ||")
                    fichier.write(f"Frais restant à payer ((Hypothèque+intérêts Totaux) - montant payé) = || {fraisTotaux}$ ||")

                fichier.write(" ======== Résultats : ")
                fichier.write(f"Pour un immeuble de || {PrixLogement}$ || avec une mise de fond de || {MiseDeFond}$ ||:")
                fichier.write(f"L'hypothèque sera de || {HypothèqueDébut}$ ||")
                fichier.write(f"Les payements mensuels sans intérêts seraient d'une somme de ||{fraisAnnuels/12}$||")
                fichier.write(f"somme totale à rembourser (intérêt + Hypothèque) = || {sommeTotale}$ ||")
                fichier.write(f"somme totale des intérêts sur {ammortissement} ans d'ammortissement à rembourser = || {intérêtsTotale}$ ||")
                fichier.write("===========")
                fichier.clode()




    def Q_sauvegarder():

        ####### Sauvegarder le fichier dans un fichier texte #######

        def nommerFichier():
            nomFichier = str(input("Quel est le nom que vous voulez donner à votre fichier?\n"))
            return nomFichier
        
        nomFichier = nommerFichier()

        def vérifNomFichier():
            try:
                with open(nomFichier, 'x') as fichier:
                    transcrireFichier(fichier, PrixLogement, MiseDeFond, Hypothèque, HypothèqueDébut, intérêts, ammortissement, hydro, taxes, autres, fraisAnnuelsHypothèque, fraisTotaux, fraisAnnuels)
                
                    
            except(FileExistsError):
                print(f"Un fichier est déjà exsitant au nom de {nomFichier}, voulez-vous:"
                    "1 - Écraser le fichier existant\n"
                    "2 - Changer le nom du fichier\n")
                
                while True:
                    if keyboard.is_pressed("1"):
                        with open(nomFichier, 'w') as fichier:
                            transcrireFichier(fichier, PrixLogement, MiseDeFond, Hypothèque, HypothèqueDébut, intérêts, ammortissement, hydro, taxes, autres, fraisAnnuelsHypothèque, fraisTotaux, fraisAnnuels)
                    if keyboard.is_pressed("2"):
                        NomFichier = nommerFichier()
                        vérifNomFichier()
            
    ####### Choix d'actions à faire #######

    print("Voulez vous:\n"
          "1 - Sauvegarder le document"
          "2 - Calculer l'hypothèque d'un bâtiment"
          "3 - Calculer..."
          "ESCAPE - Quitter l'application")
    
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
            Q_sauvegarder()
            break
        if keyboard.is_pressed("2"):
            Immeuble  = (PrixLogement, MiseDeFond, Hypothèque, HypothèqueDébut, intérêts, ammortissement, hydro, taxes, autres, fraisAnnuelsHypothèque, fraisTotaux, fraisAnnuels) = calculer()
            break
        if i==8:
            i=0
        
        print( dots, end="\r")
        time.sleep(0.1)
        i+=1

    i=0

    

            
    

