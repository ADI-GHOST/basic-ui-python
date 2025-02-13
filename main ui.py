import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import subprocess

def button1_click():
    subprocess.run(["python", r"C:\Users\GhosT\Desktop\expt\e2.py"])
    print("Personal Assistant tasks performed")

def button2_click():
    print("Button 2 Clicked")

def button3_click():
    print("Button 3 Clicked")

def button4_click():
    print("Button 4 Clicked")

class AnimatedGIF(tk.Label):
    def __init__(self, master, path):
        self.im = Image.open(path)
        self.seq = []
        for frame in ImageSequence.Iterator(self.im):
            frame = frame.resize((800, 600), Image.LANCZOS)
            photo = ImageTk.PhotoImage(frame)
            self.seq.append(photo)

        self.current_frame = 0
        super().__init__(master, image=self.seq[0])
        self.animate()

    def animate(self):
        self.config(image=self.seq[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.seq)
        self.after(50, self.animate)

app = ctk.CTk()
app.geometry("500x400")
app.title("python project sem2")


background_frame = tk.Frame(app, bg="black")
background_frame.place(x=0, y=0, relwidth=1, relheight=1)

title_label = ctk.CTkLabel(app, text="hey,how can i help you?", font=("Cascadia Code SemiBold", 24,))
title_label.place(x=0, y=0)

gif_label = AnimatedGIF(background_frame, r"C:\Users\GhosT\Desktop\project sem 2\a94aee835e16cff4f14c83dac8ffbe10.gif")
gif_label.place(x=0, y=0, relwidth=1, relheight=1)

button1 = ctk.CTkButton(app, text="Personal Assistant", command=button1_click, width=130, height=50, fg_color="red", hover_color="dark red")
button1.place(x=10, y=50)

button2 = ctk.CTkButton(app, text="weather report", command=button2_click, width=130, height=50, fg_color="green", hover_color="dark green")
button2.place(x=10, y=150)

button3 = ctk.CTkButton(app, text="code generation", command=button3_click, width=130, height=50, fg_color="blue", hover_color="dark blue")
button3.place(x=10, y=250)

button4 = ctk.CTkButton(app, text="text summarization", command=button4_click, width=95, height=50, fg_color="orange", hover_color="dark orange")
button4.place(x=10, y=350)

app.mainloop()
