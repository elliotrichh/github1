import tkinter as tk

def update_text():
    text = text_input.get("1.0", "end-1c")  # Get text from the text widget
    text_output.config(text=text)

root = tk.Tk()
root.title("Input GUI")

text_input = tk.Text(root, bg="white")
text_input.pack()

text_output = tk.Label(root, text="", bg="white")
text_output.pack()


root.mainloop()
