def points(points):
    terminaison = ["octets", "Ko", "Mo", "Go", "To", "Po", "Eo", "Zo", "Yo", "Ro", "Qo"]
    al="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        text = al[i]
        terminaison.append(text)
    for i in range(26):
        for j in range(26):
            text = ""
            text += (al[i])
            text += (al[j])
            terminaison.append(text)
    k = 0
    while points > 999:
        points = points / 1000
        k += 1
    points = round(points, 2)
    texte = f"{points} {terminaison[k]}"
    return(texte)

print(points(10000000))




from tkinter import *

fenetre = Tk()
fenetre.grid_rowconfigure(0, weight=1)
fenetre.grid_columnconfigure(0, weight=1)
    
zoneUpgrade=Canvas(fenetre)
zoneUpgrade.grid(row=0, column=0, sticky="nswe")
    
vScroll=Scrollbar(fenetre, orient=VERTICAL, command=zoneUpgrade.yview)
vScroll.grid(row=0, column=1, sticky="ns")
    
zoneUpgrade.configure(yscrollcommand=vScroll.set)
    
frm=Frame(zoneUpgrade)
    
for i in range(50):
    Label(frm, text="Label%s " % i).grid(row=i, column=0)
        
frm.update()
    
zoneUpgrade.create_window(0,0,window=frm, anchor=NW)
    
zoneUpgrade.configure(scrollregion=zoneUpgrade.bbox(ALL))

fenetre.mainloop()