from os import listdir

Libr = "C:/Users/arthu/OneDrive/Calculateurinterethypothecaire/Lib"
listeNom = listdir(Libr)
print(listeNom)
print("\n")
dicImmeuble = {}
i=0
for i in range(len(listeNom)):
    nom = listeNom[i]
    dicImmeuble[f"{nom}"]={}
    print("\n")
    print(nom)
    print("\n")
    with open(f"{Libr}/{nom}", "r") as LibDonnées:
            données = LibDonnées.readlines()
            dicImmeuble[f"{nom}"]["adresse"]=str(données[0])
            dicImmeuble[f"{nom}"]["adresse"]=dicImmeuble[f"{nom}"]["adresse"][0:(len(dicImmeuble[f"{nom}"]["adresse"])-1)]
            dicImmeuble[f"{nom}"]["typeBâtiment"]=str(données[1])
            dicImmeuble[f"{nom}"]["typeBâtiment"]=dicImmeuble[f"{nom}"]["typeBâtiment"][0:(len(dicImmeuble[f"{nom}"]["typeBâtiment"])-1)]
            dicImmeuble[f"{nom}"]["PrixLogement"]=float(données[2])
            dicImmeuble[f"{nom}"]["MiseDeFond"]=float(données[3])
            dicImmeuble[f"{nom}"]["HypothèqueDébut"]=float(données[4])
            dicImmeuble[f"{nom}"]["fraisMensuels"]=float(données[5])
            dicImmeuble[f"{nom}"]["sommeTotale"]=float(données[6])
            dicImmeuble[f"{nom}"]["intérêtsTotales"]=float(données[7])
            dicImmeuble[f"{nom}"]["ListeIntérêtsTotalePayés"]=[]
            dicImmeuble[f"{nom}"]["ListeHypothèqueRestant"]=[]

            for i in range(50):
                i+=8
                if (i%2)==0:
                    dicImmeuble[f"{nom}"]["ListeIntérêtsTotalePayés"]+=[float(données[i])]
                if (i%2)!=0:
                    dicImmeuble[f"{nom}"]["ListeHypothèqueRestant"]+=[float(données[i])]
            

            
            LibDonnées.close()

print("===========\n")  
print(dicImmeuble)
    #f"['{adresse}', '{typeBâtiment}', '{PrixLogement}', '{MiseDeFond}', '{HypothèqueDébut}', '{fraisAnnuels/12}', '{sommeTotale}', '{intérêtsTotale}']\n")
    #listeIntérêts += [intérêtsTotale]
    #                        listeHypothèque += [Hypothèque]
