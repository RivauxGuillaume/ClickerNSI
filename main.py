import time
from tkinter import Tk, Canvas, Label, Button, Text, PhotoImage
import threading
from PIL import *


#----------------------------------------------------------------Fonction---------------------------------------------------------------------------


def creer_fenetre():
    fenetre=Tk()
    fenetre.title("Computer Clicker")
    return fenetre

def creer_Canvas():
    zone_graphique = Canvas(fenetre, width=900, height=500, bg = "black")
    zone_graphique.grid(row=0, column=0, rowspan=15, columnspan=15)
    return zone_graphique

def creer_button():
    photo = PhotoImage(file="ordi2.png")
    bouton_clicker = Button(fenetre, image=photo, command=AjoutScore, bg = "black", activebackground="black", width=500, height=300, bd=0)
    bouton_clicker.grid(row=6, column=5)
    #Création des différents bouton d'améliorations
    Amelioration1Button = Button(fenetre, text="Acheter", width=10, height=1, bg="white", command=Amelioration1Clic)
    Amelioration1Button.grid(row=2, column=14)

    Amelioration2Button = Button(fenetre, text="Acheter", width=10, height=1, bg="white", command=Amelioration2Clic)
    Amelioration2Button.grid(row=3, column=14)

    Amelioration3Button = Button(fenetre, text="Acheter", width=10, height=1, bg="white", command=Amelioration3Clic)
    Amelioration3Button.grid(row=4, column=14)
    return photo, bouton_clicker, Amelioration1Button, Amelioration2Button, Amelioration3Button


def creer_text():
    # Création des différents textes d'améliorations
    Amelioration1Text=Label(fenetre, text=f"Amelioration 1 :  {prix1} notes", bg="black", fg="white")
    Amelioration1Text.grid(row=2, column=13)

    Amelioration2Text=Label(fenetre, text=f"Amelioration 1 :  {prix2} notes", bg="black", fg="white")
    Amelioration2Text.grid(row=3, column=13)

    Amelioration3Text=Label(fenetre, text=f"Amelioration 1 :  {prix3} notes", bg="black", fg="white")
    Amelioration3Text.grid(row=4, column=13)

    # Création du texte du score
    texte_score=Label(fenetre, text=f"{score} notes", bg="black", fg="white")
    texte_score.grid(row=1, column=5)
    
    # Création du nb de clic
    texte_scoreClick=Label(fenetre, text=f"{scoreClick} notes/Clics", bg="black", fg="white")
    texte_scoreClick.grid(row=2, column=5)
    
    # Création du texte du score/sec
    texte_clicSec=Label(fenetre, text=f"{scoreSec} notes/Secondes", bg="black", fg="white")
    texte_clicSec.grid(row=3, column=5)

    # Création de l'entête affichant le joueur qui joue
    text_joueur = Label(fenetre, text=f"Joueur : {joueur}", bg="black", fg="white")
    text_joueur.grid(row=0, column=5, columnspan=2)

    return Amelioration1Text, Amelioration2Text, texte_score, texte_clicSec, texte_scoreClick, Amelioration3Text, text_joueur

def pop_up():
    fenetre_pop_up = Tk()
    fenetre_pop_up.title("Entre ton nom")
    # fenetre_pop_up.geometry("300x200")

    text_popup = Label(fenetre_pop_up, text="Entre ton nom : ", height=7)
    text_popup.grid(row=0, column=0)

    prenom_user = Text(fenetre_pop_up, height=1, width=14)
    prenom_user.grid(row=0, column=1)

    bouton_valider_popup = Button(fenetre_pop_up, text="Valider", width=12, command=recuperer_nom)
    bouton_valider_popup.grid(row=1, column=0, columnspan=2)

    return fenetre_pop_up, text_popup, prenom_user, bouton_valider_popup
    
def recuperer_nom():
    global joueur
    joueur = prenom_user.get("1.0", "end-1c")
    fenetre_pop_up.destroy()

def AjoutScore():
    global score
    score+=scoreClick                                  
    #Maj du score sur l'HUD
    texte_score.configure(text=f"{score} notes")

# peut pas marcher pqs time a une précision de 1e-7 mais windows block avant
def MajScoreSec():
    global score
    coeficient = int(scoreSec/100)
    while True:
        if coeficient == 0 and scoreSec != 0:
            time.sleep(1/scoreSec)
            score+=1
        elif coeficient > 0 :
            time.nanosleep((1/(scoreSec/coeficient))/1.5)
            score+=coeficient
        texte_score.configure(text=f"{score} notes")



def Amelioration1Clic():
    global scoreClick
    global score
    if score >= 10:                                         # A modifier
        scoreClick+=1                             # A modifier
        texte_scoreClick.configure(text=f"{scoreClick} notes/Clic")
        score-=10                                      # A modifier
        texte_score.configure(text=f"{score} notes")

# bug : n'enlève pas les 100 points au score
def Amelioration2Clic():
    global scoreSec
    global score
    if score >= 100:                                         # A modifier
        scoreSec+=1                                  # A modifier
        texte_clicSec.configure(text=f"{scoreSec} notes/Secondes")
        score = score - 100                                      # A modifier
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
    score += 1000
    texte_score.configure(text=f"{score} notes")


def ptpclick(event):
    global scoreClick
    scoreClick += 20
    texte_scoreClick.configure(text=f"{scoreClick} notes/Clic")

def ptpsecondes(event):
    global scoreSec
    scoreSec += 25
    texte_clicSec.configure(text=f"{scoreSec} notes/Secondes")


#----------------------------------------------------------------Main-----------------------------------------------------------------------------

scoreClick=1
scoreSec=0
prix1=10
prix2=100
prix3=1000
score=0

fenetre_pop_up, text_popup, prenom_user, bouton_valider_popup = pop_up()
fenetre_pop_up.mainloop()

fenetre=creer_fenetre()
zone_graphique=creer_Canvas()
photo, bouton_clicker, Amelioration1Button, Amelioration2Button, Amelioration3Button=creer_button()
Amelioration1Text, Amelioration2Text, texte_score, texte_clicSec, texte_scoreClick, Amelioration3Text, text_joueur=creer_text()



# activation commandes admin
fenetre.bind("<Up>", point1k)
fenetre.bind("<Left>", ptpclick)
fenetre.bind("<Right>", ptpsecondes)



# Gestion du multithread pour les clic/sec
th1 = threading.Thread(target=MajScoreSec)
th1.daemon = True
th1.start()

fenetre.mainloop()

