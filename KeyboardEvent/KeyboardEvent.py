from tkinter import *

class KeyboardEvent:
    def __init__(self):
        window = Tk()
        window.title("키보드 이벤트")
        window.geometry("640x480")
        self.keys = set()
        self.canvas=Canvas(window, bg ="white")
        self.canvas.pack(expand=True, fill=BOTH)
        window.bind("<KeyPress>",self.keyPressHandler)
        window.bind("<KeyRelease>",self.keyReleaseHandler)
        self.keystr = "Key: "
        self.key_id = self.canvas.create_text(320,240,font="Times 15 italic bold",text=self.keystr)    
        self.canvas.create_text(320,360,font="Times 15 italic bold",text="Key Event Example")
        self.canvas.create_text(320,400,font="Times 15 italic bold",text="School of computer engineering, Gyeongsang National University")
        while True:
            #
            self.keystr = "Key: " + str(self.keys)
            self.canvas.itemconfigure(self.key_id, text=self.keystr)
            #
            window.after(33)
            window.update()

    def keyReleaseHandler(self, event):
        if event.keycode in self.keys:
            self.keys.remove(event.keycode)

    def keyPressHandler(self,event):
        self.keys.add(event.keycode)


KeyboardEvent()