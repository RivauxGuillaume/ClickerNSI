import time
from tkinter import Tk, Canvas, Label, Button
import threading


#----------------------------------------------------------------Fonction---------------------------------------------------------------------------


def creer_fenetre():
    fenetre=Tk()
    fenetre.title("Clicker")
    return fenetre


def creer_button():
    bouton_clicker = Button(fenetre, text="Clique !!!", width=50, height=20, bg="black",bd=0, activebackground="black", command=AjoutScore)
    bouton_clicker.grid(row=5, column=5)
    #Création des différents bouton d'améliorations
    Amelioration1Button = Button(fenetre, text="Acheter", width=10, height=1, bg="white", command=Amelioration1Clic)
    Amelioration1Button.grid(row=1, column=14)

    Amelioration2Button = Button(fenetre, text="Acheter", width=10, height=1, bg="white", command=Amelioration2Clic)
    Amelioration2Button.grid(row=2, column=14)
    return bouton_clicker, Amelioration1Button, Amelioration2Button


def creer_text():
    # Création des différents textes d'améliorations
    Amelioration1Text=Label(fenetre, text=f"Amelioration 1 :  {prix1} truc", bg="black", fg="white")
    Amelioration1Text.grid(row=1, column=13)

    Amelioration2Text=Label(fenetre, text=f"Amelioration 1 :  {prix2} truc", bg="black", fg="white")
    Amelioration2Text.grid(row=2, column=13)
    # Création du texte du score
    texte_score=Label(fenetre, text=f"{score} truc", bg="black", fg="white")
    texte_score.grid(row=0, column=5)
    # Création du nb de clic
    texte_scoreClick=Label(fenetre, text=f"{scoreClick} truc/Clic", bg="black", fg="white")
    texte_scoreClick.grid(row=1, column=5)
    # Création du texte du score/sec
    texte_clicSec=Label(fenetre, text=f"{scoreSec} truc/Clic", bg="black", fg="white")
    texte_clicSec.grid(row=2, column=5)


    return Amelioration1Text, Amelioration2Text, texte_score, texte_clicSec, texte_scoreClick


def creer_Canvas():
    zone_graphique = Canvas(fenetre, width=900, height=500, bg='black')
    zone_graphique.grid(row=0, column=0, rowspan=15, columnspan=15)
    return zone_graphique


def AjoutScore():
    global score
    score=score+scoreClick                                  # A modifier
    #Maj du score sur l'HUD
    texte_score.configure(text=f"{score} truc")


def MajScoreSec():
    global score
    t = 0
    while t==0:
        time.sleep(1)
        score=score+scoreSec
        texte_score.configure(text=f"{score} truc")


def Amelioration1Clic():
    global scoreClick
    global score
    if score >= 10:                                         # A modifier
        scoreClick=scoreClick+1                             # A modifier
        texte_scoreClick.configure(text=f"{scoreClick} truc/Clic")
        score=score-10                                      # A modifier
        texte_score.configure(text=f"{score} truc")


def Amelioration2Clic():
    global scoreSec
    global score
    if score >= 100:                                         # A modifier
        scoreSec=scoreSec+1                                  # A modifier
        texte_clicSec.configure(text=f"{scoreSec} truc/Clic")
        score=score-100                                      # A modifier
        texte_score.configure(text=f"{score} truc")


def Amelioration3Clic():
    global scoreClick
    global score
    if score >= 1000:                                         # A modifier
        scoreClick=scoreClick+100                             # A modifier
        texte_scoreClick.configure(text=f"{scoreClick} truc/Clic")
        score=score-1000                                      # A modifier
        texte_score.configure(text=f"{score} truc")


#----------------------------------------------------------------Main-----------------------------------------------------------------------------

scoreClick=1
scoreSec=0
prix1=10
prix2=100
score=0


fenetre=creer_fenetre()
zone_graphique=creer_Canvas()
bouton_clicker, Amelioration1Button, Amelioration2Button=creer_button()

Amelioration1Text, Amelioration2Text, texte_score, texte_clicSec, texte_scoreClick=creer_text()

# Gestion du multithread pour les clic/sec
th1=threading.Thread(target=MajScoreSec)
th1.start()


fenetre.mainloop()





