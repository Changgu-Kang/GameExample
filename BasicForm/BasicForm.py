from tkinter import *

class BasicForm:
    def __init__(self):
        window = Tk()
        window.title("기본폼")
        window.geometry("640x480")
        self.keys = set()
        self.canvas=Canvas(window, bg ="white")
        self.canvas.pack(expand=True, fill=BOTH)

        self.canvas.create_text(320,380,font="Times 15 italic bold",text="Basic Form")
        self.canvas.create_text(320,440,font="Times 15 italic bold",text="School of computer engineering, Gyeongsang National University")
        while True:
            #
            window.after(33)
            window.update()


BasicForm()
