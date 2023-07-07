#autoclicker project
import tkinter as tk
import threading
import time
import pyautogui

class autoclickerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("elliott's AutoClicker")
        self.geometry("500x300")
#
        self.clicking_lock = threading.Lock()
        self.clicking = False
        self.click_button_text = tk.StringVar()
        self.click_button_text.set("click here")
#
        self.click_button = tk.Button(self, textvariable=self.click_button_text, command=self.toggle_clicking)
        self.click_button.pack(pady=20)

        self.set_key_button = tk.Button(self, text="trigger", command=self.set_key)
        self.set_key_button.pack(pady=10)
#
        self.key_label_text = tk.StringVar()
        self.key_label_text.set("set a key")
        self.key_label = tk.Label(self, textvariable=self.key_label_text)
        self.key_label.pack(pady=10)

        self.click_count = 0
        self.click_count_label_text = tk.StringVar()
        self.click_count_label_text.set("# clicks")
        self.click_count_label = tk.Label(self, textvariable=self.click_count_label_text)
        self.click_count_label.pack(pady=10)

        self.frequency_label = tk.Label(self, text="click/s")
        self.frequency_label.pack(pady=5)

        self.frequency_entry = tk.Entry(self, state=tk.DISABLED)
        self.frequency_entry.pack(pady=5)
        self.frequency_entry.bind("<Return>", self.lock_frequency_entry)

        self.start_click_key = None
        self.click_frequency = 1.0
        self.frequency_entry_locked = False

    def toggle_clicking(self):
        with self.clicking_lock:
            self.clicking = not self.clicking

        if self.clicking:
            self.click_button_text.set("STOP!")
            self.start_clicking_thread()
        else:
            self.click_button_text.set("click?")

    def start_clicking_thread(self):
        click_thread = threading.Thread(target=self.auto_click)
        click_thread.start()

    def auto_click(self):
        while True:
            with self.clicking_lock:
                if not self.clicking:
                    break

            pyautogui.click()
            with self.clicking_lock:
                self.click_count += 1

            self.click_count_label_text.set(f"Click count: {self.click_count}")
            time.sleep(1.0 / self.click_frequency)

    def set_key(self):
        self.wait_for_key()

    def wait_for_key(self):
        self.set_key_button.config(state=tk.DISABLED)
        self.key_label_text.set("Press a key")
        self.bind("<KeyPress>", self.handle_key_press)

    def handle_key_press(self, event):
        if event.keysym.lower() == "d":
            self.start_click_key = event.keysym.lower()
            self.unbind("<KeyPress>")

            self.key_label_text.set("Key: " + self.start_click_key)
            self.set_key_button.config(state=tk.NORMAL)
            self.frequency_entry.config(state=tk.NORMAL)
            self.frequency_entry.focus_set()
            self.frequency_entry.select_range(0, tk.END)

    def lock_frequency_entry(self, event):
        if not self.frequency_entry_locked:
            self.frequency_entry.config(state=tk.DISABLED)
            self.frequency_entry_locked = True


if __name__ == "__main__":
    auto_clicker_GUI = autoclickerGUI()
    auto_clicker_GUI.mainloop()

