import time
from tkinter import Tk, Canvas, Label, Button, Text, PhotoImage
import threading
from PIL import *
import datetime

#----------------------------------------------------------------Fonction---------------------------------------------------------------------------

def creer_fenetre():
    fenetre=Tk()
    fenetre.title("Computer Clicker")
    fenetre.columnconfigure(0, minsize=60, pad=0)
    fenetre.rowconfigure(0, minsize=30, pad=0)
    fenetre.columnconfigure(1, minsize=60, pad=0)
    fenetre.rowconfigure(1, minsize=30, pad=0)
    fenetre.columnconfigure(2, minsize=60, pad=0)
    fenetre.rowconfigure(2, minsize=30, pad=0)
    fenetre.columnconfigure(3, minsize=60, pad=0)
    fenetre.rowconfigure(3, minsize=30, pad=0)
    fenetre.columnconfigure(4, minsize=60, pad=0)
    fenetre.rowconfigure(4, minsize=30, pad=0)
    fenetre.columnconfigure(5, minsize=60, pad=0)
    fenetre.rowconfigure(5, minsize=30, pad=0)
    fenetre.columnconfigure(6, minsize=60, pad=0)
    fenetre.rowconfigure(6, minsize=30, pad=0)
    fenetre.columnconfigure(7, minsize=60, pad=0)
    fenetre.rowconfigure(7, minsize=30, pad=0)
    fenetre.columnconfigure(8, minsize=60, pad=0)
    fenetre.rowconfigure(8, minsize=30, pad=0)
    fenetre.columnconfigure(9, minsize=60, pad=0)
    fenetre.rowconfigure(9, minsize=30, pad=0)
    fenetre.columnconfigure(10, minsize=60, pad=0)
    fenetre.rowconfigure(10, minsize=30, pad=0)
    fenetre.columnconfigure(11, minsize=60, pad=0)
    fenetre.rowconfigure(11, minsize=30, pad=0)
    fenetre.columnconfigure(12, minsize=60, pad=0)
    fenetre.rowconfigure(12, minsize=30, pad=0)
    fenetre.columnconfigure(13, minsize=60, pad=0)
    fenetre.rowconfigure(13, minsize=30, pad=0)
    fenetre.columnconfigure(14, minsize=60, pad=0)
    fenetre.rowconfigure(14, minsize=30, pad=0)
    return fenetre

def creer_Canvas():
    zone_graphique = Canvas(fenetre, width=1200, height=600, bg = "black")
    zone_graphique.grid(row=0, column=0, rowspan=15, columnspan=15)
    return zone_graphique

def cree_widget():
    # Joueur qui joue
    text_player = Label(fenetre, text=f"Joueur : {joueur}", bg="black", fg="white")
    text_player.grid(row=0, column=0)

    # Bouton clicker
    picture = PhotoImage(file="ordi2.png")
    button_clicker = Button(fenetre, image=picture, command=AjoutScore, bg = "black", activebackground="black", width=270, height=255, bd=0)
    button_clicker.grid(row=1, column=0, rowspan=11, columnspan=6)
    
    # Texte dernière enregistrement
    text_last_save = Label(fenetre, text=f"Dernière sauvegarde :\n {lastSave}", bg="black", fg="white")
    text_last_save.grid(row=13, column=1, columnspan=4)

    # Text score
    text_score=Label(fenetre, text=f"{score} octets", bg="black", fg="white")
    text_score.grid(row=1, column=7, columnspan=3)

    # Text octets/secondes
    text_octets_secondes=Label(fenetre, text=f"Par Secondes : {scoreSec}", bg="black", fg="white")
    text_octets_secondes.grid(row=2, column=7, columnspan=3)

    # Text octets/click
    text_octets_click=Label(fenetre, text=f"Par Click : {scoreClick}", bg="black", fg="white")
    text_octets_click.grid(row=3, column=7, columnspan=3)

    # Bouton pour sauvegarder
    button_save = Button(fenetre, bg="black", activebackground="black", bd=5, command=save, text="Sauvegarder la\nprogression", fg="white", font="Helvetica 10")
    button_save.grid(row=7, column=7, rowspan=2, columnspan=3)

    # Bouton pour sauvegarder et quitter
    button_save_quit = Button(fenetre, bg="black", activebackground="black", bd=5, command=save_and_quit, text="Sauvegarder et\nquitter", fg="white", font="Helvetica 10")
    button_save_quit.grid(row=11, column=7, rowspan=2, columnspan=3)

    return text_player, picture, button_clicker, text_last_save, text_score, text_octets_secondes, text_octets_click, button_save, button_save_quit     #pour que le programmme fonctionne, on est obligé de return la photo

def save():
    pass

def save_and_quit():
    save()
    fenetre.destroy()

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

def AjoutScore():
    global score
    score= round(score + scoreClick, 1)
    text_score.configure(text=f"{score} notes")

