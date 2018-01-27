from tkinter import *
import random
import time

tk=Tk()
tk.title("Gumballs and Bricks")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=700,height=550, bd=0,highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__ (self, canvas, score, paddle, block,color):
        self.canvas=canvas
        self.score=score
        self.paddle=paddle
        self.block=block
        self.oval=canvas.create_oval(32,32,50,50,fill=color)
        self.canvas.move(self.oval,320,80)
        starting_speed = [-3,-2,2,3]
        random.shuffle(starting_speed)
        self.x = starting_speed[0]
        self.y = starting_speed[1]
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_floor = False
    def hit_paddle(self,oval_position):
        paddle_position=self.canvas.coords(self.paddle.paddle_shape)
        if oval_position[2]>= paddle_position[0] and oval_position[0] <=paddle_position[2]:
            if oval_position[3] >=paddle_position[1] and oval_position[1]<=paddle_position[3]:
                self.x += self.paddle.x
                self.score.score_points()
                return True
        return False
    def hit_block(self,oval_position):
        square_position=self.canvas.coords(self.block.square)
        if oval_position[3]>=square_position[1] and oval_position[1]<=square_position[3]:
            if oval_position[0]<square_position[0] and oval_position[2]>=square_position[0]:
                return True
        return False
    def hit_block_right_side(self,oval_position):
        square_position=self.canvas.coords(self.block.square)
        if oval_position[3]>=square_position[1] and oval_position[1]<=square_position[3]:
            if oval_position[0]<= square_position[2] and oval_position[2]>square_position[2]:
                return True
        return False
    def hit_block_top_side(self, oval_position):
        square_position=self.canvas.coords(self.block.square)
        if oval_position[0]<=square_position[2] and oval_position[2]>=square_position[0]:
            if oval_position[3]>=square_position[1] and oval_position[1]<square_position[1]:
                return True
        return False
    def hit_block_bottom_side(self,oval_position):
        square_position=self.canvas.coords(self.block.square)
        if oval_position[0]<=square_position[2] and oval_position[2]>=square_position[0]:
            if oval_position[1]<=square_position[3] and oval_position[3]>square_position[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.oval,self.x,self.y)
        oval_position=self.canvas.coords(self.oval)
        if oval_position[1] <=0:
            self.y=3
        if oval_position[3]>= self.canvas_height:
            self.y=-3
        if oval_position[0] <= 0:
            self.x=3
        if oval_position[2] >= self.canvas_width:
            self.x=-3
        if self.hit_paddle(oval_position) == True:
            self.y=-3
        if oval_position[3] >= self.canvas_height:
            self.hit_floor = True
        if self.hit_block(oval_position) == True:
            self.x=-3
        if self.hit_block_right_side(oval_position) == True:
            self.x=3
        if self.hit_block_top_side(oval_position)==True:
            self.y=-3
        if self.hit_block_bottom_side(oval_position)==True:
            self.y=3
class Square:
    def __init__ (self,canvas,paddle, color):
        self.canvas=canvas
        self.paddle=paddle
        self.square=canvas.create_rectangle(50,50,80,80, fill=color)
        self.canvas.move(self.square, 320,120)
        starting_speed=[-2,-1,1,2]
        random.shuffle(starting_speed)
        self.x= starting_speed[2]
        self.y= starting_speed[0]
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_floor=False
    def hit_paddle (self,square_position):
        paddle_position=self.canvas.coords(self.paddle.paddle_shape)
        if square_position[2]>=paddle_position[0] and square_position[0]<= paddle_position[2]:
            if square_position[3]>= paddle_position[1] and square_position[1]<=paddle_position[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.square,self.x,self.y)
        square_position=self.canvas.coords(self.square)
        if square_position[1] <= 0:
            self.y=2
        if square_position[3] >= self.canvas_height:
            self.y=-2
        if square_position[0] <= 0 :
            self.x=2
        if square_position[2] >= self.canvas_width:
            self.x=-2
        if self.hit_paddle(square_position)==True:
            self.y=-2
        if square_position[3]>=self.canvas.winfo_height():
            self.hit_floor=True
