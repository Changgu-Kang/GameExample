from tkinter import *


class StageCanvas:
    def __init__(self,window):
        self.window = window
        self.canvas=Canvas(self.window, bg ="white") # game scene canvas
        self.canvas.create_text(320,300,font="Times 15 italic bold",text="Backspace 키 메뉴로 돌아가기")
        self.canvas.create_text(320,360,font="Times 15 italic bold",text="Stage Scene")
        self.canvas.create_text(320,400,font="Times 15 italic bold",text="School of computer engineering, Gyeongsang National University")


    def display(self):
        pass

    def pack(self):
        self.canvas.pack(expand=True, fill=BOTH)

    def unpack(self):
        self.canvas.pack_forget()

    def keyReleaseHandler(self, event):
        if event.keycode == 8:
            return 0
        else:
            return -1

    def destroy(self):
        self.canvas.destroy()


class MenuCanvas:
    def __init__(self,window):
        self.window = window
        self.menu_idx = 0

        self.canvas=Canvas(self.window, bg ="white")# menu canvas

        self.canvas.create_text(320,360,font="Times 15 italic bold",text="Scene Change")
        self.canvas.create_text(320,400,font="Times 15 italic bold",text="School of computer engineering, Gyeongsang National University")
        
        self.canvas.create_text(320,160,font="Times 15 italic bold",text="Start")
        self.canvas.create_text(320,200,font="Times 15 italic bold",text="Option")
        self.canvas.create_text(320,240,font="Times 15 italic bold",text="Exit")


        self.arrowimg = PhotoImage(file="arrow.png").subsample(20)
        self.arrow = self.canvas.create_image(250,160, image = self.arrowimg,tags="arrow")


    def display(self):
        pass
        

    def pack(self):
        self.canvas.pack(expand=True, fill=BOTH)

    def unpack(self):
        self.canvas.pack_forget()


    def keyReleaseHandler(self, event):
        if event.keycode == 38 and self.menu_idx > 0: # up direction key
            self.menu_idx = self.menu_idx - 1
            self.canvas.move(self.arrow, 0, -40)
            return -1
        elif event.keycode == 40 and self.menu_idx < 2: # down direction key
            self.menu_idx = self.menu_idx + 1
            self.canvas.move(self.arrow, 0, 40)
            return -1
        elif event.keycode == 32:
            return self.menu_idx


    def destroy(self):
        self.canvas.destroy()




class SceneChange:
    def __init__(self):
        self.window = Tk()
        self.window.title("장면전환")
        self.window.geometry("640x480")

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.scene_idx = 0
        
        self.stage = StageCanvas(self.window)
        self.menu = MenuCanvas(self.window)
        self.menu.pack()


        self.canvas_list = []
        self.canvas_list.append(self.stage)
        self.canvas_list.append(self.stage)

        self.window.bind("<KeyPress>",self.keyPressHandler)
        self.window.bind("<KeyRelease>",self.keyReleaseHandler)

        while True:
            #
            #
            for canvas in self.canvas_list:
                canvas.display()


            self.window.after(33)
            self.window.update()

    def on_closing(self):
        for canvas in self.canvas_list:
            canvas.destroy()

        self.window.destroy()

    def keyReleaseHandler(self, event):

        result = -1

        if self.scene_idx == 0:
            result = self.menu.keyReleaseHandler(event)

        elif self.scene_idx == 1:
            result = self.stage.keyReleaseHandler(event)

        if self.scene_idx == 0 and result==0:
            self.scene_idx = 1
            self.menu.unpack()
            self.stage.pack()

        elif self.scene_idx==1 and result==0:
            self.scene_idx = 0
            self.menu.pack()#메뉴 canvas 나타남
            self.stage.unpack()# Main 장면 canvas 사라짐
                
    def keyPressHandler(self,event):
        print(event.keycode)


SceneChange()