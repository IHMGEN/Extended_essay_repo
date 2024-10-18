#!/usr/bin/env python3

import logging as A,sys,random as B
from PySide2.QtWidgets import QApplication as F,QDialog as G,QLabel as H,QVBoxLayout as I
class C(G):
	def __init__(A,ad_slogan,parent=None):super(C,A).__init__(parent);A.setWindowTitle('Advertisement!');A.label=H(ad_slogan);B=I();B.addWidget(A.label);A.setLayout(B)
	def closeEvent(A,event):event.ignore()
class D(F):
	def __init__(A,args):super(D,A).__init__(args)
	@property
	def advert_slogans(self):return'Buy the milk in the milk shops!','Buy the clothes in the wool shops!','Buy the food in the food shops!'
	def create_ad_window(B,ad_slogan):A=C(ad_slogan=ad_slogan);A.show();return A
	def show_ads(A):
		C=[]
		for E in A.advert_slogans:D=A.create_ad_window(E);F,G=B.randint(1,800),B.randint(1,600);D.move(F,G);C.append(D)
		return C
if __name__=='__main__':A.basicConfig(level=A.DEBUG);E=D(sys.argv);J=E.show_ads();sys.exit(E.exec_())
