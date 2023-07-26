import tkinter as tk

def update_info():
    name_text = nameentry.get()
    age_text = ageentry.get()
    infolabel.config(text=f"Name: {name_text}\nAge: {age_text}")

root = tk.Tk()
root.title("Adjustable Information GUI")

namelabel = tk.Label(root, text="name:")
namelabel.pack()
nameentry = tk.Entry(root)
nameentry.pack()

agelabel = tk.Label(root, text="Age:")
agelabel.pack()
ageentry= tk.Entry(root)
ageentry.pack()

infolabel = tk.Label(root, text="Name: \nAge:")
infolabel.pack()

root.mainloop()
