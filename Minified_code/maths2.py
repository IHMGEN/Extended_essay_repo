_I='divide'
_H='480x624+20+20'
_G='Scientific Calculator'
_F=True
_E='gray5'
_D='gray99'
_C=False
_B='bold'
_A='arial'
from tkinter import*
import math,parser,tkinter.messagebox
root=Tk()
root.title(_G)
root.configure(background='Powder blue')
root.resizable(width=_C,height=_C)
root.geometry(_H)
calc=Frame(root)
calc.grid()
class Calc:
	def __init__(self):self.total=0;self.current='';self.input_value=_F;self.check_sum=_C;self.op='';self.result=_C
	def numberEnter(self,num):
		self.result=_C;firstnum=txtDisplay.get();secondnum=str(num)
		if self.input_value:self.current=secondnum;self.input_value=_C
		else:
			if secondnum=='.':
				if secondnum in firstnum:return
			self.current=firstnum+secondnum
		self.display(self.current)
	def sum_of_total(self):self.result=_F;self.current=float(self.current)
	def valid_function(self):
		if self.op=='add':self.total+=self.current
		if self.op=='sub':self.total-=self.current
		if self.op=='multi':self.total*=self.current
		if self.op==_I:self.total/=self.current
		if self.op=='mod':self.total%=self.current
		if self.op=='inv':self.total=1/self.current
		self.input_value=_F;self.check_sum=_C;self.display(self.total)
	def operation(self,op):
		self.current=float(self.current)
		if self.check_sum:self.valid_function()
		elif not self.result:self.total=self.current;self.input_value=_F
		self.check_sum=_F;self.op=op;self.result=_C
	def Clear_Entry(self):self.result=_C;self.current='0';self.display(0);self.input_value=_F
	def all_Clear_Entry(self):self.Clear_Entry();self.total=0
	def tanh(self):self.reult=_C;self.current=math.tanh(math.radians(float(txtDisplay.get())));self.display(self.current)
	def tan(self):self.reult=_C;self.current=math.tan(math.radians(float(txtDisplay.get())));self.display(self.current)
	def sinh(self):self.reult=_C;self.current=math.sinh(math.radians(float(txtDisplay.get())));self.display(self.current)
	def sin(self):self.reult=_C;self.current=math.sin(math.radians(float(txtDisplay.get())));self.display(self.current)
	def log(self):self.reult=_C;self.current=math.log(float(txtDisplay.get()));self.display(self.current)
	def exp(self):self.reult=_C;self.current=math.exp(float(txtDisplay.get()));self.display(self.current)
	def mathsPM(self):self.reult=_C;self.current=-float(txtDisplay.get());self.display(self.current)
	def squared(self):self.reult=_C;self.current=math.sqrt(float(txtDisplay.get()));self.display(self.current)
	def cos(self):self.reult=_C;self.current=math.cos(math.radians(float(txtDisplay.get())));self.display(self.current)
	def cosh(self):self.reult=_C;self.current=math.cosh(math.radians(float(txtDisplay.get())));self.display(self.current)
	def display(self,value):txtDisplay.delete(0,END);txtDisplay.insert(0,value)
	def pi(self):self.reult=_C;self.current=math.pi;self.display(self.current)
	def tau(self):self.reult=_C;self.current=math.tau;self.display(self.current)
	def e(self):self.reult=_C;self.current=math.e;self.display(self.current)
	def acosh(self):self.result=_C;self.current=math.acosh(float(txtDisplay.get()));self.display(self.current)
	def asinh(self):self.result=_C;self.current=math.asinh(float(txtDisplay.get()));self.display(self.current)
	def expm1(self):self.result=_C;self.current=math.expm1(float(txtDisplay.get()));self.display(self.current)
	def lgamma(self):self.result=_C;self.current=math.lgamma(float(txtDisplay.get()));self.display(self.current)
	def degrees(self):self.result=_C;self.current=math.degrees(float(txtDisplay.get()));self.display(self.current)
	def log2(self):self.result=_C;self.current=math.log2(float(txtDisplay.get()));self.display(self.current)
	def log10(self):self.result=_C;self.current=math.log10(float(txtDisplay.get()));self.display(self.current)
	def log1p(self):self.result=_C;self.current=math.log1p(float(txtDisplay.get()));self.display(self.current)
added_value=Calc()
txtDisplay=Entry(calc,relief=SUNKEN,font=(_A,20,_B),bg='powder blue',bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,'0')
numberpad='789456123'
i=0
btn=[]
for j in range(2,5):
	for k in range(3):btn.append(Button(calc,width=6,height=2,font=(_A,20,_B),bd=4,bg=_D,text=numberpad[i]));btn[i].grid(row=j,column=k,pady=1);btn[i]['command']=lambda x=numberpad[i]:added_value.numberEnter(x);i+=1
