"""
Goal :

"["1","10"]"
["1","1","0"]

<<<<<<< HEAD
"""

listboostBought = "['2', '3', '4']"

print(listboostBought)
if listboostBought == "[]":
    listboostBought = []
else:
    listboostBought = listboostBought[2:-2]
    listboostBought = listboostBought.split("""', '""")

print(listboostBought)
print(type(listboostBought))
=======



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
>>>>>>> ac91d0491048efe4b1f658f816bd3493e52fd56c
