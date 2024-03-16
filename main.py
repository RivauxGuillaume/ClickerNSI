import glob
import time
from tkinter import Tk, Canvas, Label, Button, Text, PhotoImage
import threading
from PIL import *
import datetime

#----------------------------------------------------------------Fonction---------------------------------------------------------------------------

def creer_fenetre():
    fenetre=Tk()
    
    fenetre.title("Computer Clicker")
    screen_width = fenetre.winfo_screenwidth()
    screen_height = fenetre.winfo_screenheight()
    fenetre.attributes('-fullscreen', True)
    for i in range(15):
        fenetre.columnconfigure(i, minsize=int(screen_width/16), pad=0)
        fenetre.rowconfigure(i, minsize=int(screen_height/16), pad=0)
    return fenetre, screen_width, screen_height

def creer_Canvas():
    zone_graphique = Canvas(fenetre, width=screen_width, height=screen_height, bg = "black", border=0, borderwidth=0)
    zone_graphique.grid(row=0, column=0, rowspan=15, columnspan=15)

    return zone_graphique

def cree_widget():
    # Joueur qui joue
    text_player = Label(fenetre, text=f"Joueur : {joueur}", bg="black", fg="white")
    text_player.grid(row=0, column=0)

    # Bouton clicker
    picture = PhotoImage(file="ordi2.png")
    button_clicker = Button(fenetre, image=picture, command=AjoutScore, bg = "black", activebackground="black", bd=0)
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
    button_save = Button(fenetre, bg="black", activebackground="black", bd=5, command=save, text="Sauvegarder la\nprogression", fg="white", font="Helvetica 12")
    button_save.grid(row=7, column=7, rowspan=2, columnspan=3)

    # Bouton pour sauvegarder et quitter
    button_save_quit = Button(fenetre, bg="black", activebackground="black", bd=5, command=save_and_quit, text="Sauvegarder et\nquitter", fg="white", font="Helvetica 12")
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

def load_picture():
    pictureUpgrade1 = PhotoImage(file="image/python.png")
    pictureUpgrade2 = PhotoImage(file="image/html.png")
    pictureUpgrade3 = PhotoImage(file="image/python.png")
    pictureUpgrade4 = PhotoImage(file="image/python.png")
    pictureUpgrade5 = PhotoImage(file="image/python.png")
    pictureUpgrade6 = PhotoImage(file="image/python.png")

    return pictureUpgrade1,  pictureUpgrade2, pictureUpgrade3, pictureUpgrade4, pictureUpgrade5,  pictureUpgrade6

def widgetUpgrade1():
    global pictureUpgrade1
    levelUpgrade1 = Label(fenetre, text="0", bg="black", fg="grey", font=("Arial",  18))
    levelUpgrade1.grid(row=rowUpgrade1, column=10, rowspan=2)

    buttonUpgrade1 = Button(fenetre, image=pictureUpgrade1, bg="black", activebackground="black", command=Amelioration1Clic, width=60, height=60)
    buttonUpgrade1.grid(row=rowUpgrade1, column=11, rowspan=2)

    priceUpgrade1 = Label(fenetre, text="prix : 10", bg="black", fg="white")
    priceUpgrade1.grid(row=rowUpgrade1, column=12, rowspan=2)

    textUpgrade1 = Label(fenetre, text="augmente de 0.1\nle nombre d'octets\npar secondes", bg="black", fg="white", font="Helvetica 10")
    textUpgrade1.grid(row=rowUpgrade1, column=13, rowspan=2)

    return levelUpgrade1, buttonUpgrade1, priceUpgrade1, textUpgrade1

def widgetUpgrade2():
    global pictureUpgrade2
    levelUpgrade2 = Label(fenetre, text="0", bg="black", fg="grey", font=("Arial",  18))
    levelUpgrade2.grid(row=rowUpgrade2, column=10, rowspan=2)

    buttonUpgrade2 = Button(fenetre, image=pictureUpgrade2, bg="black", activebackground="black", command=Amelioration2Clic, width=60, height=60)
    buttonUpgrade2.grid(row=rowUpgrade2, column=11, rowspan=2)

    priceUpgrade2 = Label(fenetre, text="prix : 100", bg="black", fg="white")
    priceUpgrade2.grid(row=rowUpgrade2, column=12, rowspan=2)

    textUpgrade2 = Label(fenetre, text="augmente de 2\nle nombre d'octets\npar secondes", bg="black", fg="white", font="Helvetica 10")
    textUpgrade2.grid(row=rowUpgrade2, column=13, rowspan=2)

    return levelUpgrade2, buttonUpgrade2, priceUpgrade2, textUpgrade2