btnClear=Button(calc,text=chr(67),width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.Clear_Entry).grid(row=1,column=0,pady=1)
btnAllClear=Button(calc,text=chr(67)+chr(69),width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.all_Clear_Entry).grid(row=1,column=1,pady=1)
btnSq=Button(calc,text='√',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.squared).grid(row=1,column=2,pady=1)
btnAdd=Button(calc,text='+',width=6,height=2,font=(_A,20,_B),bd=4,bg=_D,command=lambda:added_value.operation('add')).grid(row=1,column=3,pady=1)
btnSub=Button(calc,text='-',width=6,height=2,font=(_A,20,_B),bd=4,bg=_D,command=lambda:added_value.operation('sub')).grid(row=2,column=3,pady=1)
btnMult=Button(calc,text='×',width=6,height=2,font=(_A,20,_B),bd=4,bg=_D,command=lambda:added_value.operation('multi')).grid(row=3,column=3,pady=1)
btnDiv=Button(calc,text=chr(247),width=6,height=2,font=(_A,20,_B),bd=4,bg=_D,command=lambda:added_value.operation(_I)).grid(row=4,column=3,pady=1)
btnZero=Button(calc,text='0',width=6,height=2,font=(_A,20,_B),bd=4,bg=_D,command=lambda:added_value.numberEnter(0)).grid(row=5,column=0,pady=1)
btnDot=Button(calc,text='.',width=6,height=2,font=(_A,20,_B),bd=4,bg=_D,command=lambda:added_value.numberEnter('.')).grid(row=5,column=1,pady=1)
btnPM=Button(calc,text=chr(177),width=6,height=2,font=(_A,20,_B),bd=4,bg=_D,command=added_value.mathsPM).grid(row=5,column=2,pady=1)
btnEquals=Button(calc,text='=',width=6,height=2,font=(_A,20,_B),bd=4,bg=_D,command=added_value.sum_of_total).grid(row=5,column=3,pady=1)
btnPi=Button(calc,text='π',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.pi).grid(row=1,column=4,pady=1)
btnCos=Button(calc,text='cos',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.cos).grid(row=1,column=5,pady=1)
btnTan=Button(calc,text='tan',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.tan).grid(row=1,column=6,pady=1)
btnSin=Button(calc,text='sin',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.sin).grid(row=1,column=7,pady=1)
btn2Pi=Button(calc,text='2π',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.tau).grid(row=2,column=4,pady=1)
btnCosh=Button(calc,text='cosh',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.cosh).grid(row=2,column=5,pady=1)
btnTanh=Button(calc,text='tanh',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.tanh).grid(row=2,column=6,pady=1)
btnSinh=Button(calc,text='sinh',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.sinh).grid(row=2,column=7,pady=1)
btnLog=Button(calc,text='log',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.log).grid(row=3,column=4,pady=1)
btninv=Button(calc,text='Inv',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=lambda:added_value.operation('inv')).grid(row=3,column=5,pady=1)
btnMod=Button(calc,text='Mod',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg='lime green',command=lambda:added_value.operation('mod')).grid(row=3,column=6,pady=1)
btnE=Button(calc,text='e',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.e).grid(row=3,column=7,pady=1)
btnLog2=Button(calc,text='log2',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.log2).grid(row=4,column=4,pady=1)
btnDeg=Button(calc,text='deg',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.degrees).grid(row=4,column=5,pady=1)
btnAcosh=Button(calc,text='acosh',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.acosh).grid(row=4,column=6,pady=1)
btnAsinh=Button(calc,text='asinh',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.asinh).grid(row=4,column=7,pady=1)
btnLog10=Button(calc,text='log10',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.log10).grid(row=5,column=4,pady=1)
btnLog1p=Button(calc,text='log1p',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.log1p).grid(row=5,column=5,pady=1)
btnExpm1=Button(calc,text='expm1',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.expm1).grid(row=5,column=6,pady=1)
btnLgamma=Button(calc,text='lgamma',width=6,height=2,font=(_A,20,_B),bd=4,fg=_D,bg=_E,command=added_value.lgamma).grid(row=5,column=7,pady=1)
lblDisplay=Label(calc,text=_G,font=(_A,30,_B),justify=CENTER)
lblDisplay.grid(row=0,column=4,columnspan=4)
lblDisplay=Label(calc,text='Program Warehouse',font=(_A,30,_B),justify=CENTER)
lblDisplay.grid(row=6,column=0,columnspan=4)
def iExit():
	iExit=tkinter.messagebox.askyesno(_G,'Confirm if you want to exit')
	if iExit>0:root.destroy();return
def Scientific():root.resizable(width=_C,height=_C);root.geometry('990x624+20+20')
def Standard():root.resizable(width=_F,height=_C);root.geometry(_H)
menubar=Menu(calc)
filemenu=Menu(menubar,tearoff=0,relief=RAISED)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Standard',command=Standard)
filemenu.add_command(label='Scientific',command=Scientific)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=iExit)
root.config(menu=menubar)
root.mainloop()
