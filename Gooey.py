import tkinter as tk

def calculate_time():
    elltime = int(entry.get())
    stime = (elltime - 5 + 24) % 24

    if stime >= 12:
        am_pm = "PM"
    else:
        am_pm = "AM"

    stime %= 12
    if stime == 0:
        stime = 12

    resultoutput.config(text=f"{stime} USA Eastern {am_pm}")

root = tk.Tk()
root.title("Elliot's Timezone Converter")

label = tk.Label(text="GMT to USA eastern:")
label.pack()

entry = tk.Entry(root)
entry.pack()

convertbutton = tk.Button(root, text="Convert", command=calculate_time)
convertbutton.pack()

resultoutput = tk.Label(root, text="")
resultoutput.pack()

root.mainloop()


