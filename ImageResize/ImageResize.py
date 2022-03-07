from tkinter import *
from PIL import Image, ImageTk

class ImageResizeForm:
    def __init__(self):
        window = Tk()
        window.title("기본폼")
        window.geometry("640x480")
        self.keys = set()
        self.canvas=Canvas(window, bg ="white")
        self.canvas.pack(expand=True, fill=BOTH)

        self.canvas.create_text(320,380,font="Times 15 italic bold",text="Basic Form")
        
        
        self.img = Image.open("tank.png")
        self.img_resize = self.img.resize((int(self.img.width), int(self.img.height)))
        
        self.tkimage = ImageTk.PhotoImage(self.img_resize)
        self.obj_image = self.canvas.create_image(250, 250, image=self.tkimage)
          
        self.w = 0.1

        while True:

            self.img_resize = self.img.resize((int(self.img.width*self.w), int(self.img.height*self.w)))
            self.tkimage = ImageTk.PhotoImage(self.img_resize)
            self.canvas.itemconfigure(self.obj_image, image=self.tkimage)#속성 수정
            
            self.w += 0.01

            window.after(33)
            window.update()


ImageResizeForm()


