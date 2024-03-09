from tkinter import *
from PIL import *

def creer_fenetre():
    fenetre=Tk()
    fenetre.title("Computer Clicker")
    fenetre.grid_columnconfigure(0, minsize=60)
    fenetre.grid_rowconfigure(0, minsize=30)
    return fenetre

def creer_Canvas():
    zone_graphique = Canvas(fenetre, width=900, height=450, bg = "black")
    zone_graphique.grid(row=0, column=0, rowspan=15, columnspan=15)
    return zone_graphique

def cree_widget():
    text_joueur = Label(fenetre, text=f"Joueur : {joueur}", bg="black", fg="white")
    text_joueur.grid(row=0, column=0)
    
    return text_joueur

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
text_joueur =  cree_widget()
# photo, bouton_clicker, Amelioration1Button, Amelioration2Button, Amelioration3Button=creer_button()
# Amelioration1Text, Amelioration2Text, texte_score, texte_clicSec, texte_scoreClick, Amelioration3Text, text_joueur=creer_text()

fenetre.mainloop()