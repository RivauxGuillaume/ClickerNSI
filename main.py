import time
from tkinter import Tk, Canvas, Label, Button, Text, PhotoImage
import threading
from PIL import *
import datetime

#----------------------------------------------------------------Fonction---------------------------------------------------------------------------

def creer_fenetre():
    fenetre=Tk()

    fenetre.title("Computer Clicker")
    screen_width = (fenetre.winfo_screenwidth() - 4)
    screen_height = (fenetre.winfo_screenheight() - 4)
    fenetre.attributes('-fullscreen', True)
    for i in range(15):
        fenetre.columnconfigure(i, minsize=int(screen_width/16), pad=0)
        fenetre.rowconfigure(i, minsize=int(screen_height/16), pad=0)
    return fenetre, screen_width, screen_height

def creer_Canvas():
    zone_graphique = Canvas(fenetre, width=screen_width, height=screen_height, bg = "gray28", border=0, borderwidth=0)
    zone_graphique.grid(row=0, column=0, rowspan=15, columnspan=15)

    return zone_graphique

def cree_widget():
    # Joueur qui joue
    text_player = Label(fenetre, text=f"Joueur : {joueur}", bg="gray28", fg="white")
    text_player.grid(row=0, column=0)

    # Bouton clicker
    picture = PhotoImage(file="image/ordi2.png")
    button_clicker = Button(fenetre, image=picture, command=AjoutScore, bg = "gray28", activebackground="gray28", bd=0)
    button_clicker.grid(row=1, column=0, rowspan=11, columnspan=6)

    # Texte dernière enregistrement
    text_last_save = Label(fenetre, text=f"Dernière sauvegarde :\n {lastSave}", bg="gray28", fg="white")
    text_last_save.grid(row=13, column=1, columnspan=4)

    # Text score
    text_score=Label(fenetre, text=f"{score} octets", bg="gray28", fg="white")
    text_score.grid(row=1, column=7, columnspan=3)

    # Text octets/secondes
    text_octets_secondes=Label(fenetre, text=f"Par Secondes : {scoreSec}", bg="gray28", fg="white")
    text_octets_secondes.grid(row=2, column=7, columnspan=3)

    # Text octets/click
    text_octets_click=Label(fenetre, text=f"Par Click : {scoreClick}", bg="gray28", fg="white")
    text_octets_click.grid(row=3, column=7, columnspan=3)

    # Bouton pour sauvegarder
    button_save = Button(fenetre, bg="gray28", activebackground="gray28", bd=5, command=save, text="Sauvegarder la\nprogression", fg="white", font="Helvetica 12")
    button_save.grid(row=7, column=7, rowspan=2, columnspan=3)

    # Bouton pour sauvegarder et quitter
    button_save_quit = Button(fenetre, bg="gray28", activebackground="gray28", bd=5, command=save_and_quit, text="Sauvegarder et\nquitter", fg="white", font="Helvetica 12")
    button_save_quit.grid(row=11, column=7, rowspan=2, columnspan=3)

    return text_player, picture, button_clicker, text_last_save, text_score, text_octets_secondes, text_octets_click, button_save, button_save_quit     #pour que le programmme fonctionne, on est obligé de return la photo

def save():
    pass

def save_and_quit():
    save()
    fenetre.destroy()

def start():
    lastSave = datetime.datetime.now().strftime('%a %d/%m/%y %H:%M') # à modifié pour avoir la dernière datetime a récuperer dans le fichier de sauvegarde

    return lastSave

def pop_up():
    fenetre_pop_up = Tk()
    fenetre_pop_up.title("Entre ton nom")
    fenetre_pop_up.geometry("200x150+900+400")

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
    text_score.configure(text=f"{score} octets")

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
        text_score.configure(text=f"{score} octets")

def load_picture():
    pictureUpgrade1 = PhotoImage(file="image/python.png")
    pictureUpgrade2 = PhotoImage(file="image/html.png")
    pictureUpgrade3 = PhotoImage(file="image/css.png")
    pictureUpgrade4 = PhotoImage(file="image/js.png")
    pictureUpgrade5 = PhotoImage(file="image/c++.png")
    pictureUpgrade6 = PhotoImage(file="image/c#.png")
    pictureUpgrade7 = PhotoImage(file="image/python.png")
    pictureUpgrade8 = PhotoImage(file="image/python.png")
    pictureUpgrade9 = PhotoImage(file="image/python.png")
    pictureUpgrade10 = PhotoImage(file="image/python.png")
    pictureUpgrade11 = PhotoImage(file="image/python.png")
    pictureUpgrade12 = PhotoImage(file="image/python.png")
    pictureUpgrade13 = PhotoImage(file="image/python.png")
    pictureUpgrade14 = PhotoImage(file="image/python.png")
    pictureUpgrade15 = PhotoImage(file="image/python.png")
    pictureUpgrade16 = PhotoImage(file="image/python.png")
    pictureBoost1 = PhotoImage(file="image/css.png")
    pictureBoost2 = PhotoImage(file="image/html.png")
    pictureBoost3 = PhotoImage(file="image/c#.png")
    pictureBoost4 = PhotoImage(file="image/js.png")
    pictureBoost5 = PhotoImage(file="image/c#.png")
    pictureBoost6 = PhotoImage(file="image/js.png")
    pictureBoost7 = PhotoImage(file="image/c#.png")
    pictureBoost8 = PhotoImage(file="image/js.png")
    pictureBoost9 = PhotoImage(file="image/c#.png")
    pictureBoost10 = PhotoImage(file="image/js.png")
    pictureBoost11 = PhotoImage(file="image/c#.png")
    pictureBoost12 = PhotoImage(file="image/js.png")
    pictureBoost13 = PhotoImage(file="image/c#.png")
    pictureBoost14 = PhotoImage(file="image/js.png")
    pictureBoost15 = PhotoImage(file="image/c#.png")

    return pictureUpgrade1,  pictureUpgrade2, pictureUpgrade3, pictureUpgrade4, pictureUpgrade5,  pictureUpgrade6, pictureUpgrade7, pictureUpgrade8, pictureUpgrade9, pictureUpgrade10, pictureUpgrade11, pictureUpgrade12, pictureUpgrade13, pictureUpgrade14, pictureUpgrade15, pictureUpgrade16, pictureBoost1, pictureBoost2, pictureBoost3, pictureBoost4, pictureBoost5, pictureBoost6, pictureBoost7, pictureBoost8, pictureBoost9, pictureBoost10, pictureBoost11, pictureBoost12, pictureBoost13, pictureBoost14, pictureBoost15