def widgetUpgrade3():
    global pictureUpgrade3
    levelUpgrade3 = Label(fenetre, text="0", bg="black", fg="grey", font=("Arial",  18))
    levelUpgrade3.grid(row=rowUpgrade3, column=10, rowspan=2)

    buttonUpgrade3 = Button(fenetre, image=pictureUpgrade3, bg="black", activebackground="black", command=Amelioration3Clic, width=60, height=60)
    buttonUpgrade3.grid(row=rowUpgrade3, column=11, rowspan=2)

    priceUpgrade3 = Label(fenetre, text="prix : 1 100", bg="black", fg="white")
    priceUpgrade3.grid(row=rowUpgrade3, column=12, rowspan=2)

    textUpgrade3 = Label(fenetre, text="augmente de 8\nle nombre d'octets\npar secondes", bg="black", fg="white", font="Helvetica 10")
    textUpgrade3.grid(row=rowUpgrade3, column=13, rowspan=2)

    return levelUpgrade3, buttonUpgrade3, priceUpgrade3, textUpgrade3

def widgetUpgrade4():
    global pictureUpgrade4
    levelUpgrade4 = Label(fenetre, text="0", bg="black", fg="grey", font=("Arial",  18))
    levelUpgrade4.grid(row=rowUpgrade4, column=10, rowspan=2)

    buttonUpgrade4 = Button(fenetre, image=pictureUpgrade4, bg="black", activebackground="black", command=Amelioration4Clic, width=60, height=60)
    buttonUpgrade4.grid(row=rowUpgrade4, column=11, rowspan=2)

    priceUpgrade4 = Label(fenetre, text="prix : 12 000", bg="black", fg="white")
    priceUpgrade4.grid(row=rowUpgrade4, column=12, rowspan=2)

    textUpgrade4 = Label(fenetre, text="augmente de 47\nle nombre d'octets\npar secondes", bg="black", fg="white", font="Helvetica 10")
    textUpgrade4.grid(row=rowUpgrade4, column=13, rowspan=2)

    return levelUpgrade4, buttonUpgrade4, priceUpgrade4, textUpgrade4

def widgetUpgrade5():
    global pictureUpgrade5
    levelUpgrade5 = Label(fenetre, text="0", bg="black", fg="grey", font=("Arial",  18))
    levelUpgrade5.grid(row=rowUpgrade5, column=10, rowspan=2)

    pictureUpgrade5 = PhotoImage(file="image/python.png")
    buttonUpgrade5 = Button(fenetre, image=pictureUpgrade5, bg="black", activebackground="black", command=Amelioration5Clic, width=60, height=60)
    buttonUpgrade5.grid(row=rowUpgrade5, column=11, rowspan=2)

    priceUpgrade5 = Label(fenetre, text="prix : 130 000", bg="black", fg="white")
    priceUpgrade5.grid(row=rowUpgrade5, column=12, rowspan=2)

    textUpgrade5 = Label(fenetre, text="augmente de 260\nle nombre d'octets\npar secondes", bg="black", fg="white", font="Helvetica 10")
    textUpgrade5.grid(row=rowUpgrade5, column=13, rowspan=2)

    return levelUpgrade5, buttonUpgrade5, priceUpgrade5, textUpgrade5

