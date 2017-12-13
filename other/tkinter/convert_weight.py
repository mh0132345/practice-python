from tkinter import *

window = Tk()

def convet_kg():
    kg = float(kg_value.get())
    gram = kg * 1000
    pound = kg * 2.20462
    ounce = kg * 35.274
    grams.insert(END, gram)
    pounds.insert(END, pound)
    ounces.insert(END, ounce)

lb = Label(window, text="Kg")
lb.grid(row=0, column=0)

kg_value = StringVar()
kg=Entry(window,textvariable=kg_value)
kg.grid(row=0, column=1)

b1 = Button(window, text="Execute", command=convet_kg)
b1.grid(row=0, column=2)

grams=Text(window, height=1, width=20)
grams.grid(row=1, column=0)

pounds=Text(window, height=1, width=20)
pounds.grid(row=1, column=1)

ounces=Text(window, height=1, width=20)
ounces.grid(row=1, column=2)

window.mainloop()
