import keyboard
import time

nom = ""
def nommer():
    nom = input("Nommer une personne")
    return nom


while True:
    if keyboard.is_pressed("SPACE"):
        time.sleep(0.5)
        nom = nommer()
        print(nom)
        break

    