def widgetUpgrade1():
    global pictureUpgrade1
    levelUpgrade1 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade1.grid(row=rowUpgrade1, column=10, rowspan=2)

    buttonUpgrade1 = Button(fenetre, image=pictureUpgrade1, bg="gray28", activebackground="gray28", command=Amelioration1Clic, width=60, height=60)
    buttonUpgrade1.grid(row=rowUpgrade1, column=11, rowspan=2)

    priceUpgrade1 = Label(fenetre, text="prix : 10", bg="gray28", fg="white")
    priceUpgrade1.grid(row=rowUpgrade1, column=12, rowspan=2)

    textUpgrade1 = Label(fenetre, text="augmente de 0.1\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade1.grid(row=rowUpgrade1, column=13, rowspan=2)

    return levelUpgrade1, buttonUpgrade1, priceUpgrade1, textUpgrade1

def widgetUpgrade2():
    global pictureUpgrade2
    levelUpgrade2 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade2.grid(row=rowUpgrade2, column=10, rowspan=2)

    buttonUpgrade2 = Button(fenetre, image=pictureUpgrade2, bg="gray28", activebackground="gray28", command=Amelioration2Clic, width=60, height=60)
    buttonUpgrade2.grid(row=rowUpgrade2, column=11, rowspan=2)

    priceUpgrade2 = Label(fenetre, text="prix : 100", bg="gray28", fg="white")
    priceUpgrade2.grid(row=rowUpgrade2, column=12, rowspan=2)

    textUpgrade2 = Label(fenetre, text="augmente de 2\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade2.grid(row=rowUpgrade2, column=13, rowspan=2)

    return levelUpgrade2, buttonUpgrade2, priceUpgrade2, textUpgrade2

def widgetUpgrade3():
    global pictureUpgrade3
    levelUpgrade3 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade3.grid(row=rowUpgrade3, column=10, rowspan=2)

    buttonUpgrade3 = Button(fenetre, image=pictureUpgrade3, bg="gray28", activebackground="gray28", command=Amelioration3Clic, width=60, height=60)
    buttonUpgrade3.grid(row=rowUpgrade3, column=11, rowspan=2)

    priceUpgrade3 = Label(fenetre, text="prix : 1 100", bg="gray28", fg="white")
    priceUpgrade3.grid(row=rowUpgrade3, column=12, rowspan=2)

    textUpgrade3 = Label(fenetre, text="augmente de 8\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade3.grid(row=rowUpgrade3, column=13, rowspan=2)

    return levelUpgrade3, buttonUpgrade3, priceUpgrade3, textUpgrade3

def widgetUpgrade4():
    global pictureUpgrade4
    levelUpgrade4 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade4.grid(row=rowUpgrade4, column=10, rowspan=2)

    buttonUpgrade4 = Button(fenetre, image=pictureUpgrade4, bg="gray28", activebackground="gray28", command=Amelioration4Clic, width=60, height=60)
    buttonUpgrade4.grid(row=rowUpgrade4, column=11, rowspan=2)

    priceUpgrade4 = Label(fenetre, text="prix : 12 000", bg="gray28", fg="white")
    priceUpgrade4.grid(row=rowUpgrade4, column=12, rowspan=2)

    textUpgrade4 = Label(fenetre, text="augmente de 47\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade4.grid(row=rowUpgrade4, column=13, rowspan=2)

    return levelUpgrade4, buttonUpgrade4, priceUpgrade4, textUpgrade4

def widgetUpgrade5():
    global pictureUpgrade5
    levelUpgrade5 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade5.grid(row=rowUpgrade5, column=10, rowspan=2)

    buttonUpgrade5 = Button(fenetre, image=pictureUpgrade5, bg="gray28", activebackground="gray28", command=Amelioration5Clic, width=60, height=60)
    buttonUpgrade5.grid(row=rowUpgrade5, column=11, rowspan=2)

    priceUpgrade5 = Label(fenetre, text="prix : 130 000", bg="gray28", fg="white")
    priceUpgrade5.grid(row=rowUpgrade5, column=12, rowspan=2)

    textUpgrade5 = Label(fenetre, text="augmente de 260\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade5.grid(row=rowUpgrade5, column=13, rowspan=2)

    return levelUpgrade5, buttonUpgrade5, priceUpgrade5, textUpgrade5

def widgetUpgrade6():
    global pictureUpgrade6
    levelUpgrade6 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade6.grid(row=rowUpgrade6, column=10, rowspan=2)

    buttonUpgrade6 = Button(fenetre, image=pictureUpgrade6, bg="gray28", activebackground="gray28", command=Amelioration6Clic, width=60, height=60)
    buttonUpgrade6.grid(row=rowUpgrade6, column=11, rowspan=2)

    priceUpgrade6 = Label(fenetre, text="prix : 1 400 000", bg="gray28", fg="white")
    priceUpgrade6.grid(row=rowUpgrade6, column=12, rowspan=2)

    textUpgrade6 = Label(fenetre, text="augmente de 1 400\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade6.grid(row=rowUpgrade6, column=13, rowspan=2)

    return levelUpgrade6, buttonUpgrade6, priceUpgrade6, textUpgrade6

def widgetUpgrade7():
    global pictureUpgrade7
    levelUpgrade7 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade7.grid(row=rowUpgrade7, column=10, rowspan=2)

    buttonUpgrade7 = Button(fenetre, image=pictureUpgrade7, bg="gray28", activebackground="gray28", command=Amelioration7Clic, width=60, height=60)
    buttonUpgrade7.grid(row=rowUpgrade7, column=11, rowspan=2)

    priceUpgrade7 = Label(fenetre, text="prix : 20 000 000", bg="gray28", fg="white")
    priceUpgrade7.grid(row=rowUpgrade7, column=12, rowspan=2)

    textUpgrade7 = Label(fenetre, text="augmente de 7 800\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade7.grid(row=rowUpgrade7, column=13, rowspan=2)

    return levelUpgrade7, buttonUpgrade7, priceUpgrade7, textUpgrade7

def widgetUpgrade8():
    global pictureUpgrade8
    levelUpgrade8 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade8.grid(row=rowUpgrade8, column=10, rowspan=2)

    buttonUpgrade8 = Button(fenetre, image=pictureUpgrade8, bg="gray28", activebackground="gray28", command=Amelioration8Clic, width=60, height=60)
    buttonUpgrade8.grid(row=rowUpgrade8, column=11, rowspan=2)

    priceUpgrade8 = Label(fenetre, text="prix : 330 000 000", bg="gray28", fg="white")
    priceUpgrade8.grid(row=rowUpgrade8, column=12, rowspan=2)

    textUpgrade8 = Label(fenetre, text="augmente de 44 000\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade8.grid(row=rowUpgrade8, column=13, rowspan=2)

    return levelUpgrade8, buttonUpgrade8, priceUpgrade8, textUpgrade8

def widgetUpgrade9():
    global pictureUpgrade9
    levelUpgrade9 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade9.grid(row=rowUpgrade9, column=10, rowspan=2)

    buttonUpgrade9 = Button(fenetre, image=pictureUpgrade9, bg="gray28", activebackground="gray28", command=Amelioration9Clic, width=60, height=60)
    buttonUpgrade9.grid(row=rowUpgrade9, column=11, rowspan=2)

    priceUpgrade9 = Label(fenetre, text="prix :5 100 000 000", bg="gray28", fg="white")
    priceUpgrade9.grid(row=rowUpgrade9, column=12, rowspan=2)

    textUpgrade9 = Label(fenetre, text="augmente de 260 000\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade9.grid(row=rowUpgrade9, column=13, rowspan=2)

    return levelUpgrade9, buttonUpgrade9, priceUpgrade9, textUpgrade9

def widgetUpgrade10():
    global pictureUpgrade10
    levelUpgrade10 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade10.grid(row=rowUpgrade10, column=10, rowspan=2)

    buttonUpgrade10 = Button(fenetre, image=pictureUpgrade10, bg="gray28", activebackground="gray28", command=Amelioration10Clic, width=60, height=60)
    buttonUpgrade10.grid(row=rowUpgrade10, column=11, rowspan=2)

    priceUpgrade10 = Label(fenetre, text="prix : 75 000 000 000", bg="gray28", fg="white")
    priceUpgrade10.grid(row=rowUpgrade10, column=12, rowspan=2)

    textUpgrade10 = Label(fenetre, text="augmente de 1 600 000\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade10.grid(row=rowUpgrade10, column=13, rowspan=2)

    return levelUpgrade10, buttonUpgrade10, priceUpgrade10, textUpgrade10

def widgetUpgrade11():
    global pictureUpgrade11
    levelUpgrade11 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade11.grid(row=rowUpgrade11, column=10, rowspan=2)

    buttonUpgrade11 = Button(fenetre, image=pictureUpgrade11, bg="gray28", activebackground="gray28", command=Amelioration11Clic, width=60, height=60)
    buttonUpgrade11.grid(row=rowUpgrade11, column=11, rowspan=2)

    priceUpgrade11 = Label(fenetre, text="prix : 1 000 000 000 000", bg="gray28", fg="white")
    priceUpgrade11.grid(row=rowUpgrade11, column=12, rowspan=2)

    textUpgrade11 = Label(fenetre, text="augmente de 10 000 000\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade11.grid(row=rowUpgrade11, column=13, rowspan=2)

    return levelUpgrade11, buttonUpgrade11, priceUpgrade11, textUpgrade11

def widgetUpgrade12():
    global pictureUpgrade12
    levelUpgrade12 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade12.grid(row=rowUpgrade12, column=10, rowspan=2)

    buttonUpgrade12 = Button(fenetre, image=pictureUpgrade12, bg="gray28", activebackground="gray28", command=Amelioration12Clic, width=60, height=60)
    buttonUpgrade12.grid(row=rowUpgrade12, column=11, rowspan=2)

    priceUpgrade12 = Label(fenetre, text="prix : 14 000 000 000 000", bg="gray28", fg="white")
    priceUpgrade12.grid(row=rowUpgrade12, column=12, rowspan=2)

    textUpgrade12 = Label(fenetre, text="augmente de 65 000 000\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade12.grid(row=rowUpgrade12, column=13, rowspan=2)

    return levelUpgrade12, buttonUpgrade12, priceUpgrade12, textUpgrade12

def widgetUpgrade13():
    global pictureUpgrade13
    levelUpgrade13 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade13.grid(row=rowUpgrade13, column=10, rowspan=2)

    buttonUpgrade13 = Button(fenetre, image=pictureUpgrade13, bg="gray28", activebackground="gray28", command=Amelioration13Clic, width=60, height=60)
    buttonUpgrade13.grid(row=rowUpgrade13, column=11, rowspan=2)

    priceUpgrade13 = Label(fenetre, text="prix : 170 000 000 000 000", bg="gray28", fg="white")
    priceUpgrade13.grid(row=rowUpgrade13, column=12, rowspan=2)

    textUpgrade13 = Label(fenetre, text="augmente de 430 000 000\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade13.grid(row=rowUpgrade13, column=13, rowspan=2)

    return levelUpgrade13, buttonUpgrade13, priceUpgrade13, textUpgrade13

def widgetUpgrade14():
    global pictureUpgrade14
    levelUpgrade14 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade14.grid(row=rowUpgrade14, column=10, rowspan=2)

    buttonUpgrade14 = Button(fenetre, image=pictureUpgrade14, bg="gray28", activebackground="gray28", command=Amelioration14Clic, width=60, height=60)
    buttonUpgrade14.grid(row=rowUpgrade14, column=11, rowspan=2)

    priceUpgrade14 = Label(fenetre, text="prix : 2 100 000 000 000 000", bg="gray28", fg="white")
    priceUpgrade14.grid(row=rowUpgrade14, column=12, rowspan=2)

    textUpgrade14 = Label(fenetre, text="augmente de 2 900 000 000\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade14.grid(row=rowUpgrade14, column=13, rowspan=2)

    return levelUpgrade14, buttonUpgrade14, priceUpgrade14, textUpgrade14

def widgetUpgrade15():
    global pictureUpgrade15
    levelUpgrade15 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade15.grid(row=rowUpgrade15, column=10, rowspan=2)

    buttonUpgrade15 = Button(fenetre, image=pictureUpgrade15, bg="gray28", activebackground="gray28", command=Amelioration15Clic, width=60, height=60)
    buttonUpgrade15.grid(row=rowUpgrade15, column=11, rowspan=2)

    priceUpgrade15 = Label(fenetre, text="prix : 26 000 000 000 000 000", bg="gray28", fg="white")
    priceUpgrade15.grid(row=rowUpgrade15, column=12, rowspan=2)

    textUpgrade15 = Label(fenetre, text="augmente de 21 000 000 000\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade15.grid(row=rowUpgrade15, column=13, rowspan=2)

    return levelUpgrade15, buttonUpgrade15, priceUpgrade15, textUpgrade15

def widgetUpgrade16():
    global pictureUpgrade16
    levelUpgrade16 = Label(fenetre, text="0", bg="gray28", fg="grey", font=("Arial",  18))
    levelUpgrade16.grid(row=rowUpgrade16, column=10, rowspan=2)

    buttonUpgrade16 = Button(fenetre, image=pictureUpgrade16, bg="gray28", activebackground="gray28", command=Amelioration16Clic, width=60, height=60)
    buttonUpgrade16.grid(row=rowUpgrade16, column=11, rowspan=2)

    priceUpgrade16 = Label(fenetre, text="prix : 310 000 000 000 000 000", bg="gray28", fg="white")
    priceUpgrade16.grid(row=rowUpgrade16, column=12, rowspan=2)

    textUpgrade16 = Label(fenetre, text="augmente de 150 000 000 000\nle nombre d'octets\npar secondes", bg="gray28", fg="white", font="Helvetica 10")
    textUpgrade16.grid(row=rowUpgrade16, column=13, rowspan=2)

    return levelUpgrade16, buttonUpgrade16, priceUpgrade16, textUpgrade16

def widgetBoost1():
    buttonBoost1=Button(fenetre, image=pictureBoost1, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost1Clic)
    buttonBoost1.grid(row=1, column=columnBoost1)
    return buttonBoost1

def widgetBoost2():
    buttonBoost2=Button(fenetre, image=pictureBoost2, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost2Clic)
    buttonBoost2.grid(row=1, column=columnBoost2)
    return buttonBoost2

def widgetBoost3():
    buttonBoost3=Button(fenetre, image=pictureBoost3, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost3Clic)
    buttonBoost3.grid(row=1, column=columnBoost3)
    return buttonBoost3

def widgetBoost4():
    buttonBoost4=Button(fenetre, image=pictureBoost4, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost4Clic)
    buttonBoost4.grid(row=1, column=columnBoost4)
    return buttonBoost4

def widgetBoost5():
    buttonBoost5=Button(fenetre, image=pictureBoost5, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost5Clic)
    buttonBoost5.grid(row=1, column=columnBoost5)
    return buttonBoost5

def widgetBoost6():
    buttonBoost6=Button(fenetre, image=pictureBoost6, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost6Clic)
    buttonBoost6.grid(row=1, column=columnBoost6)
    return buttonBoost6

def widgetBoost7():
    buttonBoost7=Button(fenetre, image=pictureBoost7, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost7Clic)
    buttonBoost7.grid(row=1, column=columnBoost7)
    return buttonBoost7

def widgetBoost8():
    buttonBoost8=Button(fenetre, image=pictureBoost8, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost8Clic)
    buttonBoost8.grid(row=1, column=columnBoost8)
    return buttonBoost8

def widgetBoost9():
    buttonBoost9=Button(fenetre, image=pictureBoost9, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost9Clic)
    buttonBoost9.grid(row=1, column=columnBoost9)
    return buttonBoost9

def widgetBoost10():
    buttonBoost10=Button(fenetre, image=pictureBoost10, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost10Clic)
    buttonBoost10.grid(row=1, column=columnBoost10)
    return buttonBoost10

def widgetBoost11():
    buttonBoost11=Button(fenetre, image=pictureBoost11, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost11Clic)
    buttonBoost11.grid(row=1, column=columnBoost11)
    return buttonBoost11

def widgetBoost12():
    buttonBoost12=Button(fenetre, image=pictureBoost12, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost12Clic)
    buttonBoost12.grid(row=1, column=columnBoost12)
    return buttonBoost12

def widgetBoost13():
    buttonBoost13=Button(fenetre, image=pictureBoost13, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost13Clic)
    buttonBoost13.grid(row=1, column=columnBoost13)
    return buttonBoost13

def widgetBoost14():
    buttonBoost14=Button(fenetre, image=pictureBoost14, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost14Clic)
    buttonBoost14.grid(row=1, column=columnBoost14)
    return buttonBoost14

def widgetBoost15():
    buttonBoost15=Button(fenetre, image=pictureBoost15, bg="gray28", activebackground="gray28", width=60, height=60, command=Boost15Clic)
    buttonBoost15.grid(row=1, column=columnBoost15)
    return buttonBoost15

def deleteAmelioration(niveau):
    global dicVariable
    global listAmelioration
    global levelUpgrade6, buttonUpgrade6, priceUpgrade6, textUpgrade6
    global levelUpgrade7, buttonUpgrade7, priceUpgrade7, textUpgrade7
    global levelUpgrade8, buttonUpgrade8, priceUpgrade8, textUpgrade8
    global levelUpgrade9, buttonUpgrade9, priceUpgrade9, textUpgrade9
    global levelUpgrade10, buttonUpgrade10, priceUpgrade10, textUpgrade10
    global levelUpgrade11, buttonUpgrade11, priceUpgrade11, textUpgrade11
    global levelUpgrade12, buttonUpgrade12, priceUpgrade12, textUpgrade12
    global levelUpgrade13, buttonUpgrade13, priceUpgrade13, textUpgrade13
    global levelUpgrade14, buttonUpgrade14, priceUpgrade14, textUpgrade14
    global levelUpgrade15, buttonUpgrade15, priceUpgrade15, textUpgrade15
    global levelUpgrade16, buttonUpgrade16, priceUpgrade16, textUpgrade16
    time.sleep(5)
    dicVariable[f"levelUpgrade{niveau}"].destroy()
    dicVariable[f"buttonUpgrade{niveau}"].destroy()
    dicVariable[f"priceUpgrade{niveau}"].destroy()
    dicVariable[f"textUpgrade{niveau}"].destroy()
    for i in range(len(listAmelioration)):
        if listAmelioration[i] == niveau:
            for j in listAmelioration:
                if j > niveau:
                    dicVariable[f"rowUpgrade{j}"] -= 2
                    dicVariable[f"levelUpgrade{j}"].grid(row=dicVariable[f"rowUpgrade{j}"])
                    dicVariable[f"buttonUpgrade{j}"].grid(row=dicVariable[f"rowUpgrade{j}"])
                    dicVariable[f"priceUpgrade{j}"].grid(row=dicVariable[f"rowUpgrade{j}"])
                    dicVariable[f"textUpgrade{j}"].grid(row=dicVariable[f"rowUpgrade{j}"])
            numADelete = i
    del(listAmelioration[numADelete])
    if max(listAmelioration) == 5:
        levelUpgrade6, buttonUpgrade6,  priceUpgrade6, textUpgrade6 = widgetUpgrade6()
        dicVariable["levelUpgrade6"] = levelUpgrade6
        dicVariable["buttonUpgrade6"] = buttonUpgrade6
        dicVariable["priceUpgrade6"] = priceUpgrade6
        dicVariable["textUpgrade6"] = textUpgrade6
        dicVariable["rowUpgrade6"] = rowUpgrade6
        listAmelioration.append(6)
    elif max(listAmelioration) == 6:
        levelUpgrade7, buttonUpgrade7,  priceUpgrade7, textUpgrade7 = widgetUpgrade7()
        dicVariable["levelUpgrade7"] = levelUpgrade7
        dicVariable["buttonUpgrade7"] = buttonUpgrade7
        dicVariable["priceUpgrade7"] = priceUpgrade7
        dicVariable["textUpgrade7"] = textUpgrade7
        dicVariable["rowUpgrade7"] = rowUpgrade7
        listAmelioration.append(7)
    elif max(listAmelioration) == 7:
        levelUpgrade8, buttonUpgrade8,  priceUpgrade8, textUpgrade8 = widgetUpgrade8()
        dicVariable["levelUpgrade8"] = levelUpgrade8
        dicVariable["buttonUpgrade8"] = buttonUpgrade8
        dicVariable["priceUpgrade8"] = priceUpgrade8
        dicVariable["textUpgrade8"] = textUpgrade8
        dicVariable["rowUpgrade8"] = rowUpgrade8
        listAmelioration.append(8)
    elif max(listAmelioration) == 8:
        levelUpgrade9, buttonUpgrade9,  priceUpgrade9, textUpgrade9 = widgetUpgrade9()
        dicVariable["levelUpgrade9"] = levelUpgrade9
        dicVariable["buttonUpgrade9"] = buttonUpgrade9
        dicVariable["priceUpgrade9"] = priceUpgrade9
        dicVariable["textUpgrade9"] = textUpgrade9
        dicVariable["rowUpgrade9"] = rowUpgrade9
        listAmelioration.append(9)
    elif max(listAmelioration) == 9:
        levelUpgrade10, buttonUpgrade10,  priceUpgrade10, textUpgrade10 = widgetUpgrade10()
        dicVariable["levelUpgrade10"] = levelUpgrade10
        dicVariable["buttonUpgrade10"] = buttonUpgrade10
        dicVariable["priceUpgrade10"] = priceUpgrade10
        dicVariable["textUpgrade10"] = textUpgrade10
        dicVariable["rowUpgrade10"] = rowUpgrade10
        listAmelioration.append(10)
    elif max(listAmelioration) == 10:
        levelUpgrade11, buttonUpgrade11,  priceUpgrade11, textUpgrade11 = widgetUpgrade11()
        dicVariable["levelUpgrade11"] = levelUpgrade11
        dicVariable["buttonUpgrade11"] = buttonUpgrade11
        dicVariable["priceUpgrade11"] = priceUpgrade11
        dicVariable["textUpgrade11"] = textUpgrade11
        dicVariable["rowUpgrade11"] = rowUpgrade11
        listAmelioration.append(11)
    elif max(listAmelioration) == 11:
        levelUpgrade12, buttonUpgrade12,  priceUpgrade12, textUpgrade12 = widgetUpgrade12()
        dicVariable["levelUpgrade12"] = levelUpgrade12
        dicVariable["buttonUpgrade12"] = buttonUpgrade12
        dicVariable["priceUpgrade12"] = priceUpgrade12
        dicVariable["textUpgrade12"] = textUpgrade12
        dicVariable["rowUpgrade12"] = rowUpgrade12
        listAmelioration.append(12)
    elif max(listAmelioration) == 12:
        levelUpgrade13, buttonUpgrade13,  priceUpgrade13, textUpgrade13 = widgetUpgrade13()
        dicVariable["levelUpgrade13"] = levelUpgrade13
        dicVariable["buttonUpgrade13"] = buttonUpgrade13
        dicVariable["priceUpgrade13"] = priceUpgrade13
        dicVariable["textUpgrade13"] = textUpgrade13
        dicVariable["rowUpgrade13"] = rowUpgrade13
        listAmelioration.append(13)
    elif max(listAmelioration) == 13:
        levelUpgrade14, buttonUpgrade14,  priceUpgrade14, textUpgrade14 = widgetUpgrade14()
        dicVariable["levelUpgrade14"] = levelUpgrade14
        dicVariable["buttonUpgrade14"] = buttonUpgrade14
        dicVariable["priceUpgrade14"] = priceUpgrade14
        dicVariable["textUpgrade14"] = textUpgrade14
        dicVariable["rowUpgrade14"] = rowUpgrade14
        listAmelioration.append(14)
    elif max(listAmelioration) == 14:
        levelUpgrade15, buttonUpgrade15,  priceUpgrade15, textUpgrade15 = widgetUpgrade15()
        dicVariable["levelUpgrade15"] = levelUpgrade15
        dicVariable["buttonUpgrade15"] = buttonUpgrade15
        dicVariable["priceUpgrade15"] = priceUpgrade15
        dicVariable["textUpgrade15"] = textUpgrade15
        dicVariable["rowUpgrade15"] = rowUpgrade15
        listAmelioration.append(15)
    elif max(listAmelioration) == 15:
        levelUpgrade16, buttonUpgrade16,  priceUpgrade16, textUpgrade16 = widgetUpgrade16()
        dicVariable["levelUpgrade16"] = levelUpgrade16
        dicVariable["buttonUpgrade16"] = buttonUpgrade16
        dicVariable["priceUpgrade16"] = priceUpgrade16
        dicVariable["textUpgrade16"] = textUpgrade16
        dicVariable["rowUpgrade16"] = rowUpgrade16
        listAmelioration.append(16)
    


def deleteBoost(niveau):
    global dicVariable
    global listBoost
    global buttonBoost6, buttonBoost7, buttonBoost8, buttonBoost9, buttonBoost10, buttonBoost11, buttonBoost12, buttonBoost13, buttonBoost14, buttonBoost15

    dicVariable[f"buttonBoost{niveau}"].destroy()
    for i in range(len(listBoost)):
        if listBoost[i] == niveau:
            for j in listBoost:
                if j > niveau:
                    dicVariable[f"columnBoost{j}"] -= 1
                    dicVariable[f"buttonBoost{j}"].grid(column=dicVariable[f"columnBoost{j}"])
            numADelete = i
    del(listBoost[numADelete])
    if max(listBoost) == 5:
        buttonBoost6=widgetBoost6()
        dicVariable["buttonBoost6"] = buttonBoost6
        listBoost.append(6)
    elif max(listBoost) == 6:
        buttonBoost7=widgetBoost7()
        dicVariable["buttonBoost7"] = buttonBoost7
        listBoost.append(7)
    elif max(listBoost) == 7:
        buttonBoost8=widgetBoost8()
        dicVariable["buttonBoost8"] = buttonBoost8
        listBoost.append(8)
    elif max(listBoost) == 8:
        buttonBoost9 = widgetBoost9()
        dicVariable["buttonBoost9"] = buttonBoost9
        listBoost.append(9)
    elif max(listBoost) == 9:
        buttonBoost10 = widgetBoost10()
        dicVariable["buttonBoost10"] = buttonBoost10
        listBoost.append(10)
    elif max(listBoost) == 10:
        buttonBoost11 = widgetBoost11()
        dicVariable["buttonBoost11"] = buttonBoost11
        listBoost.append(11)
    elif max(listBoost) == 11:
        buttonBoost12 = widgetBoost12()
        dicVariable["buttonBoost12"] = buttonBoost12
        listBoost.append(12)
    elif max(listBoost) == 12:
        buttonBoost13 = widgetBoost13()
        dicVariable["buttonBoost13"] = buttonBoost13
        listBoost.append(13)
    elif max(listBoost) == 13:
        buttonBoost14 = widgetBoost14()
        dicVariable["buttonBoost14"] = buttonBoost14
        listBoost.append(14)
    elif max(listBoost) == 14:
        buttonBoost15 = widgetBoost15()
        dicVariable["buttonBoost15"] = buttonBoost15
        listBoost.append(15)
    print(listBoost)




def Amelioration1Clic():
    global scoreSec
    global score
    global niveau_amelioration1
    global levelUpgrade1
    if niveau_amelioration1 <= 49:
        if score >= prix_amelioration_1[niveau_amelioration1]:
            niveau_amelioration1 += 1
            scoreSec = round(scoreSec + 0.1, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score= round(score-prix_amelioration_1[niveau_amelioration1 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration1 == 50:
                levelUpgrade1.configure(text="MAX")
                priceUpgrade1.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[1])
                th2.start()
            else:
                levelUpgrade1.configure(text=niveau_amelioration1)
                priceUpgrade1.configure(text=f"prix : {prix_amelioration_1[niveau_amelioration1]}")


def Amelioration2Clic():
    global scoreSec
    global score
    global niveau_amelioration2
    global levelUpgrade2
    if niveau_amelioration2 <= 49:
        if score >= prix_amelioration_2[niveau_amelioration2]:
            niveau_amelioration2 += 1
            scoreSec = round(scoreSec + 2, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score= round(score-prix_amelioration_2[niveau_amelioration2 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration2 == 50:
                levelUpgrade2.configure(text="MAX")
                priceUpgrade2.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[2])
                th2.start()
            else:
                levelUpgrade2.configure(text=niveau_amelioration2)
                priceUpgrade2.configure(text=f"prix : {prix_amelioration_2[niveau_amelioration2]}")

def Amelioration3Clic():
    global scoreSec
    global score
    global niveau_amelioration3
    global levelUpgrade3
    if niveau_amelioration3 <= 49:
        if score >= prix_amelioration_3[niveau_amelioration3]:
            niveau_amelioration3 += 1
            scoreSec = round(scoreSec + 8, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score= round(score-prix_amelioration_3[niveau_amelioration3 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration3 == 50:
                levelUpgrade3.configure(text="MAX")
                priceUpgrade3.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[3])
                th2.start()
            else:
                levelUpgrade3.configure(text=niveau_amelioration3)
                priceUpgrade3.configure(text=f"prix : {prix_amelioration_3[niveau_amelioration3]}")

def Amelioration4Clic():
    global scoreSec
    global score
    global niveau_amelioration4
    global levelUpgrade4
    if niveau_amelioration4 <= 49:
        if score >= prix_amelioration_4[niveau_amelioration4]:
            niveau_amelioration4 += 1
            scoreSec = round(scoreSec + 47, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score= round(score-prix_amelioration_4[niveau_amelioration4 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration4 == 50:
                levelUpgrade4.configure(text="MAX")
                priceUpgrade4.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[4])
                th2.start()
            else:
                levelUpgrade4.configure(text=niveau_amelioration4)
                priceUpgrade4.configure(text=f"prix : {prix_amelioration_4[niveau_amelioration4]}")

def Amelioration5Clic():
    global scoreSec
    global score
    global niveau_amelioration5
    global levelUpgrade5
    if niveau_amelioration5 <= 49:
        if score >= prix_amelioration_5[niveau_amelioration5]:
            niveau_amelioration5 += 1
            scoreSec = round(scoreSec + 260, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score = round(score - prix_amelioration_5[niveau_amelioration5 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration5 == 50:
                levelUpgrade5.configure(text="MAX")
                priceUpgrade5.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[5])
                th2.start()
            else:
                levelUpgrade5.configure(text=niveau_amelioration5)
                priceUpgrade5.configure(text=f"prix : {prix_amelioration_5[niveau_amelioration5]}")

def Amelioration6Clic():
    global scoreSec
    global score
    global niveau_amelioration6
    if niveau_amelioration6 <= 49:
        if score >= prix_amelioration_6[niveau_amelioration6]:
            niveau_amelioration6 += 1
            scoreSec = round(scoreSec + 1400, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score = round(score - prix_amelioration_6[niveau_amelioration6 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration6 == 50:
                levelUpgrade6.configure(text="MAX")
                priceUpgrade6.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[6])
                th2.start()
            else:
                levelUpgrade6.configure(text=niveau_amelioration6)
                priceUpgrade6.configure(text=f"prix : {prix_amelioration_6[niveau_amelioration6]}")

def Amelioration7Clic():
    global scoreSec
    global score
    global niveau_amelioration7
    if niveau_amelioration7 <= 49:
        if score >= prix_amelioration_7[niveau_amelioration7]:
            niveau_amelioration7 += 1
            scoreSec = round(scoreSec + 1400, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score = round(score - prix_amelioration_7[niveau_amelioration7 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration7 == 50:
                levelUpgrade7.configure(text="MAX")
                priceUpgrade7.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[7])
                th2.start()
            else:
                levelUpgrade7.configure(text=niveau_amelioration7)
                priceUpgrade7.configure(text=f"prix : {prix_amelioration_7[niveau_amelioration7]}")

def Amelioration8Clic():
    global scoreSec
    global score
    global niveau_amelioration8
    if niveau_amelioration8 <= 49:
        if score >= prix_amelioration_8[niveau_amelioration8]:
            niveau_amelioration8 += 1
            scoreSec = round(scoreSec + 1400, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score = round(score - prix_amelioration_8[niveau_amelioration8 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration8 == 50:
                levelUpgrade8.configure(text="MAX")
                priceUpgrade8.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[8])
                th2.start()
            else:
                levelUpgrade8.configure(text=niveau_amelioration8)
                priceUpgrade8.configure(text=f"prix : {prix_amelioration_8[niveau_amelioration8]}")

def Amelioration9Clic():
    global scoreSec
    global score
    global niveau_amelioration9
    if niveau_amelioration9 <= 49:
        if score >= prix_amelioration_9[niveau_amelioration9]:
            niveau_amelioration9 += 1
            scoreSec = round(scoreSec + 1400, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score = round(score - prix_amelioration_9[niveau_amelioration9 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration9 == 50:
                levelUpgrade9.configure(text="MAX")
                priceUpgrade9.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[9])
                th2.start()
            else:
                levelUpgrade9.configure(text=niveau_amelioration9)
                priceUpgrade9.configure(text=f"prix : {prix_amelioration_9[niveau_amelioration9]}")

def Amelioration10Clic():
    global scoreSec
    global score
    global niveau_amelioration10
    if niveau_amelioration10 <= 49:
        if score >= prix_amelioration_10[niveau_amelioration10]:
            niveau_amelioration10 += 1
            scoreSec = round(scoreSec + 1400, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score = round(score - prix_amelioration_10[niveau_amelioration10 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration10 == 50:
                levelUpgrade10.configure(text="MAX")
                priceUpgrade10.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[10])
                th2.start()
            else:
                levelUpgrade10.configure(text=niveau_amelioration10)
                priceUpgrade10.configure(text=f"prix : {prix_amelioration_10[niveau_amelioration10]}")

def Amelioration11Clic():
    global scoreSec
    global score
    global niveau_amelioration11
    if niveau_amelioration11 <= 49:
        if score >= prix_amelioration_11[niveau_amelioration11]:
            niveau_amelioration11 += 1
            scoreSec = round(scoreSec + 1400, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score = round(score - prix_amelioration_11[niveau_amelioration11 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration11 == 50:
                levelUpgrade11.configure(text="MAX")
                priceUpgrade11.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[11])
                th2.start()
            else:
                levelUpgrade11.configure(text=niveau_amelioration11)
                priceUpgrade11.configure(text=f"prix : {prix_amelioration_11[niveau_amelioration11]}")

def Amelioration12Clic():
    global scoreSec
    global score
    global niveau_amelioration12
    if niveau_amelioration12 <= 49:
        if score >= prix_amelioration_12[niveau_amelioration12]:
            niveau_amelioration12 += 1
            scoreSec = round(scoreSec + 1400, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score = round(score - prix_amelioration_12[niveau_amelioration12 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration12 == 50:
                levelUpgrade12.configure(text="MAX")
                priceUpgrade12.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[12])
                th2.start()
            else:
                levelUpgrade12.configure(text=niveau_amelioration12)
                priceUpgrade12.configure(text=f"prix : {prix_amelioration_12[niveau_amelioration12]}")

def Amelioration13Clic():
    global scoreSec
    global score
    global niveau_amelioration13
    if niveau_amelioration13 <= 49:
        if score >= prix_amelioration_13[niveau_amelioration13]:
            niveau_amelioration13 += 1
            scoreSec = round(scoreSec + 1400, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score = round(score - prix_amelioration_13[niveau_amelioration13 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration13 == 50:
                levelUpgrade13.configure(text="MAX")
                priceUpgrade13.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[13])
                th2.start()
            else:
                levelUpgrade13.configure(text=niveau_amelioration13)
                priceUpgrade13.configure(text=f"prix : {prix_amelioration_13[niveau_amelioration13]}")

def Amelioration14Clic():
    global scoreSec
    global score
    global niveau_amelioration14
    if niveau_amelioration14 <= 49:
        if score >= prix_amelioration_14[niveau_amelioration14]:
            niveau_amelioration14 += 1
            scoreSec = round(scoreSec + 1400, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score = round(score - prix_amelioration_14[niveau_amelioration14 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration14 == 50:
                levelUpgrade14.configure(text="MAX")
                priceUpgrade14.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[14])
                th2.start()
            else:
                levelUpgrade14.configure(text=niveau_amelioration14)
                priceUpgrade14.configure(text=f"prix : {prix_amelioration_14[niveau_amelioration14]}")

def Amelioration15Clic():
    global scoreSec
    global score
    global niveau_amelioration15
    if niveau_amelioration15 <= 49:
        if score >= prix_amelioration_15[niveau_amelioration15]:
            niveau_amelioration15 += 1
            scoreSec = round(scoreSec + 1400, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score = round(score - prix_amelioration_15[niveau_amelioration15 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration15 == 50:
                levelUpgrade15.configure(text="MAX")
                priceUpgrade15.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[15])
                th2.start()
            else:
                levelUpgrade15.configure(text=niveau_amelioration15)
                priceUpgrade15.configure(text=f"prix : {prix_amelioration_15[niveau_amelioration15]}")

def Amelioration16Clic():
    global scoreSec
    global score
    global niveau_amelioration16
    if niveau_amelioration16 <= 49:
        if score >= prix_amelioration_16[niveau_amelioration16]:
            niveau_amelioration16 += 1
            scoreSec = round(scoreSec + 1400, 1)
            text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")
            score = round(score - prix_amelioration_16[niveau_amelioration16 - 1], 1)
            text_score.configure(text=f"{score} octets")
            if niveau_amelioration16 == 50:
                levelUpgrade16.configure(text="MAX")
                priceUpgrade16.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[16])
                th2.start()
            else:
                levelUpgrade16.configure(text=niveau_amelioration16)
                priceUpgrade16.configure(text=f"prix : {prix_amelioration_16[niveau_amelioration16]}")

def Boost1Clic():
    global scoreClick
    global score
    if score >= prix_boost1:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost1
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[1])
        th3.start()

def Boost2Clic():
    global scoreClick
    global score
    if score >= prix_boost2:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost2
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[2])
        th3.start()

def Boost3Clic():
    global scoreClick
    global score
    if score >= prix_boost3:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost3
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[3])
        th3.start()
        
def Boost4Clic():
    global scoreClick
    global score
    if score >= prix_boost4:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost4
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[4])
        th3.start()
        
def Boost5Clic():
    global scoreClick
    global score
    if score >= prix_boost5:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost5
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[5])
        th3.start()
        
def Boost6Clic():
    global scoreClick
    global score
    if score >= prix_boost6:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost6
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[6])
        th3.start()
        
def Boost7Clic():
    global scoreClick
    global score
    if score >= prix_boost7:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost7
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[7])
        th3.start()

def Boost8Clic():
    global scoreClick
    global score
    if score >= prix_boost8:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost8
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[8])
        th3.start()

def Boost9Clic():
    global scoreClick
    global score
    if score >= prix_boost9:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost9
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[9])
        th3.start()

def Boost10Clic():
    global scoreClick
    global score
    if score >= prix_boost10:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost10
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[10])
        th3.start()

def Boost11Clic():
    global scoreClick
    global score
    if score >= prix_boost11:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost11
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[11])
        th3.start()

def Boost12Clic():
    global scoreClick
    global score
    if score >= prix_boost12:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost12
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[12])
        th3.start()

def Boost13Clic():
    global scoreClick
    global score
    if score >= prix_boost13:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost13
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[13])
        th3.start()

def Boost14Clic():
    global scoreClick
    global score
    if score >= prix_boost14:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost14
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[14])
        th3.start()

def Boost15Clic():
    global scoreClick
    global score
    if score >= prix_boost15:
        scoreClick = scoreClick*2
        text_octets_click.configure(text=f"Par Click : {scoreClick}")
        score=score-prix_boost15
        text_score.configure(text=f"{score} notes")
        th3 = threading.Thread(target=deleteBoost, args=[15])
        th3.start()

def prix(prix_base):
    a = [prix_base]
    for i in range(50):
        a.append(int(a[i]*1.15))
    return a
#---------------------------------------------------------Provisoire---------------------------------------

def point1k(event):
    global score
    score += 10000000000000
    text_score.configure(text=f"{score} octets")


def ptpclick(event):
    global scoreClick
    scoreClick += 200000000000
    text_octets_click.configure(text=f"{scoreClick} octets/Clic")

def ptpsecondes(event):
    global scoreSec
    scoreSec += 250000000000
    text_octets_secondes.configure(text=f"{scoreSec} octets/Secondes")


#----------------------------------------------------------------Main-----------------------------------------------------------------------------

scoreClick=1
scoreSec=0
score=0
dicImageBoost={}
listAmelioration = [1, 2, 3, 4, 5]
listBoost = [1, 2, 3, 4, 5]
rowUpgrade1 = 3
rowUpgrade2 = 5
rowUpgrade3 = 7
rowUpgrade4 = 9
rowUpgrade5 = 11
rowUpgrade6 = 11
rowUpgrade7 = 11
rowUpgrade8 = 11
rowUpgrade9 = 11
rowUpgrade10 = 11
rowUpgrade11 = 11
rowUpgrade12 = 11
rowUpgrade13 = 11
rowUpgrade14 = 11
rowUpgrade15 = 11
rowUpgrade16 = 11

columnBoost1 = 10
columnBoost2 = 11
columnBoost3 = 12
columnBoost4 = 13
columnBoost5 = 14
columnBoost6 = 14
columnBoost7 = 14
columnBoost8 = 14
columnBoost9 = 14
columnBoost10 = 14
columnBoost11 = 14
columnBoost12 = 14
columnBoost13 = 14
columnBoost14 = 14
columnBoost15 = 14

niveau_amelioration1 = 0
prix_amelioration_1 = prix(10)
niveau_amelioration2 = 0
prix_amelioration_2 = prix(100)
niveau_amelioration3 = 0
prix_amelioration_3 = prix(1_100)
niveau_amelioration4 = 0
prix_amelioration_4 = prix(12_000)
niveau_amelioration5 = 0
prix_amelioration_5 = prix(130_000)
niveau_amelioration6 = 0
prix_amelioration_6 = prix(1_400_000)
niveau_amelioration7 = 0
prix_amelioration_7 = prix(20_000_000)
niveau_amelioration8 = 0
prix_amelioration_8 = prix(330_000_000)
niveau_amelioration9 = 0
prix_amelioration_9 = prix(5_100_000_000)
niveau_amelioration10 = 0
prix_amelioration_10 = prix(75_000_000_000)
niveau_amelioration11 = 0
prix_amelioration_11 = prix(1_000_000_000_000)
niveau_amelioration12 = 0
prix_amelioration_12 = prix(14_000_000_000_000)
niveau_amelioration13 = 0
prix_amelioration_13 = prix(170_000_000_000_000)
niveau_amelioration14 = 0
prix_amelioration_14 = prix(2_100_000_000_000_000)
niveau_amelioration15 = 0
prix_amelioration_15 = prix(26_000_000_000_000_000)
niveau_amelioration16 = 0
prix_amelioration_16 = prix(310_000_000_000_000_000)

prix_boost1=100
prix_boost2=500
prix_boost3=1000
prix_boost4=5000
prix_boost5=10000
prix_boost6=11000
prix_boost7=50000
prix_boost8=50000
prix_boost9=55000
prix_boost10=55000
prix_boost11=120000
prix_boost12=550000
prix_boost13=600000
prix_boost14=600000
prix_boost15=999999

#a mdifier pour 1 seul écran
fenetre_pop_up, text_popup, prenom_user, bouton_valider_popup = pop_up()
fenetre_pop_up.mainloop()

lastSave = start() #a modifier pour recup dans le fichier sauvegarde
fenetre, screen_width, screen_height = creer_fenetre()
zone_graphique = creer_Canvas()
text_player, picture, button_clicker, text_last_save, text_score, text_octets_secondes, text_octets_click, button_save, button_save_quit =  cree_widget()

pictureUpgrade1,  pictureUpgrade2, pictureUpgrade3, pictureUpgrade4, pictureUpgrade5,  pictureUpgrade6, pictureUpgrade7, pictureUpgrade8, pictureUpgrade9, pictureUpgrade10, pictureUpgrade11, pictureUpgrade12, pictureUpgrade13, pictureUpgrade14, pictureUpgrade15, pictureUpgrade16, pictureBoost1, pictureBoost2, pictureBoost3, pictureBoost4, pictureBoost5, pictureBoost6, pictureBoost7, pictureBoost8, pictureBoost9, pictureBoost10, pictureBoost11, pictureBoost12, pictureBoost13, pictureBoost14, pictureBoost15 = load_picture()
levelUpgrade1, buttonUpgrade1, priceUpgrade1, textUpgrade1 = widgetUpgrade1()
levelUpgrade2, buttonUpgrade2, priceUpgrade2, textUpgrade2 = widgetUpgrade2()
levelUpgrade3, buttonUpgrade3, priceUpgrade3, textUpgrade3 = widgetUpgrade3()
levelUpgrade4, buttonUpgrade4, priceUpgrade4, textUpgrade4 = widgetUpgrade4()
levelUpgrade5, buttonUpgrade5, priceUpgrade5, textUpgrade5 = widgetUpgrade5()

buttonBoost1=widgetBoost1()
buttonBoost2=widgetBoost2()
buttonBoost3=widgetBoost3()
buttonBoost4=widgetBoost4()
buttonBoost5=widgetBoost5()
buttonBoost6=widgetBoost6()
buttonBoost7=widgetBoost7()
buttonBoost8=widgetBoost8()
buttonBoost9=widgetBoost9()
buttonBoost10=widgetBoost10()
buttonBoost11=widgetBoost11()
buttonBoost12=widgetBoost12()
buttonBoost13=widgetBoost13()
buttonBoost14=widgetBoost14()
buttonBoost15=widgetBoost15()

dicVariable={"levelUpgrade1" : levelUpgrade1, "buttonUpgrade1" : buttonUpgrade1, "priceUpgrade1" : priceUpgrade1, "textUpgrade1" : textUpgrade1, "rowUpgrade1" : rowUpgrade1, "levelUpgrade2" : levelUpgrade2, "buttonUpgrade2" : buttonUpgrade2, "priceUpgrade2" : priceUpgrade2, "textUpgrade2" : textUpgrade2, "rowUpgrade2" : rowUpgrade2, "levelUpgrade3" : levelUpgrade3, "buttonUpgrade3" : buttonUpgrade3, "priceUpgrade3" : priceUpgrade3, "textUpgrade3" : textUpgrade3, "rowUpgrade3" : rowUpgrade3, "levelUpgrade4" : levelUpgrade4, "buttonUpgrade4" : buttonUpgrade4, "priceUpgrade4" : priceUpgrade4, "textUpgrade4" : textUpgrade4, "rowUpgrade4" : rowUpgrade4, "levelUpgrade5" : levelUpgrade5, "buttonUpgrade5" : buttonUpgrade5, "priceUpgrade5" : priceUpgrade5, "textUpgrade5" : textUpgrade5, "rowUpgrade5" : rowUpgrade5, "buttonBoost1" : buttonBoost1, "buttonBoost2" : buttonBoost2, "buttonBoost3" : buttonBoost3, "buttonBoost4" : buttonBoost4, "buttonBoost5": buttonBoost5, "buttonBoost6": buttonBoost6, "buttonBoost7": buttonBoost7, "buttonBoost8": buttonBoost8, "buttonBoost9": buttonBoost9, "buttonBoost10": buttonBoost10, "buttonBoost11": buttonBoost11,  "buttonBoost12": buttonBoost12, "buttonBoost13": buttonBoost13, "buttonBoost14": buttonBoost14, "buttonBoost15": buttonBoost15, "columnBoost1" : columnBoost1, "columnBoost2" : columnBoost2, "columnBoost3" : columnBoost3, "columnBoost4" : columnBoost4, "columnBoost5" : columnBoost5, "columnBoost6" : columnBoost6, "columnBoost7" : columnBoost7, "columnBoost8" : columnBoost8, "columnBoost9" : columnBoost9, "columnBoost10" : columnBoost10, "columnBoost11" : columnBoost11, "columnBoost12" : columnBoost12, "columnBoost13" : columnBoost13, "columnBoost14" : columnBoost14, "columnBoost15" : columnBoost15}



# activation commandes admin
fenetre.bind("<Up>", point1k)
fenetre.bind("<Left>", ptpclick)
fenetre.bind("<Right>", ptpsecondes)




# Gestion du multithread pour les clic/sec
th1 = threading.Thread(target=MajScoreSec)
th1.daemon = True
th1.start()

fenetre.mainloop()