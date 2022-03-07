from tkinter import *
import pygame
from PIL import Image, ImageTk

class StageCanvas:
    def __init__(self,window):
        self.window = window
        self.keys = set()
        self.canvas=Canvas(self.window, bg ="white") # game scene canvas
        self.canvas.create_text(320,300,font="Times 15 italic bold",text="Backspace 키 메뉴로 돌아가기")
        self.canvas.create_text(320,360,font="Times 15 italic bold",text="Stage Scene")
        self.canvas.create_text(320,400,font="Times 15 italic bold",text="School of computer engineering, Gyeongsang National University")


        self.weapon_angle = 0

        #Effect sound
        self.sounds = pygame.mixer
        self.sounds.init()
        self.voice = pygame.mixer.Channel(1)
        #pygame.mixer.get_num_channels() 채널 수 확인
        self.s_effect1 = self.sounds.Sound("sound/tankmove.mp3")


        self.weapon_img = Image.open("image/tank_weapon.png")
        self.weapon_tkimage = ImageTk.PhotoImage(self.weapon_img.rotate(self.weapon_angle))        
        self.tank_weapon = self.canvas.create_image(300,240, image = self.weapon_tkimage,tags="tank_weapon")

        
        self.img_tank_body = PhotoImage(file="image/tank_body.png")
        self.tank_body = self.canvas.create_image(320,240, image = self.img_tank_body,tags="tank_body")
        

    def display(self):
        for key in self.keys:
            if key == 39: # right direction key
                if not self.voice.get_busy():
                    self.voice.play(self.s_effect1)
                self.canvas.move(self.tank_weapon, 5, 0)
                self.canvas.move(self.tank_body, 5, 0)
            elif key == 37: # left direction key                
                if not self.voice.get_busy():
                    self.voice.play(self.s_effect1)
                self.canvas.move(self.tank_weapon, -5, 0)
                self.canvas.move(self.tank_body, -5, 0)
            elif key == 38 and self.weapon_angle < 30:
                self.weapon_angle  = self.weapon_angle + 1
                print(self.weapon_angle)
                self.weapon_tkimage = ImageTk.PhotoImage(self.weapon_img.rotate(self.weapon_angle,expand=True))
                self.canvas.itemconfigure(self.tank_weapon, image=self.weapon_tkimage)#object 속성 수정
            elif key == 40 and self.weapon_angle > 0:
                self.weapon_angle  = self.weapon_angle - 1
                print(self.weapon_angle)
                self.weapon_tkimage = ImageTk.PhotoImage(self.weapon_img.rotate(self.weapon_angle,expand=True))
                self.canvas.itemconfigure(self.tank_weapon, image=self.weapon_tkimage)#object 속성 수정
            



    def pack(self):
        self.canvas.pack(expand=True, fill=BOTH)

    def unpack(self):
        self.canvas.pack_forget()

    def keyReleaseHandler(self, event):
        if event.keycode == 8:
            return 0
        else:
            return -1

    def keyReleaseHandler(self, event):
        if event.keycode in self.keys:
            self.keys.remove(event.keycode)

        if len(self.keys)==0:
            self.voice.stop()

        if event.keycode == 8:
            return 0
        else:
            return -1

    def keyPressHandler(self,event):        
        self.keys.add(event.keycode)

    def destroy(self):
        self.canvas.destroy()


class MenuCanvas:
    def __init__(self,window):
        self.window = window
        self.menu_idx = 0
        self.keys = set()
        self.canvas=Canvas(self.window, bg ="white")# menu canvas

        self.canvas.create_text(320,360,font="Times 15 italic bold",text="Scene Change")
        self.canvas.create_text(320,400,font="Times 15 italic bold",text="School of computer engineering, Gyeongsang National University")
        
        self.canvas.create_text(320,160,font="Times 15 italic bold",text="Start")
        self.canvas.create_text(320,200,font="Times 15 italic bold",text="Option")
        self.canvas.create_text(320,240,font="Times 15 italic bold",text="Exit")


        self.arrowimg = PhotoImage(file="image/arrow.png").subsample(20)
        self.arrow = self.canvas.create_image(250,160, image = self.arrowimg,tags="arrow")


    def display(self):
        pass
        

    def pack(self):
        self.canvas.pack(expand=True, fill=BOTH)

    def unpack(self):
        self.canvas.pack_forget()


    def keyPressHandler(self,event):        
        pass

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




class WarTank:
    def __init__(self):
        self.window = Tk()
        self.window.title("WarTank")
        self.window.geometry("640x480")

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.scene_idx = 0
        
        self.stage = StageCanvas(self.window)
        self.menu = MenuCanvas(self.window)
        self.menu.pack()


        self.canvas_list = []
        self.canvas_list.append(self.menu)
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

        result = self.canvas_list[self.scene_idx].keyReleaseHandler(event)        

        if self.scene_idx == 0 and result==0:
            self.scene_idx = 1
            self.menu.unpack()
            self.stage.pack()

        elif self.scene_idx==1 and result==0:
            self.scene_idx = 0
            self.menu.pack()#메뉴 canvas 나타남
            self.stage.unpack()# Main 장면 canvas 사라짐
                
    def keyPressHandler(self,event):
        self.canvas_list[self.scene_idx].keyPressHandler(event)
        


WarTank()