def MajScoreSec():
    global score
    global scoreSec
    initial_diviseur = 100
    while True:
        coeficient = int(scoreSec/initial_diviseur)
        if coeficient > initial_diviseur:
            initial_diviseur = initial_diviseur * 10
        if coeficient == 0 and scoreSec != 0:
            time.sleep(1/scoreSec)
            score+=1
        elif coeficient > 0:
            time.sleep(1/(scoreSec/coeficient))
            score+=int(coeficient * (initial_diviseur/100))
        text_score.configure(text=f"{score} notes")


def widgetUpgrade1():
    levelUpgrade1 = Label(fenetre, text="0", bg="black", fg="grey", font=("Arial",  18))
    levelUpgrade1.grid(row=3, column=11, rowspan=2)

    pictureUpgrade1 = PhotoImage(file="image/python.png")
    buttonUpgrade1 = Button(fenetre, image=pictureUpgrade1, bg="black", activebackground="black", command=Amelioration1Clic, width=60, height=60)
    buttonUpgrade1.grid(row=3, column=12, rowspan=2)

    priceUpgrade1 = Label(fenetre, text="prix : 10", bg="black", fg="white")
    priceUpgrade1.grid(row=3, column=13, rowspan=2)

    textUpgrade1 = Label(fenetre, text="augmente de 0.1 le nombre\nd'octets par secondes", bg="black", fg="white", font="Helvetica 10")
    textUpgrade1.grid(row=3, column=14, rowspan=2)

    return levelUpgrade1, pictureUpgrade1, buttonUpgrade1, priceUpgrade1, textUpgrade1

def widgetUpgrade2():
    levelUpgrade2 = Label(fenetre, text="0", bg="black", fg="grey", font=("Arial",  18))
    levelUpgrade2.grid(row=5, column=11, rowspan=2)

    pictureUpgrade2 = PhotoImage(file="image/python.png")
    buttonUpgrade2 = Button(fenetre, image=pictureUpgrade2, bg="black", activebackground="black", command=Amelioration2Clic, width=60, height=60)
    buttonUpgrade2.grid(row=5, column=12, rowspan=2)

    priceUpgrade2 = Label(fenetre, text="prix : 10", bg="black", fg="white")
    priceUpgrade2.grid(row=5, column=13, rowspan=2)

    textUpgrade2 = Label(fenetre, text="augmente de 0.1 le nombre\nd'octets par secondes", bg="black", fg="white", font="Helvetica 10")
    textUpgrade2.grid(row=5, column=14, rowspan=2)

    return levelUpgrade2, pictureUpgrade2, buttonUpgrade2, priceUpgrade2, textUpgrade2

def widgetUpgrade3():
    levelUpgrade3 = Label(fenetre, text="0", bg="black", fg="grey", font=("Arial",  18))
    levelUpgrade3.grid(row=7, column=11, rowspan=2)

    pictureUpgrade3 = PhotoImage(file="image/python.png")
    buttonUpgrade3 = Button(fenetre, image=pictureUpgrade3, bg="black", activebackground="black", command=Amelioration4Clic, width=60, height=60)
    buttonUpgrade3.grid(row=7, column=12, rowspan=2)

    priceUpgrade3 = Label(fenetre, text="prix : 10", bg="black", fg="white")
    priceUpgrade3.grid(row=7, column=13, rowspan=2)

    textUpgrade3 = Label(fenetre, text="augmente de 0.1 le nombre\nd'octets par secondes", bg="black", fg="white", font="Helvetica 10")
    textUpgrade3.grid(row=7, column=14, rowspan=2)

    return levelUpgrade3, pictureUpgrade3, buttonUpgrade3, priceUpgrade3, textUpgrade3

def widgetUpgrade4():
    levelUpgrade4 = Label(fenetre, text="0", bg="black", fg="grey", font=("Arial",  18))
    levelUpgrade4.grid(row=9, column=11, rowspan=2)

    pictureUpgrade4 = PhotoImage(file="image/python.png")
    buttonUpgrade4 = Button(fenetre, image=pictureUpgrade4, bg="black", activebackground="black", command=Amelioration4Clic, width=60, height=60)
    buttonUpgrade4.grid(row=9, column=12, rowspan=2)

    priceUpgrade4 = Label(fenetre, text="prix : 10", bg="black", fg="white")
    priceUpgrade4.grid(row=9, column=13, rowspan=2)

    textUpgrade4 = Label(fenetre, text="augmente de 0.1 le nombre\nd'octets par secondes", bg="black", fg="white", font="Helvetica 10")
    textUpgrade4.grid(row=9, column=14, rowspan=2)

    return levelUpgrade4, pictureUpgrade4, buttonUpgrade4, priceUpgrade4, textUpgrade4

