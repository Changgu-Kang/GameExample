from tkinter import *
import random

class BezierCurvePos:
    def __init__(self):
        window = Tk()
        window.title("Bezier Curve")
        window.geometry("640x480")
        
        self.canvas=Canvas(window, bg ="white")
        self.canvas.pack(expand=True, fill=BOTH)

        self.canvas.create_text(320,380,font="Times 15 italic bold",text="Bezier Curve")
        self.canvas.create_text(320,440,font="Times 15 italic bold",text="School of computer engineering, Gyeongsang National University")

        self.ctlPoints=[]


        #랜덤 컨트롤 포인트 3개 생성
        self.ctlPoints.append([random.randrange(0,640),random.randrange(0,480)])
        self.ctlPoints.append([random.randrange(0,640),random.randrange(0,480)])
        self.ctlPoints.append([random.randrange(0,640),random.randrange(0,480)])
        self.ctlPoints.append([random.randrange(0,640),random.randrange(0,480)])


        for i in range(len(self.ctlPoints)):
            self.canvas.create_oval(self.ctlPoints[i][0] - 5.0, self.ctlPoints[i][1]-5.0,self.ctlPoints[i][0]+5.0,self.ctlPoints[i][1]+5.0,fill='blue')

        pnt_cnt = 50

        pnts = []

        self.tankimg = PhotoImage(file="tank.png").subsample(10)
        self.tank = self.canvas.create_image(self.ctlPoints[0][0],self.ctlPoints[0][1], image = self.tankimg,tags="tank")


        #
        for i in range(pnt_cnt):
            t = 1.0-((i+1) * (1.0/pnt_cnt))
            pnts.append(self.getCurPos(t, len(self.ctlPoints)))
            self.canvas.create_oval(pnts[i][0]-2,pnts[i][1]-2,pnts[i][0]+2,pnts[i][1]+2,fill='red')       


        self.frame_cnt = 0
        while True:
            #
            pos = self.canvas.coords(self.tank)
            x_gap = pnts[self.frame_cnt%pnt_cnt][0] - pos[0]
            y_gap = pnts[self.frame_cnt%pnt_cnt][1] - pos[1]
            self.canvas.move(self.tank,x_gap,y_gap)
            self.frame_cnt = self.frame_cnt + 1
            window.after(33)
            window.update()


    def getCurPos(self, t, cpntN): 
        if cpntN==3 and len(self.ctlPoints)==3:
            return [pow((1.0-t),2) * self.ctlPoints[0][i]+ 2.0*t*(1.0 - t) * self.ctlPoints[1][i] + pow(t,2) * self.ctlPoints[2][i] for i in range(2)]

        elif cpntN==4 and len(self.ctlPoints)==4:
            return [pow((1.0-t),3) * self.ctlPoints[0][i]+ 3.0*t*pow((1.0 - t),2) * self.ctlPoints[1][i] + 3.0*pow(t,2)*(1.0-t) * self.ctlPoints[2][i] + pow(t, 3) * self.ctlPoints[3][i] for i in range(2)]
            


BezierCurvePos()
