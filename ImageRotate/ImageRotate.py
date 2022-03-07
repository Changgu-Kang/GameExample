from tkinter import *
from PIL import Image, ImageTk

class BasicForm:
    def __init__(self):
        window = Tk()
        window.title("기본폼")
        window.geometry("640x480")
        self.keys = set()
        self.canvas=Canvas(window, bg ="white")
        self.canvas.pack(expand=True, fill=BOTH)

        self.canvas.create_text(320,380,font="Times 15 italic bold",text="Basic Form")
        self.img = Image.open("tank.png")
        self.img = self.img.resize((self.img.width//6,self.img.height//6),Image.NEAREST)

        self.angle = 0
        self.tkimage = ImageTk.PhotoImage(self.img.rotate(self.angle))
        self.obj_image = self.canvas.create_image(320, 240, image=self.tkimage)            

        while True:
            #
            self.tkimage = ImageTk.PhotoImage(self.img.rotate(self.angle,expand=True))            
            self.canvas.itemconfigure(self.obj_image, image=self.tkimage)#object 속성 수정
            
            self.angle += 10
            self.angle %= 360

            window.after(33)
            window.update()


BasicForm()

