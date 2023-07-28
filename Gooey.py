import tkinter as tk

# function to calculate the converted time and update the GUI
def calculate_time():
    # get the user's input time from the entry widget and convert it to an integer
    elltime = int(entry.get())

    # calculate the time in USA Eastern timezone by subtracting 5 hours (GMT to EST) and adding 12 to handle negative values
    stime = (elltime - 5 + 12) % 24

    # check if the calculated time is in the afternoon (AM) or evening (PM)
    if stime > 12:
        # if the time is after 12 PM, set the resultoutput label to "AM"
        resultoutput.config(text="AM")
    else:
        # if the time is 12 PM or earlier, set the resultoutput label to "PM"
        resultoutput.config(text="PM")


    # if the result is 0, set it to 12 (midnight)
    stime %= 12
    if stime == 0:
        stime = 12

    # update the resultoutput label to display the final converted time along with the AM/PM designation in USA Eastern timezone
    resultoutput.config(text=f"{stime} USA eastern")

# create the main application window
root = tk.Tk()
root.title("Elliot's Timezone Converter")

# create a label to prompt the user for input
labels = tk.Label(text="Elliot's time")
labels.pack()

# create an entry widget for the user to enter the time in GMT
entry = tk.Entry(root)
entry.pack()

# create a button to initiate the time conversion and display the result
convertbutton = tk.Button(root, text="Convert", command=calculate_time)
convertbutton.pack()

# create a label to display the converted time and AM/PM designation
resultoutput = tk.Label(root)
resultoutput.pack()

# start the main event loop to run the application
root.mainloop()

