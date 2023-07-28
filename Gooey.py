import tkinter as tk

def calculate_time():
    elltime = int(entry.get())
    stime = (elltime - 5 + 12) % 24

    if stime > 12:
        resultoutput.config(text="AM")
    else:
        resultoutput.config(text="PM")

    stime %= 12
    if stime == 0:
        stime = 12

    resultoutput.config(text=f"{stime} USA eastern")

root = tk.Tk()
root.title("Elliot's Timezone Converter")

labels = tk.Label(text="Elliot's time")
labels.pack()

entry = tk.Entry(root)
entry.pack()

convertbutton = tk.Button(root, text="Convert", command=calculate_time)
convertbutton.pack()

resultoutput = tk.Label(root)
resultoutput.pack()

root.mainloop()