def widgetUpgrade6():
    global pictureUpgrade6
    levelUpgrade6 = Label(fenetre, text="0", bg="black", fg="grey", font=("Arial",  18))
    levelUpgrade6.grid(row=rowUpgrade6, column=10, rowspan=2)

    pictureUpgrade6 = PhotoImage(file="image/python.png")
    buttonUpgrade6 = Button(fenetre, image=pictureUpgrade6, bg="black", activebackground="black", command=Amelioration6Clic, width=60, height=60)
    buttonUpgrade6.grid(row=rowUpgrade6, column=11, rowspan=2)

    priceUpgrade6 = Label(fenetre, text="prix : 1 400 000", bg="black", fg="white")
    priceUpgrade6.grid(row=rowUpgrade6, column=12, rowspan=2)

    textUpgrade6 = Label(fenetre, text="augmente de 1400\nle nombre d'octets\npar secondes", bg="black", fg="white", font="Helvetica 10")
    textUpgrade6.grid(row=rowUpgrade6, column=13, rowspan=2)

    return levelUpgrade6, buttonUpgrade6, priceUpgrade6, textUpgrade6


def widgetBoost():
    pictureBoost1 = PhotoImage(file="image/python.png")
    buttonBoost1=Button(fenetre, image=pictureBoost1, bg="black", activebackground="black", width=60, height=60)
    buttonBoost1.grid(row=1, column=10)

    pictureBoost2 = PhotoImage(file="image/python.png")
    buttonBoost2=Button(fenetre, image=pictureBoost1, bg="black", activebackground="black", width=60, height=60)
    buttonBoost2.grid(row=1, column=11)

    pictureBoost3 = PhotoImage(file="image/python.png")
    buttonBoost3=Button(fenetre, image=pictureBoost1, bg="black", activebackground="black", width=60, height=60)
    buttonBoost3.grid(row=1, column=12)

    pictureBoost4 = PhotoImage(file="image/python.png")
    buttonBoost4=Button(fenetre, image=pictureBoost1, bg="black", activebackground="black", width=60, height=60)
    buttonBoost4.grid(row=1, column=13)

    pictureBoost5 = PhotoImage(file="image/python.png")
    buttonBoost5=Button(fenetre, image=pictureBoost1, bg="black", activebackground="black", width=60, height=60)
    buttonBoost5.grid(row=1, column=14)
    return buttonBoost1, pictureBoost1

def deleteAmelioration(niveau):
    global dicVariable
    global listAmelioration
    global ameliorationMaxAficher
    global levelUpgrade6, buttonUpgrade6, priceUpgrade6, textUpgrade6

    time.sleep(5)
    dicVariable[f"levelUpgrade{niveau}"].destroy()
    dicVariable[f"buttonUpgrade{niveau}"].destroy()
    dicVariable[f"priceUpgrade{niveau}"].destroy()
    dicVariable[f"textUpgrade{niveau}"].destroy()
    for i in range(len(listAmelioration)):
        if listAmelioration[i] == niveau:
            for j in listAmelioration:
                if j > listAmelioration[i]:
                    dicVariable[f"levelUpgrade{j}"].grid(row=dicVariable[f"rowUpgrade{j}"]-2)
                    dicVariable[f"buttonUpgrade{j}"].grid(row=dicVariable[f"rowUpgrade{j}"]-2)
                    dicVariable[f"priceUpgrade{j}"].grid(row=dicVariable[f"rowUpgrade{j}"]-2)
                    dicVariable[f"textUpgrade{j}"].grid(row=dicVariable[f"rowUpgrade{j}"]-2)
            numADelete = i
    del(listAmelioration[numADelete])
    if ameliorationMaxAficher == 5:
        levelUpgrade6, buttonUpgrade6,  priceUpgrade6, textUpgrade6 = widgetUpgrade6()
        dicVariable["levelUpgrade6"] = levelUpgrade6
        dicVariable["buttonUpgrade6"] = buttonUpgrade6
        dicVariable["priceUpgrade6"] = priceUpgrade6
        dicVariable["textUpgrade6"] = textUpgrade6
        dicVariable["rowUpgrade6"] = rowUpgrade6
    ameliorationMaxAficher += 1
    

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
            text_score.configure(text=f"{score} notes")
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
            text_score.configure(text=f"{score} notes")
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
            text_score.configure(text=f"{score} notes")
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
            text_score.configure(text=f"{score} notes")
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
            text_score.configure(text=f"{score} notes")
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
            text_score.configure(text=f"{score} notes")
            if niveau_amelioration6 == 50:
                levelUpgrade6.configure(text="MAX")
                priceUpgrade6.configure(text=f"niveau max\natteint")
                th2 = threading.Thread(target=deleteAmelioration, args=[6])
                th2.start()
            else:
                levelUpgrade6.configure(text=niveau_amelioration6)
                priceUpgrade6.configure(text=f"prix : {prix_amelioration_6[niveau_amelioration6]}")

