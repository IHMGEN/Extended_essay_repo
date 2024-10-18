_G='complete'
_F=True
_E='Down'
_D='Up'
_C='Left'
_B=False
_A='Right'
from tkinter import*
import random,time,numpy as np
from PIL import ImageTk,Image
size_of_board=600
rows=10
cols=10
DELAY=100
snake_initial_length=3
symbol_size=(size_of_board/3-size_of_board/8)/2
symbol_thickness=2
RED_COLOR='#EE4035'
BLUE_COLOR='#0492CF'
Green_color='#7BC043'
BLUE_COLOR_LIGHT='#67B0CF'
RED_COLOR_LIGHT='#EE7E77'
class SnakeAndApple:
	def __init__(self):self.window=Tk();self.window.title('Snake-and-Apple');self.canvas=Canvas(self.window,width=size_of_board,height=size_of_board);self.canvas.pack();self.window.bind('<Key>',self.key_input);self.window.bind('<Button-1>',self.mouse_input);self.play_again();self.begin=_B
	def initialize_board(self):
		self.board=[];self.apple_obj=[];self.old_apple_cell=[]
		for i in range(rows):
			for j in range(cols):self.board.append((i,j))
		for i in range(rows):self.canvas.create_line(i*size_of_board/rows,0,i*size_of_board/rows,size_of_board)
		for i in range(cols):self.canvas.create_line(0,i*size_of_board/cols,size_of_board,i*size_of_board/cols)
	def initialize_snake(self):
		self.snake=[];self.crashed=_B;self.snake_heading=_A;self.last_key=self.snake_heading;self.forbidden_actions={};self.forbidden_actions[_A]=_C;self.forbidden_actions[_C]=_A;self.forbidden_actions[_D]=_E;self.forbidden_actions[_E]=_D;self.snake_objects=[]
		for i in range(snake_initial_length):self.snake.append((i,0))
	def play_again(self):self.canvas.delete('all');self.initialize_board();self.initialize_snake();self.place_apple();self.display_snake(mode=_G);self.begin_time=time.time()
	def mainloop(self):
		while _F:
			self.window.update()
			if self.begin:
				if not self.crashed:self.window.after(DELAY,self.update_snake(self.last_key))
				else:self.begin=_B;self.display_gameover()
	def display_gameover(self):A='cmr 20 bold';score=len(self.snake);self.canvas.delete('all');score_text='Scores \n';self.canvas.create_text(size_of_board/2,3*size_of_board/8,font='cmr 40 bold',fill=Green_color,text=score_text);score_text=str(score);self.canvas.create_text(size_of_board/2,1*size_of_board/2,font='cmr 50 bold',fill=BLUE_COLOR,text=score_text);time_spent=str(np.round(time.time()-self.begin_time,1))+'sec';self.canvas.create_text(size_of_board/2,3*size_of_board/4,font=A,fill=BLUE_COLOR,text=time_spent);score_text='Click to play again \n';self.canvas.create_text(size_of_board/2,15*size_of_board/16,font=A,fill='gray',text=score_text)
	def place_apple(self):unoccupied_cels=set(self.board)-set(self.snake);self.apple_cell=random.choice(list(unoccupied_cels));row_h=int(size_of_board/rows);col_w=int(size_of_board/cols);x1=self.apple_cell[0]*row_h;y1=self.apple_cell[1]*col_w;x2=x1+row_h;y2=y1+col_w;self.apple_obj=self.canvas.create_rectangle(x1,y1,x2,y2,fill=RED_COLOR_LIGHT,outline=BLUE_COLOR)
	def display_snake(self,mode=''):
		if self.snake_objects!=[]:self.canvas.delete(self.snake_objects.pop(0))
		if mode==_G:
			for(i,cell)in enumerate(self.snake):row_h=int(size_of_board/rows);col_w=int(size_of_board/cols);x1=cell[0]*row_h;y1=cell[1]*col_w;x2=x1+row_h;y2=y1+col_w;self.snake_objects.append(self.canvas.create_rectangle(x1,y1,x2,y2,fill=BLUE_COLOR,outline=BLUE_COLOR))
		else:
			cell=self.snake[-1];row_h=int(size_of_board/rows);col_w=int(size_of_board/cols);x1=cell[0]*row_h;y1=cell[1]*col_w;x2=x1+row_h;y2=y1+col_w;self.snake_objects.append(self.canvas.create_rectangle(x1,y1,x2,y2,fill=BLUE_COLOR,outline=RED_COLOR))
			if self.snake[0]==self.old_apple_cell:self.snake.insert(0,self.old_apple_cell);self.old_apple_cell=[];tail=self.snake[0];row_h=int(size_of_board/rows);col_w=int(size_of_board/cols);x1=tail[0]*row_h;y1=tail[1]*col_w;x2=x1+row_h;y2=y1+col_w;self.snake_objects.insert(0,self.canvas.create_rectangle(x1,y1,x2,y2,fill=BLUE_COLOR,outline=RED_COLOR))
			self.window.update()
	def update_snake(self,key):
		tail=self.snake[0];head=self.snake[-1]
		if tail!=self.old_apple_cell:self.snake.pop(0)
		if key==_C:self.snake.append((head[0]-1,head[1]))
		elif key==_A:self.snake.append((head[0]+1,head[1]))
		elif key==_D:self.snake.append((head[0],head[1]-1))
		elif key==_E:self.snake.append((head[0],head[1]+1))
		head=self.snake[-1]
		if head[0]>cols-1 or head[0]<0 or head[1]>rows-1 or head[1]<0 or len(set(self.snake))!=len(self.snake):self.crashed=_F
		elif self.apple_cell==head:self.old_apple_cell=self.apple_cell;self.canvas.delete(self.apple_obj);self.place_apple();self.display_snake()
		else:self.snake_heading=key;self.display_snake()
	def check_if_key_valid(self,key):
		valid_keys=[_D,_E,_C,_A]
		if key in valid_keys and self.forbidden_actions[self.snake_heading]!=key:return _F
		else:return _B
	def mouse_input(self,event):self.play_again()
	def key_input(self,event):
		if not self.crashed:
			key_pressed=event.keysym
			if self.check_if_key_valid(key_pressed):self.begin=_F;self.last_key=key_pressed
game_instance=SnakeAndApple()
game_instance.mainloop()
