from tkinter import *
import pygame


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
        
        self.tankimg = PhotoImage(file="image/tank.png").subsample(8)
        self.tank = self.canvas.create_image(320,240, image = self.tankimg,tags="tank")

        #Effect sound
        self.sounds = pygame.mixer
        self.sounds.init()
        self.s_effect1 = self.sounds.Sound("sound/tankmove.mp3")
        

        self.canvas.create_text(320,350,font="Times 15 italic bold",text="← 또는 → 키를 입력하시오")
        self.canvas.create_text(320,420,font="Times 15 italic bold",text="Object Control By KeyEvent")
        self.canvas.create_text(320,450,font="Times 15 italic bold",text="School of computer engineering, Gyeongsang National Universityty")
        

        while True:
            #
            self.display()
            window.after(33)
            window.update()


    def display(self):
        for key in self.keys:
            if key == 39: # right direction key                
                #self.s_effect1.play()
                self.canvas.move(self.tank, 5, 0)
            if key == 37: # left direction key                
                #self.s_effect1.play()
                self.canvas.move(self.tank, -5, 0)


    def keyReleaseHandler(self, event):
        if event.keycode in self.keys:
            #self.s_effect1.stop()
            self.keys.remove(event.keycode)

    def keyPressHandler(self,event):        
        self.keys.add(event.keycode)
        
KeyboardEvent()
