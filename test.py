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

root=Tk()
frame=Frame(root,width=300,height=300)
frame.grid(row=0,column=0)
canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=300,height=300)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

root.mainloop()