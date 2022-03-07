from tkinter import *

class Menu:
    def __init__(self):
        window = Tk()
        window.title("키보드 이벤트")
        window.geometry("640x480")
        self.menu_idx = 0
        self.canvas=Canvas(window, bg ="white")
        self.canvas.pack(expand=True, fill=BOTH)
        window.bind("<KeyPress>",self.keyPressHandler)
        window.bind("<KeyRelease>",self.keyReleaseHandler)
        self.canvas.create_text(320,360,font="Times 15 italic bold",text="Menu Example")
        self.canvas.create_text(320,400,font="Times 15 italic bold",text="School of computer engineering, Gyeongsang National University")
        
        self.canvas.create_text(320,160,font="Times 15 italic bold",text="Menu 1")
        self.canvas.create_text(320,200,font="Times 15 italic bold",text="Menu 2")
        self.canvas.create_text(320,240,font="Times 15 italic bold",text="Menu 3")

        self.menustr = "Menu selection: "
        self.menu_id = self.canvas.create_text(320,320,font="Times 15 italic bold",text=self.menustr)    


        self.arrowimg = PhotoImage(file="arrow.png").subsample(20)
        self.arrow = self.canvas.create_image(250,160, image = self.arrowimg,tags="arrow")
        while True:
            #
            #
            window.after(33)
            window.update()

    def keyReleaseHandler(self, event):
        if event.keycode == 38 and self.menu_idx > 0: # up direction key
            self.menu_idx = self.menu_idx - 1
            self.canvas.move(self.arrow, 0, -40)
        if event.keycode == 40 and self.menu_idx < 2: # down direction key
            self.menu_idx = self.menu_idx + 1
            self.canvas.move(self.arrow, 0, 40)
        if event.keycode == 32:
            self.menustr = "Menu selection: " + str(self.menu_idx)
            self.canvas.itemconfigure(self.menu_id, text=self.menustr)#object 속성 수정

    def keyPressHandler(self,event):
        print(event.keycode)


Menu()