def widgetUpgrade5():
    levelUpgrade5 = Label(fenetre, text="0", bg="black", fg="grey", font=("Arial",  18))
    levelUpgrade5.grid(row=11, column=11, rowspan=2)

    pictureUpgrade5 = PhotoImage(file="image/python.png")
    buttonUpgrade5 = Button(fenetre, image=pictureUpgrade5, bg="black", activebackground="black", command=Amelioration5Clic, width=60, height=60)
    buttonUpgrade5.grid(row=11, column=12, rowspan=2)

    priceUpgrade5 = Label(fenetre, text="prix : 10", bg="black", fg="white")
    priceUpgrade5.grid(row=11, column=13, rowspan=2)

    textUpgrade5 = Label(fenetre, text="augmente de 0.1 le nombre\nd'octets par secondes", bg="black", fg="white", font="Helvetica 10")
    textUpgrade5.grid(row=11, column=14, rowspan=2)

    return levelUpgrade5, pictureUpgrade5, buttonUpgrade5, priceUpgrade5, textUpgrade5

def Amelioration1Clic():
    global scoreClick
    global score
    global niveau_amelioration1
    global levelUpgrade1
    if niveau_amelioration1 <= 49:
        if score >= prix_amelioration_1[niveau_amelioration1]:
            niveau_amelioration1 += 1# A modifier
            if niveau_amelioration1 == 50:
                levelUpgrade1.configure(text="MAX")
                priceUpgrade1.configure(text=f"niveau max\natteint")
            else:
                levelUpgrade1.configure(text=niveau_amelioration1)
                priceUpgrade1.configure(text=f"prix : {prix_amelioration_1[niveau_amelioration1]}")
            scoreClick = round(scoreClick + 0.1, 1)                            # A modifier
            text_octets_click.configure(text=f"{scoreClick} octets/Clic")
            score= round(score-prix_amelioration_1[niveau_amelioration1 - 1], 1)                                      # A modifier
            text_score.configure(text=f"{score} notes")

def Amelioration2Clic():
    pass

def Amelioration3Clic():
    pass

def Amelioration4Clic():
    pass

def Amelioration5Clic():
    pass

"""
        elif coeficient > 0:
            time.sleep(1/(scoreSec/coeficient))
            score+=int(coeficient * (initial_diviseur/100))
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
"""
#---------------------------------------------------------Provisoire---------------------------------------

def point1k(event):
    global score
    score += 1000
    text_score.configure(text=f"{score} notes")


def ptpclick(event):
    global scoreClick
    scoreClick += 20
    text_octets_click.configure(text=f"{scoreClick} notes/Clic")

def ptpsecondes(event):
    global scoreSec
    scoreSec += 25
    text_octets_secondes.configure(text=f"{scoreSec} notes/Secondes")


#----------------------------------------------------------------Main-----------------------------------------------------------------------------

scoreClick=1
scoreSec=0
score=0
niveau_amelioration1 = 0
prix_amelioration_1 = [10, 12.0, 14.4, 17.3, 20.8, 25.0, 30.0, 36.0, 43.2, 51.8, 62.2, 74.6, 89.5, 107.4, 128.9, 154.7, 185.6, 222.7, 267.2, 320.6, 384.7, 461.6, 553.9, 664.7, 797.6, 957.1, 1148.5, 1378.2, 1653.8, 1984.6, 2381.5, 2857.8, 3429.4, 4115.3, 4938.4, 5926.1, 7111.3, 8533.6, 10240.3, 12288.4, 14746.1, 17695.3, 21234.4, 25481.3, 30577.6, 36693.1, 44031.7, 52838.0, 63405.6, 76086.7]

fenetre_pop_up, text_popup, prenom_user, bouton_valider_popup = pop_up()
fenetre_pop_up.mainloop()

lastSave = start()
fenetre = creer_fenetre()
zone_graphique = creer_Canvas()
text_player, picture, button_clicker, text_last_save, text_score, text_octets_secondes, text_octets_click, button_save, button_save_quit =  cree_widget()
levelUpgrade1, pictureUpgrade1, buttonUpgrade1, priceUpgrade1, textUpgrade1 = widgetUpgrade1()
levelUpgrade2, pictureUpgrade2, buttonUpgrade2, priceUpgrade2, textUpgrade2 = widgetUpgrade2()
levelUpgrade3, pictureUpgrade3, buttonUpgrade3, priceUpgrade3, textUpgrade3 = widgetUpgrade3()
levelUpgrade4, pictureUpgrade4, buttonUpgrade4, priceUpgrade4, textUpgrade4 = widgetUpgrade4()
levelUpgrade5, pictureUpgrade5, buttonUpgrade5, priceUpgrade5, textUpgrade5 = widgetUpgrade5()



# activation commandes admin
fenetre.bind("<Up>", point1k)
fenetre.bind("<Left>", ptpclick)
fenetre.bind("<Right>", ptpsecondes)



# Gestion du multithread pour les clic/sec
th1 = threading.Thread(target=MajScoreSec)
th1.daemon = True
th1.start()

fenetre.mainloop()

