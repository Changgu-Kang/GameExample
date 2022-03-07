from tkinter import * # tkinter에서 모든 정의를 임포트한다.


class LoadGIFImage:
	def __init__(self):
		window = Tk() # 윈도우 생성
		window.title("GIF Image Example") # 제목을 설정
		window.geometry("640x480") # 윈도우 크기 설정
		window.resizable(0,0)        
		self.canvas = Canvas(window, bg = "white")
		self.canvas.pack(expand=True,fill=BOTH)	
		
		self.my_image_number = 0 
		#마지막 range(60) 에서 60 은 gif 이미지 수를 나타냄
		#gif 파일의 이미지를 한장씩 읽고 리스트에 저장함
		self.myimages = [PhotoImage(file='dragon-gif.gif',format = 'gif -index %i' %(i)) for i in range(60)]
		
		
		#아래 코드에서 subsample(2) 는 이미지 크기를 작게함. 인수 값에 따라 작아짐
		#self.myimages = [PhotoImage(file='dragon-gif.gif',format = 'gif -index %i' %(i)).subsample(1) for i in range(60)]

		#이미지를 canvas에 그리고 id 값을 생성후 self.dragon 변수에 저장
		self.dragon = self.canvas.create_image(300,240, image = self.myimages[0],tags="dragon")

		self.canvas.create_text(320,360,font="Times 15 italic bold",text="Load GIF Image")
		self.canvas.create_text(320,400,font="Times 15 italic bold",text="School of computer engineering, Gyeongsang National University")

		while True:

			#canvas에서 self.dragon 이미지를 읽어오고 gif의 다음 이미지로 교체함
			self.canvas.itemconfig(self.dragon, image = self.myimages[self.my_image_number%len(self.myimages)])    

			self.my_image_number += 1
			window.after(33)
			window.update()

		#window.mainloop() # 이벤트 루프를 생성한다.


LoadGIFImage() # GUI 생성한다.