class Paddle:
    def __init__ (self,canvas,color):
        self.canvas=canvas
        self.paddle_shape=canvas.create_rectangle(00,00,120,10,fill=color)
        self.canvas.move(self.paddle_shape, .5*self.canvas.winfo_width()-60,.85*self.canvas.winfo_height()-5)
        self.canvas_width=self.canvas.winfo_width()
        self.x=0
        self.y=0
        self.canvas.bind_all('<KeyPress-Left>', self.move_paddle_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_paddle_right)
        self.game_on= False
        self.canvas.bind_all('<KeyPress-Return>', self.begin_game)
        self.canvas.bind_all('<Button-1>', self.change_color)
    def draw(self):
        self.canvas.move(self.paddle_shape,self.x,0)
        paddle_shape_position=self.canvas.coords(self.paddle_shape)
        if paddle_shape_position[0]<=0:
            self.x=2
        if paddle_shape_position[2]>= self.canvas_width:
            self.x=-2
    def move_paddle_left(self,event):
        self.x= -5
    def move_paddle_right(self,event):
        self.x= 5
    def begin_game(self,event):
        self.game_on= True
        canvas.itemconfig(start_up_message, state='hidden')
        tk.update()
        time.sleep(0.3)
        game_on_message=canvas.create_text(350,250, text="Game on! :D", font=('helvetica',40),fill='red')
        tk.update()
        time.sleep(1)
        canvas.itemconfig(game_on_message, state='hidden')
    def change_color(self,event):
        colors = ['blue','yellow','grey','brown','pink','red','green',\
                      'teal','magenta','violet','purple','orange','gold','black']
        fill_color=random.choice(colors)
        canvas.itemconfig(self.paddle_shape,fill=fill_color)

class Score:
    def __init__ (self,canvas,color):
        self.score = 0
        self.canvas = canvas
        self.points=canvas.create_text(60,40, text=self.score, font=('arial', 10), fill=color)
    def score_points(self):
        self.score += 50
        self.canvas.itemconfig(self.points, text=self.score)
       
score= Score(canvas, 'green')
paddle= Paddle(canvas,'blue')
block = Square(canvas,paddle,'purple')
ball = Ball(canvas, score, paddle, block, 'orange')


start_up_message=canvas.create_text(350,250, text="Hit 'Enter' to Begin...", font=('helvetica', 30), fill='black')
player_score=canvas.create_text(60,20, text="PLAYER SCORE", font=('arial', 10), fill='green')


while True:
    if ball.hit_floor == False and block.hit_floor == False and paddle.game_on == True:
        paddle.draw()
        ball.draw()
        block.draw()
        if score.score == 1000:
            canvas.create_text(350,250, text='You win!', font=('helvetica', 30), fill='blue')
            tk.update()
            time.sleep(1)
            canvas.create_text(350,300, text='Your grade = :)', font=('helvetica', 18), fill='blue')
            canvas.create_text(350,350, text='CURRENT HIGH SCORE:   1000', font=('arial', 12), fill='green')
            tk.update()
            time.sleep(1.4)
            break
            while True:
                time.sleep(1)
    tk.update_idletasks()
    tk.update()
    time.sleep(.01)
    if ball.hit_paddle ==True:
        Score.score_points()
    if ball.hit_floor == True or block.hit_floor == True:
        tk.update()
        time.sleep(.5)
        game_over_message=canvas.create_text(350,250, text="Game Over", font=('helvetica',30), fill='red')
        tk.update()
        time.sleep(1)
        while True:
            grade_message=canvas.create_text(350, 300, text="Your grade = :[", font=('helvetica',18), state='normal',fill='blue')
            insert_coin_message=canvas.create_text(350,350, text="INSERT MONEY INTO MIKE'S WALLET TO CONTINUE", font=('arial',12), fill='green', state='normal')
            tk.update()
            time.sleep(1.4)
            canvas.itemconfig(grade_message, state='hidden')
            canvas.itemconfig(insert_coin_message, state='hidden')
            tk.update()
            time.sleep(.5)
