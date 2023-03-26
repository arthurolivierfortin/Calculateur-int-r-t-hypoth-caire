
import time
import keyboard
from os import listdir


path = "C:/Users/arthu/OneDrive/Calculateurinterethypothecaire/DonneesResultatsImmeubles/"
pathLib = "C:/Users/arthu/OneDrive/Calculateurinterethypothecaire/Lib/"

class Immeuble:

    nomFichier=listdir(path)
            
        
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

class Vérifications:

    pasOk=True
    nom='correct'
    skip=False

####### PAGE INITIAL #######

print("===============================================================")
print("$$$ Calculateur d'Hypothèque -- Par Arthur-Olivier Fortin $$$\n")
print("          pesez sur la barre d'espace pour commencer ")
print("============================================================= \n")


debut = True
while True:
    Vérifications.pasOk=True
    Vérifications.nom='correct'
    i = 0
    if debut:
        def loading():
            i=0
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
        loading()


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
        fraisTotaux = (Hypothèque+(hydro+taxes+autres)*ammortissement)
        adresse = input("Entrez l'adresse du bâtiment\n")
        typeBâtiment = input("Entrez le type du bâtiment\n")

        print('====================================\n')
        print(f"Type d'immeuble : {typeBâtiment}\n")
        print(f"Adresse : {adresse}\n")
        print('====================================\n')
        print("\n")
        print("\n")
        print("\n")
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
            print(f" sommeTotale debourse à date = || {sommeTotale}$ ||\n")
            fraisTotaux-=(fraisAnnuels)
            intérêtsTotale += intérêtsAnnuels
            Hypothèque-=(fraisAnnuelsHypothèque)
            print(f"Somme des intérêts payé à date = || {intérêtsTotale}$ ||")
            print(f"Les intérêts payés lors de l'année {années+1} = || {intérêtsAnnuels}$ ||")
            print(f"Les frais totaux lors de l'année {années+1} = || {(fraisAnnuels)+intérêtsAnnuels}$ ||")
            print(f"Frais restant à payer ((Hypothêque+intérêts Totaux) - montant payé) = || {fraisTotaux}$ ||")

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
                ammortissement = self.amortissement
                hydro = self.hydro
                taxes = self.taxes 
                autres = self.autres
                fraisAnnuelsHypothèque = self.fraisAnnuelHypothèque
                fraisTotaux = self.fraisTotaux
                fraisAnnuels = self.fraisAnnuels
                adresse = self.adresse
                typeBâtiment = self.typeBâtiment

                
                sommeTotale = 0
                intérêtsTotale = 0

                with open(f"{path}{fichier}", "w") as fichier:
                    fichier.write('====================================\n')
                    fichier.write(f"type du Batiment: {typeBâtiment}\n")
                    fichier.write(f"Adresse: {adresse}\n")
                    fichier.write(f"Pour un immeuble de || {PrixLogement}$ || avec une mise de fond de || {MiseDeFond}$ ||:\n")
                    fichier.write(f"L'hypotheque sera de || {HypothèqueDébut}$ ||\n")
                    fichier.write(f"Les payements mensuels sans interets seraient d'une somme de ||{fraisAnnuels/12}$||\n")
                    fichier.write(f"somme totale a rembourser (interet + Hypotheque) = || {sommeTotale}$ ||\n")
                    fichier.write(f"somme totale des interets sur {ammortissement} ans d'ammortissement e rembourser = || {intérêtsTotale}$ ||\n")
                    fichier.write('====================================\n')
                    fichier.write("\n")
                    fichier.write("\n")
                    fichier.write("\n")
                    fichier.write(f"..................................................................\n")
                    fichier.write(f"Hypotheque = || {Hypothèque}$ ||\n")
                    fichier.write(f"interet = || {intérêts}$ ||\n")
                    fichier.write(f"ammortissement = || {ammortissement}$ ||\n")
                    fichier.write(f"frais hydro annuel = || {hydro}$ ||\n")
                    fichier.write(f"taxes annuel = || {taxes}$ ||\n")
                    fichier.write(f"autres frais annuel = || {autres}$ ||\n")
                    fichier.write(f"Frais Annuels (sans les interets)  = || {fraisAnnuels}$ ||\n")
                    fichier.write(f"Frais Mensuels (sans les interets)  = || {fraisAnnuels/12}$ ||\n")
                    fichier.write(f"..................................................................\n")


                    for années in range(ammortissement):
                        fichier.write(f"====== Annee {années+1} ======\n")
                        intérêtsAnnuels = (Hypothèque*intérêts)/(ammortissement)
                        fichier.write(f" InteretsAnnuels = || {intérêtsAnnuels}$ ||\n")
                        sommeTotale+=((fraisAnnuels)+intérêtsAnnuels)
                        fichier.write(f" sommeTotale debourse a date = || {sommeTotale}$ ||\n")
                        fraisTotaux-=(fraisAnnuels)
                        intérêtsTotale += intérêtsAnnuels
                        Hypothèque-=(fraisAnnuelsHypothèque)
                        fichier.write(f"Somme des interets paye e date = || {intérêtsTotale}$ ||\n")
                        fichier.write(f"Les interets payes lors de l'annee {années+1} = || {intérêtsAnnuels}$ ||\n")
                        fichier.write(f"Les frais totaux lors de l'annee {années+1} = || {(fraisAnnuels)+intérêtsAnnuels}$ ||\n")
                        fichier.write(f"Frais restant e payer ((Hypotheque+interets Totaux) - montant paye) = || {fraisTotaux}$ ||\n")
                        fichier.write("\n")
                        fichier.write("\n")
                        fichier.write("\n")
                        fichier.write("\n")
                        fichier.write("\n")
                        fichier.write("\n")
                    fichier.close()

                    listeIntérêts = []
                    listeHypothèque = []
                    with open(f"{pathLib}{fichier}", "w") as fichier:
                        fichier.write(f"['{adresse}', '{typeBâtiment}', '{PrixLogement}', '{MiseDeFond}', '{HypothèqueDébut}', '{fraisAnnuels/12}', '{sommeTotale}', '{intérêtsTotale}']")
                        for années in range(ammortissement):
                            intérêtsAnnuels = (Hypothèque*intérêts)/(ammortissement)
                            intérêtsTotale += intérêtsAnnuels
                            Hypothèque-=(fraisAnnuelsHypothèque)
                            listeIntérêts += intérêtsTotale
                            listeHypothèque += Hypothèque
                        fichier.write(f"{listeIntérêts}")
                        fichier.write(f"{listeHypothèque}")
                    fichier.close()



    def Q_sauvegarder():

        ####### Sauvegarder le fichier dans un fichier texte #######

        def nommerFichier():
            nomFichier = str(input("Quel est le nom que vous voulez donner à votre fichier?\n"))
            return nomFichier
        
        

        def vérifNomFichier(Vérifications):
            while True:
                nomFichier = nommerFichier()
                try:
                    with open(f"{path}{nomFichier}", "x") as fichier:
                        fichier.close()
                    transcrireFichier(nomBâtiment, nomFichier)
                    break
                    
                    
                        
                except(FileExistsError):
                    print(f"Un fichier est déjà exsitant au nom de {nomFichier}, voulez-vous (Pesez sur la touche):\n"
                        "4 - Écraser le fichier existant\n"
                        "5 - Changer le nom du fichier\n")
                    
                    while True:
                        if keyboard.is_pressed("4"):
                            transcrireFichier(nomBâtiment, nomFichier)
                            Vérifications.pasOk = False
                            break
                        
                        if keyboard.is_pressed("5"):
                            break
                        continue

                if Vérifications.pasOk == False:
                    break
            Vérifications.pasOk=True

        vérifNomFichier(Vérifications)
        
        print("Enregistrement .", end="\r")
        time.sleep(0.2)
        print("Enregistrement ..", end="\r")
        time.sleep(0.2)
        print("Enregistrement ...", end="\r")
        time.sleep(0.2)
        print("Enregistrement ....", end="\r")
        time.sleep(0.2)
        print("Enregistrement .....", end="\r")
        time.sleep(0.2)
        print("Fichier Enregistré  ", end="\r")
        time.sleep(0.5)
        print("\n")

            
    ####### Choix d'actions à faire #######

    print("Voulez vous (Pesez sur la touche):\n"
          "1 - Sauvegarder les résultats d'un bâtiment récemment calculés dans un fichier texte\n"
          "2 - Calculer l'hypothèque d'un nouveau bâtiment\n"
          "3 - Calculer...\n"
          "4 - Comparer les résultats de deux ou plusieurs bâtiments\n"
          "5 - Afficher le nom de vos fichier dans votre dossier d'hypothèque d'immeuble\n"
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
            time.sleep(0.2)
            print("\n")
            Q_sauvegarder()
            break
        if keyboard.is_pressed("2"):
            time.sleep(0.2)
            print("\n")
            nomBâtiment = input("Quel est le nom du bâtiment?")
            
            def verifNomClasse(nomBâtiment):
                for i in range(len(Immeuble.nomFichier)):
                    for nom in Immeuble.nomFichier:
                        if nom == nomBâtiment:
                            print(f"Un bâtiment se nomme déjà {nomBâtiment}\n")
                            Vérifications.nom = 'pascorrect'

            if Vérifications.nom != 'correct':
                verifNomClasse(nomBâtiment)

            PrixLogement, MiseDeFond, Hypothèque, HypothèqueDébut, intérêts, ammortissement, hydro, taxes, autres, fraisAnnuelsHypothèque, fraisTotaux, fraisAnnuels, adresse, typeBâtiment = calculer()
            nomBâtiment  = Immeuble(PrixLogement, MiseDeFond, Hypothèque, HypothèqueDébut, intérêts, ammortissement, hydro, taxes, autres, fraisAnnuelsHypothèque, fraisTotaux, fraisAnnuels, adresse, typeBâtiment)
            print("Voulez vous enregistrer le document dans un fichier texte sur votre ordinateur?\n"
                  "1 - Oui\n"
                  "2 - Non\n")
            while True:
                if keyboard.is_pressed("1"):
                    Q_sauvegarder()
                    break
                if keyboard.is_pressed("2"):
                    break
            break
        if keyboard.is_pressed("5"):
            print(Immeuble.nom)
        if i==8:
            i=0
        
        print( dots, end="\r")
        time.sleep(0.1)
        i+=1

    i=0

    

            
    