#---------------------------------------------------------Provisoire---------------------------------------

def point1k(event):
    global score
    score += 10000000000000
    text_score.configure(text=f"{score} notes")


def ptpclick(event):
    global scoreClick
    scoreClick += 200000000000
    text_octets_click.configure(text=f"{scoreClick} notes/Clic")

def ptpsecondes(event):
    global scoreSec
    scoreSec += 250000000000
    text_octets_secondes.configure(text=f"{scoreSec} notes/Secondes")


#----------------------------------------------------------------Main-----------------------------------------------------------------------------

scoreClick=1
scoreSec=0
score=0
dicImageBoost={}
dicVariable={}
listAmelioration = [1, 2, 3, 4, 5]
ameliorationMaxAficher = 5
rowUpgrade1 = 3
rowUpgrade2 = 5
rowUpgrade3 = 7
rowUpgrade4 = 9
rowUpgrade5 = 11
rowUpgrade6 = 11

niveau_amelioration1 = 0
prix_amelioration_1 = [10, 12, 14, 17, 21, 25, 30, 36, 43, 52, 62, 75, 90, 107, 129, 155, 186, 223, 267, 321, 385, 462, 554, 665, 798, 957, 1149, 1378, 1654, 1985, 2381, 2858, 3429, 4115, 4938, 5926, 7111, 8534, 10240, 12288, 14746, 17695, 21234, 25481, 30578, 36693, 44032, 52838, 63406, 76087]
niveau_amelioration2 = 0
prix_amelioration_2 = [100, 115, 132, 152, 174, 201, 231, 266, 305, 351, 404, 465, 535, 615, 707, 813, 935, 1076, 1237, 1423, 1636, 1882, 2164, 2489, 2862, 3291, 3785, 4353, 5006, 5757, 6621, 7614, 8756, 10069, 11580, 13317, 15315, 17612, 20254, 23292, 26786, 30804, 35424, 40738, 46849, 53876, 61958, 71252, 81940, 94231]
niveau_amelioration3 = 0
prix_amelioration_3 = [1100, 1265, 1454, 1672, 1923, 2212, 2544, 2926, 3364, 3869, 4450, 5117, 5885, 6768, 7783, 8950, 10293, 11837, 13612, 15654, 18003, 20703, 23809, 27380, 31487, 36210, 41642, 47888, 55072, 63332, 72832, 83757, 96321, 110769, 127385, 146493, 168467, 193737, 222797, 256217, 294649, 338847, 389674, 448125, 515344, 592646, 681543, 783774, 901340, 1036541]
niveau_amelioration4 = 0
prix_amelioration_4 = [12000, 13799, 15869, 18250, 20988, 24136, 27756, 31920, 36708, 42214, 48546, 55828, 64203, 73833, 84908, 97644, 112291, 129135, 148505, 170781, 196398, 225858, 259736, 298697, 343502, 395027, 454281, 522423, 600787, 690905, 794541, 913722, 1050780, 1208397, 1389657, 1598106, 1837822, 2113495, 2430519, 2795097, 3214362, 3696516, 4250994, 4888643, 5621940, 6465231, 7435015, 8550268, 9832808, 11307729]
niveau_amelioration5 = 0
prix_amelioration_5 = [130000, 149490, 171920, 197710, 227370, 261470, 300690, 345800, 397670, 457320, 525920, 604810, 695530, 799860, 919840, 1057810, 1216490, 1398960, 1608800, 1850130, 2127640, 244679, 2813810, 3235880, 3721270, 4279460, 4921380, 5659590, 6508520, 7484800, 8607530, 9898650, 11383450, 13090970, 15054620, 17312810, 19909740, 22896200, 26330630, 30280220, 34822260, 40045600, 46052440, 52960300, 60904350, 70040000, 80546000, 92627900, 106522090, 122500400]
niveau_amelioration6 = 0
prix_amelioration_6 = [1400000, 1609999, 1851498, 2129222, 2448605, 2815895, 3238279, 3724020, 4282623, 4925016, 5663768, 6513333, 7490332, 8613881, 9905963, 11391857, 13100635, 15065730, 17325589, 19924427, 22913091, 26350054, 30302562, 34847946, 40075137, 46086407, 52999368, 60949273, 70091663, 80605412, 92696223, 106600656, 122590754, 140979367, 162126272, 186445212, 214411993, 246573791, 283559859, 326093837, 375007912, 431259098, 495947962, 570340156, 655891179, 754274855, 867416083, 997528495, 1147157769, 1319231434, 1517116149]


