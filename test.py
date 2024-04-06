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

window_screen = Tk()
window_screen.title('Codeunderscored')

theFrame = Frame(
    window_screen,
    width=500,
    height=400
    )
theFrame.pack(expand=True, fill=BOTH)

theCanvas=Canvas(
    theFrame,
    bg='#4A7A8C',
    width=500,
    height=400,
    scrollregion=(0,0,700,700)
    )

vertibar=Scrollbar(
    theFrame,
    orient=VERTICAL
    )
vertibar.pack(side=RIGHT,fill=Y)
vertibar.config(command=theCanvas.yview)


theCanvas.config(width=500,height=400)

theCanvas.config(
    yscrollcommand=vertibar.set
    )
theCanvas.pack(expand=True,side=LEFT,fill=BOTH)

window_screen.mainloop()
