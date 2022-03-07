from tkinter import *

class MouseEvent:
    def __init__(self):
        window = Tk()
        window.title("마우스 이벤트")
        window.geometry("640x480")
        self.keys = set()
        self.canvas=Canvas(window, bg ="white")
        self.canvas.pack(expand=True, fill=BOTH)
        window.bind("<Button-1>",self.MouseClickEvent)
        window.bind('<Double-1>', self.MouseDoubleClickEvent)
        window.bind('<B1-Motion>', self.MouseMotionEvent) 

        self.mousestr = "Mouse: "
        self.mouse_id = self.canvas.create_text(320,240,font="Times 15 italic bold",text=self.mousestr)    
        self.canvas.create_text(320,360,font="Times 15 italic bold",text="Mouse Event Example")
        self.canvas.create_text(320,400,font="Times 15 italic bold",text="School of computer engineering, Gyeongsang National University")
        while True:
            #
            self.canvas.itemconfigure(self.mouse_id, text=self.mousestr)
            #
            window.after(33)
            window.update()

    def MouseClickEvent(self, event):
        self.mousestr = "Mouse: " + str(event.x) + ", " + str(event.y) + "에서 마우스 클릭 이벤트 발생"
        

    def MouseDoubleClickEvent(self, event):
        self.mousestr = "Mouse: " + str(event.x) + ", " + str(event.y) + "에서 마우스 더블 클릭 이벤트 발생"

    def MouseMotionEvent(self, event):
        self.mousestr = "Mouse: " + str(event.x) + ", " + str(event.y) + "에서 마우스 모션 이벤트 발생"


MouseEvent()
