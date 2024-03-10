from tkinter import *
from PIL import *
import datetime

def start():
    lastSave = datetime.datetime.now().strftime('%a %d/%m/%y %H:%M') # modifié pour avoir la dernière datetime a récuperer dans le fichier de sauvegarde

    return lastSave

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

def creer_fenetre():
    fenetre=Tk()
    fenetre.title("Computer Clicker")
    fenetre.grid_columnconfigure(0, minsize=60)
    fenetre.grid_rowconfigure(0, minsize=30)
    return fenetre

def creer_Canvas():
    zone_graphique = Canvas(fenetre, width=900, height=420, bg = "red")
    zone_graphique.grid(row=0, column=0, rowspan=15, columnspan=14)
    return zone_graphique

def cree_widget():
    # Joueur qui joue
    text_player = Label(fenetre, text=f"Joueur : {joueur}", bg="black", fg="white")
    text_player.grid(row=0, column=0)

    # Bouton clicker
    picture = PhotoImage(file="ordi2.png")
    button_clicker = Button(fenetre, image=picture, command=AjoutScore, bg = "black", activebackground="black", width=270, height=255, bd=0)
    button_clicker.grid(row=1, column=0, rowspan=11, columnspan=5)
    
    # Texte dernière enregistrement
    text_last_save = Label(fenetre, text=f"Dernière sauvegarde :\n {lastSave}", bg="black", fg="white")
    text_last_save.grid(row=13, column=1, columnspan=2)

    # Text score
    text_score=Label(fenetre, text=f"{score} octets", bg="black", fg="white")
    text_score.grid(row=1, column=6, columnspan=3)

    # Text octets/secondes
    text_octets_secondes=Label(fenetre, text=f"Par Secondes : {scoreSec}", bg="black", fg="white")
    text_octets_secondes.grid(row=2, column=6, columnspan=3)

    # Text octets/click
    text_octets_click=Label(fenetre, text=f"Par Click : {scoreClick}", bg="black", fg="white")
    text_octets_click.grid(row=3, column=6, columnspan=3)

    # Bouton pour sauvegarder
    button_save = Button(fenetre, bg="black", activebackground="black", bd=5, command=save, text="Sauvegarder la progression", fg="white")
    button_save.grid(row=7, column=6, rowspan=2, columnspan=3)

    # Bouton pour sauvegarder et quitter
    button_save_quit = Button(fenetre, bg="black", activebackground="black", bd=5, command=save_and_quit, text="Sauvegarder et quitter", fg="white")
    button_save_quit.grid(row=11, column=6, rowspan=2, columnspan=3)

    return text_player, picture, button_clicker, text_last_save, text_score, text_octets_secondes, text_octets_click, button_save, button_save_quit       #pour que le programmme fonctionne, on est obligé de return la photo

def AjoutScore():
    global score
    score+=scoreClick                                  
    #Maj du score sur l'HUD
    text_score.configure(text=f"{score} notes")

def save():
    pass

def save_and_quit():
    save()
    fenetre.destroy()


scoreClick=1
scoreSec=0
prix1=10
prix2=100
prix3=1000
score=0

fenetre_pop_up, text_popup, prenom_user, bouton_valider_popup = pop_up()
fenetre_pop_up.mainloop()

lastSave = start()
fenetre = creer_fenetre()
zone_graphique = creer_Canvas()
text_player, picture, button_clicker, text_last_save, text_score, text_octets_secondes, text_octets_click, button_save, button_save_quit =  cree_widget()
# photo, bouton_clicker, Amelioration1Button, Amelioration2Button, Amelioration3Button=creer_button()
# Amelioration1Text, Amelioration2Text, texte_score, texte_clicSec, texte_scoreClick, Amelioration3Text, text_joueur=creer_text()

fenetre.mainloop()