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




import tkinter as tk

root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# Create a frame for the canvas with non-zero row&column weights
frame_canvas = tk.Frame(root)
frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)
# Set grid_propagate to False to allow 5-by-5 buttons resizing later
frame_canvas.grid_propagate(False)

# Add a canvas in that frame
canvas = tk.Canvas(frame_canvas, bg="yellow")
canvas.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

# Create a frame to contain the buttons
frame_buttons = tk.Frame(canvas, bg="blue")
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

btn=tk.Button(frame_buttons).grid(row=0,column=0, sticky='news')

# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"))

# Launch the GUI
root.mainloop()


"""
import tkinter as tk

root = tk.Tk()

frame_canvas = tk.Frame(root)
frame_canvas.grid(row=2, column=0, sticky='nw')

# Add a canvas in that frame
canvas = tk.Canvas(frame_canvas, bg="yellow")
canvas.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

# Create a frame to contain the buttons
frame_buttons = tk.Frame(canvas, bg="blue")
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

btn=tk.Button(frame_buttons, width=5, height=2)

canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
"""