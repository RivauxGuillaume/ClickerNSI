
from tkinter import Tk, Canvas, Label, Button

#----------------------------------------------------------------Fonction---------------------------------------------------------------------------


def creer_fenetre():
    fenetre=Tk()
    fenetre.title("Clicker")
    return fenetre


def creer_widgets():
    zone_graphique = Canvas(fenetre, width=900, height=500, bg='black')
    zone_graphique.grid(row=0, column=0, rowspan=15, columnspan=15)

    bouton_clicker = Button(fenetre, text="Clique !!!", width=50, height=20, bg="black",bd=0, activebackground="black", command=AjoutScore)
    bouton_clicker.grid(row=5, column=5)

    Amelioration1Button = Button(fenetre, text="Acheter", width=10, height=1, bg="white", command=Amelioration1Clic)
    Amelioration1Button.grid(row=1, column=14)

    Amelioration2Button = Button(fenetre, text="Acheter", width=10, height=1, bg="white", command=Amelioration2Clic)
    Amelioration2Button.grid(row=2, column=14)

    texte_score=Label(fenetre, text=f"{score} truc", bg="black", fg="white")
    texte_score.grid(row=0, column=5)

    Amelioration1Text=Label(fenetre, text=f"Amelioration 1 :  {prix1} truc", bg="black", fg="white")
    Amelioration1Text.grid(row=1, column=13)

    Amelioration2Text=Label(fenetre, text=f"Amelioration 1 :  {prix2} truc", bg="black", fg="white")
    Amelioration2Text.grid(row=2, column=13)

    texte_clicSec=Label(fenetre, text=f"{scoreClick} truc/Clic", bg="black", fg="white")
    texte_clicSec.grid(row=1, column=5)
    return zone_graphique, bouton_clicker, texte_score, texte_clicSec, Amelioration1Button, Amelioration1Text, Amelioration2Button


def AjoutScore():
    global score
    score=score+scoreClick                                  # A modifier
    texte_score.configure(text=score)

def Amelioration1Clic():
    global scoreClick
    global score
    if score >= 10:                                         # A modifier
        scoreClick=scoreClick+1                             # A modifier
        texte_clicSec.configure(text=f"{scoreClick}/sec")
        score=score-10                                      # A modifier
        texte_score.configure(text=f"{score}")


def Amelioration2Clic():
    global scoreClick
    global score
    if score >= 100:                                         # A modifier
        scoreClick=scoreClick+10                             # A modifier
        texte_clicSec.configure(text=f"{scoreClick}/sec")
        score=score-100                                      # A modifier
        texte_score.configure(text=f"{score}")


def Amelioration3Clic():
    global scoreClick
    global score
    if score >= 1000:                                         # A modifier
        scoreClick=scoreClick+100                             # A modifier
        texte_clicSec.configure(text=f"{scoreClick}/sec")
        score=score-1000                                      # A modifier
        texte_score.configure(text=f"{score}")


#----------------------------------------------------------------Main-----------------------------------------------------------------------------

scoreClick=1
prix1=10
prix2=100
score=0
t=0
fenetre=creer_fenetre()
zone_graphique, bouton_clicker, texte_score, texte_clicSec, Amelioration1Button, Amelioration1Text, Amelioration2Button=creer_widgets()



fenetre.mainloop()





