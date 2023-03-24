import time
import keyboard


i=0

print("===============================================================")
print("$$$ Calculateur d'Hypothèque -- Par Arthur-Olivier Fortin $$$\n")
print("          pesez sur la barre d'espace pour commencer ")
print("============================================================= \n")
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
 