fenetre_pop_up, text_popup, prenom_user, bouton_valider_popup = pop_up()
fenetre_pop_up.mainloop()

lastSave = start()
fenetre, screen_width, screen_height = creer_fenetre()
zone_graphique = creer_Canvas()
text_player, picture, button_clicker, text_last_save, text_score, text_octets_secondes, text_octets_click, button_save, button_save_quit =  cree_widget()

pictureUpgrade1,  pictureUpgrade2, pictureUpgrade3, pictureUpgrade4, pictureUpgrade5,  pictureUpgrade6 = load_picture()
levelUpgrade1, buttonUpgrade1, priceUpgrade1, textUpgrade1 = widgetUpgrade1()
levelUpgrade2, buttonUpgrade2, priceUpgrade2, textUpgrade2 = widgetUpgrade2()
levelUpgrade3, buttonUpgrade3, priceUpgrade3, textUpgrade3 = widgetUpgrade3()
levelUpgrade4, buttonUpgrade4, priceUpgrade4, textUpgrade4 = widgetUpgrade4()
levelUpgrade5, buttonUpgrade5, priceUpgrade5, textUpgrade5 = widgetUpgrade5()
# global levelUpgrade6, buttonUpgrade6, priceUpgrade6, textUpgrade6

dicVariable["levelUpgrade1"] = levelUpgrade1
dicVariable["buttonUpgrade1"] = buttonUpgrade1
dicVariable["priceUpgrade1"] = priceUpgrade1
dicVariable["textUpgrade1"] = textUpgrade1
dicVariable["rowUpgrade1"] = rowUpgrade1
dicVariable["levelUpgrade2"] = levelUpgrade2
dicVariable["buttonUpgrade2"] = buttonUpgrade2
dicVariable["priceUpgrade2"] = priceUpgrade2
dicVariable["textUpgrade2"] = textUpgrade2
dicVariable["rowUpgrade2"] = rowUpgrade2
dicVariable["levelUpgrade3"] = levelUpgrade3
dicVariable["buttonUpgrade3"] = buttonUpgrade3
dicVariable["priceUpgrade3"] = priceUpgrade3
dicVariable["textUpgrade3"] = textUpgrade3
dicVariable["rowUpgrade3"] = rowUpgrade3
dicVariable["levelUpgrade4"] = levelUpgrade4
dicVariable["buttonUpgrade4"] = buttonUpgrade4
dicVariable["priceUpgrade4"] = priceUpgrade4
dicVariable["textUpgrade4"] = textUpgrade4
dicVariable["rowUpgrade4"] = rowUpgrade4
dicVariable["levelUpgrade5"] = levelUpgrade5
dicVariable["buttonUpgrade5"] = buttonUpgrade5
dicVariable["priceUpgrade5"] = priceUpgrade5
dicVariable["textUpgrade5"] = textUpgrade5
dicVariable["rowUpgrade5"] = rowUpgrade5

ButtonBoost1, pictureBoost1=widgetBoost()



# activation commandes admin
fenetre.bind("<Up>", point1k)
fenetre.bind("<Left>", ptpclick)
fenetre.bind("<Right>", ptpsecondes)



# Gestion du multithread pour les clic/sec
th1 = threading.Thread(target=MajScoreSec)
th1.daemon = True
th1.start()

fenetre.mainloop()
