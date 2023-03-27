from os import listdir


Lib = "C:/Users/arthu/OneDrive/Calculateurinterethypothecaire/Lib"
listeNom = listdir(Lib)
dicImmeuble = {}
for nom in listeNom:
    with open(f"{Lib}/{nom}", "r") as LibDonnées:
            données = LibDonnées.readlines()
            dicImmeuble["adresse"]=str(données[0])
            dicImmeuble["adresse"]=dicImmeuble["adresse"][0:(len(dicImmeuble["adresse"])-1)]
            dicImmeuble["typeBâtiment"]=str(données[1])
            dicImmeuble["typeBâtiment"]=dicImmeuble["typeBâtiment"][0:(len(dicImmeuble["typeBâtiment"])-1)]
            dicImmeuble["PrixLogement"]=float(données[2])
            dicImmeuble["MiseDeFond"]=float(données[3])
            dicImmeuble["HypothèqueDébut"]=float(données[4])
            dicImmeuble["fraisMensuels"]=float(données[5])
            dicImmeuble["sommeTotale"]=float(données[6])
            dicImmeuble["intérêtsTotales"]=float(données[7])
            dicImmeuble["ListeIntérêtsTotalePayés"]=[]
            dicImmeuble["ListeHypothèqueRestant"]=[]

            for i in range(50):
                i+=8
                if (i%2)==0:
                    dicImmeuble["ListeIntérêtsTotalePayés"]+=[float(données[i])]
                if (i%2)!=0:
                    dicImmeuble["ListeHypothèqueRestant"]+=[float(données[i])]
                
            
                  
            
            print(dicImmeuble)
            

    #f"['{adresse}', '{typeBâtiment}', '{PrixLogement}', '{MiseDeFond}', '{HypothèqueDébut}', '{fraisAnnuels/12}', '{sommeTotale}', '{intérêtsTotale}']\n")
    #listeIntérêts += [intérêtsTotale]
    #                        listeHypothèque += [Hypothèque]
