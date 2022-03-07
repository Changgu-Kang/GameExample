from tkinter import * # tkinter에서 모든 정의를 임포트한다.
import pygame

class GameSound:
	def __init__(self):
		window = Tk() # 윈도우 생성
		window.title("게임사운드") # 제목을 설정
		window.geometry("640x480") # 윈도우 크기 설정
		window.resizable(0,0)        
		
		self.keys=set()
		self.canvas = Canvas(window, bg = "white")
		self.canvas.pack(expand=True,fill=BOTH)
		window.bind("<KeyPress>",self.keyPressHandler)
		window.bind("<KeyRelease>",self.keyReleaseHandler)

		#pygame 에서 music vs sound
		# music: 배경음악 재생을 위해 사용
		# sound: 효과음을 위해 사용

        #BG sound.
		pygame.init()
		pygame.mixer.music.load("bgm.wav") #Loading File Into Mixer
		pygame.mixer.music.play(-1) #Playing It In The Whole Device
		self.canvas.create_text(320,360,font="Times 15 italic bold",text="Sound Example")
		self.canvas.create_text(320,400,font="Times 15 italic bold",text="School of computer engineering, Gyeongsang National University")

		#Effect sound
		self.sounds = pygame.mixer
		self.sounds.init()
		self.s_effect1 = self.sounds.Sound("gunsound.mp3")
				
		while True:
			#
			window.after(33)
			window.update()
					



	def keyReleaseHandler(self, event):
		if event.keycode in self.keys:
		    self.keys.remove(event.keycode)

	def keyPressHandler(self, event):		
		self.s_effect1.play()
		self.keys.add(event.keycode)


GameSound() # GUI 생성한다.

