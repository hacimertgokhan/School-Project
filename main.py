import tkinter as tk
import random as random
from tkinter import messagebox
from PIL import Image, ImageTk

pencere=tk.Tk()
pencere.geometry("1280x720")

path = "human.gif"

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(pencere, image = img)

panel.pack(side = "bottom", fill = "both")

pencere.title("For Deutschland")

etiket1=tk.Label(pencere,text="Almanca eğitim & öğrenme projesi" ,font="Arial", bg="#7BA5A5")
etiket1.pack()


def dialog():
    randomRakam = random.randint(1,3)
    rastgeledeger = liste.get(randomRakam)
    var = messagebox.showinfo("Şansına çıkan kelime", rastgeledeger)

button1 = tk.Button(pencere, text=" Rastgele kelime ", width=20, command=dialog)
button1.pack(side="bottom")

liste = tk.Listbox(pencere, width=35, height=30, font="Arial",bg="gray",fg="white",relief="raised",selectmode="extended")
liste.pack(side="top")
liste.insert(1,"")
liste.insert(2,"Pardus Linux")
liste.insert(3,"Ubuntu Linux")
liste.insert(4,"Milis Linux")
liste.insert(5,"Linux Mint")
liste.pack()

pencere.mainloop()