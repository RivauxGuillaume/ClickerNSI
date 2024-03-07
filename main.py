"""
commentaire pour l'autre ici
"""
import time
from tkinter import Tk, Canvas, Label, Button
import threading


#----------------------------------------------------------------Fonction---------------------------------------------------------------------------


def creer_fenetre():
    fenetre=Tk()
    fenetre.title("Music Clicker")
    return fenetre


def creer_button():
    bouton_clicker = Button(fenetre, text="Clique !!!", width=50, height=20, bg="black", fg="white", bd=0, activebackground="black", command=AjoutScore, borderwidth=5) #remplacer le clicker qui est actuelement un bouton par une image (qui si possible change au fur a mesur du niveau)
    bouton_clicker.grid(row=5, column=5)
    #Création des différents bouton d'améliorations
    Amelioration1Button = Button(fenetre, text="Acheter", width=10, height=1, bg="white", command=Amelioration1Clic)
    Amelioration1Button.grid(row=1, column=14)

    Amelioration2Button = Button(fenetre, text="Acheter", width=10, height=1, bg="white", command=Amelioration2Clic)
    Amelioration2Button.grid(row=2, column=14)
    return bouton_clicker, Amelioration1Button, Amelioration2Button


def creer_text():
    # Création des différents textes d'améliorations
    Amelioration1Text=Label(fenetre, text=f"Amelioration 1 :  {prix1} notes", bg="black", fg="white")
    Amelioration1Text.grid(row=1, column=13)

    Amelioration2Text=Label(fenetre, text=f"Amelioration 1 :  {prix2} notes", bg="black", fg="white")
    Amelioration2Text.grid(row=2, column=13)
    # Création du texte du score
    texte_score=Label(fenetre, text=f"{score} notes", bg="black", fg="white")
    texte_score.grid(row=0, column=5)
    # Création du nb de clic
    texte_scoreClick=Label(fenetre, text=f"{scoreClick} notes/Clics", bg="black", fg="white")
    texte_scoreClick.grid(row=1, column=5)
    # Création du texte du score/sec
    texte_clicSec=Label(fenetre, text=f"{scoreSec} notes/Secondes", bg="black", fg="white")
    texte_clicSec.grid(row=2, column=5)


    return Amelioration1Text, Amelioration2Text, texte_score, texte_clicSec, texte_scoreClick


def creer_Canvas():
    zone_graphique = Canvas(fenetre, width=900, height=500, bg='black')
    zone_graphique.grid(row=0, column=0, rowspan=15, columnspan=15)
    return zone_graphique


def AjoutScore():
    global score
    score+=scoreClick                                  
    #Maj du score sur l'HUD
    texte_score.configure(text=f"{score} notes")


def MajScoreSec():
    global score
    while True:
        if scoreSec != 0 :
            time.sleep(1/scoreSec)
            score+=1
            texte_score.configure(text=f"{score} notes")


def Amelioration1Clic():
    global scoreClick
    global score
    if score >= 10:                                         # A modifier
        scoreClick+=1                             # A modifier
        texte_scoreClick.configure(text=f"{scoreClick} notes/Clic")
        score-=10                                      # A modifier
        texte_score.configure(text=f"{score} notes")


def Amelioration2Clic():
    global scoreSec
    global score
    if score >= 100:                                         # A modifier
        scoreSec+=1                                  # A modifier
        texte_clicSec.configure(text=f"{scoreSec} notes/Secondes")
        score-=100                                      # A modifier
        texte_score.configure(text=f"{score} notes")


def Amelioration3Clic():
    global scoreClick
    global score
    if score >= 1000:                                         # A modifier
        scoreClick=scoreClick+100                             # A modifier
        texte_scoreClick.configure(text=f"{scoreClick} notes/Clic")
        score=score-1000                                      # A modifier
        texte_score.configure(text=f"{score} notes")
#---------------------------------------------------------Provisoire---------------------------------------
def point1k(event):
    global score
    score = 1000
    texte_score.configure(text=f"{score} notes")


def ptpclick(event):
    global scoreClick
    scoreClick = 20
    texte_scoreClick.configure(text=f"{scoreClick} notes/Clic")

def ptpsecondes(event):
    global scoreSec
    scoreSec = 25
    texte_clicSec.configure(text=f"{scoreSec} notes/Secondes")


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

# activation commandes admin
fenetre.bind("<Up>", point1k)
fenetre.bind("<Left>", ptpclick)
fenetre.bind("<Right>", ptpsecondes)

# Gestion du multithread pour les clic/sec
th1=threading.Thread(target=MajScoreSec)
th1.start()


fenetre.mainloop()





