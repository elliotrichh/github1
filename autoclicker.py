#autoclicker project
import tkinter as tk
import threading
import time
import pyautogui

class AutoClickerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("elliot's autoclicker")
        self.geometry("500x150")

        self.clicking = False

        self.click_button = tk.Button(self, text="click?", command=self.toggle_clicking)
        self.click_button.pack(pady=20)

    def toggle_clicking(self):
        self.clicking = not self.clicking

        if self.clicking:
            self.click_button.config(text="STOP!")
            self.start_clicking_thread()
        else:
            self.click_button.config(text="click?")

    def start_clicking_thread(self):
        click_thread = threading.Thread(target=self.auto_click)
        click_thread.start()

    def auto_click(self):
        while self.clicking:
            pyautogui.click()
            time.sleep(0.1)  #adjust the click delay


if __name__ == "__main__":
    autoclicker_gui = AutoClickerGUI()
    autoclicker_gui.mainloop()
