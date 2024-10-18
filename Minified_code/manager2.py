y='Are you sure you want to send this folder to recycle bin? (YES/NO)'
x='deleteManager'
w='\nChoose a file to delete: '
v='\nChoose a folder to open: '
u=' to a desired location.'
t='Enter a new name: '
q='\nChoose a file to move: '
p='2'
o='1'
k='y'
j='yes'
i='Yes or No: '
h='pasteManager'
g="You can't choose a file.\nPlease choose a folder."
e='No file/folder exist of this name.'
d='backManager'
c='exitManager'
b='Type "backManager" to go up one directory.'
a='\n\nType "exitManager" to exit from file manager.'
Z='Drives: '
V='Error\nEnter a correct drive name.\n'
U='..'
S='\n'
R='\nEnter your Choice: '
Q='. '
P=str
O=len
M=range
I='\\'
G=True
F=input
A=print
import sys as Y,os as B,shutil as W,send2trash as r
A('Welcome to the python-file-manager\n')
D=[chr(A)+':'for A in M(65,90)if B.path.exists(chr(A)+':')]
def N():
	C=B.listdir(B.getcwd())
	for D in C:A(D)
while G:
	A('1.Open files/folders \n2.Rename \n3.Move and Paste \n4.Copy and Paste \n5.Delete\n');f=F('Choose one of the following: ')
	if f==o:
		A('\nQuick Acess:\n1. Documents\n2. Videos\n3. Pictures\n4. Downloads\n');A(Z)
		for E in M(O(D)):A(P(5+E)+Q+D[E])
		while G:
			H=F(R)
			if H==o:K='C:\\Users\\$USERNAME\\Documents';B.chdir(B.path.expandvars(K));break
			elif H==p:K='C:\\Users\\$USERNAME\\Videos';B.chdir(B.path.expandvars(K));break
			elif H=='3':K='C:\\Users\\$USERNAME\\Pictures';B.chdir(B.path.expandvars(K));break
			elif H=='4':K='C:\\Users\\$USERNAME\\Downloads';B.chdir(B.path.expandvars(K));break
			elif H in D:B.chdir(H+I);break
			else:A('Error\nEnter a correct input / drive name.\n')
		while G:
			N();A(a);A(b);C=F('\nChoose a file/folder: ');A(S)
			if C in B.listdir(B.getcwd()):
				if B.path.isfile(C):B.system('"'+C+'"')
				else:B.chdir(C)
			elif C==c:Y.exit(0)
			elif C==d:B.chdir(U)
			else:A(e)
	if f==p:
		A('You chose to rename');A(Z)
		for E in M(O(D)):A(P(1+E)+Q+D[E])
		while G:
			H=F(R)
			if H in D:B.chdir(H+I);break
			else:A(V)
		while G:
			N();A(a);A(b);A('Type "renameManager" to rename this directory');C=F('\nChoose a file to rename: ');A(S)
			if C in B.listdir(B.getcwd()):
				if B.path.isfile(C):l=F(t);m=C;n=B.getcwd()+I+l;W.move(m,n)
				else:B.chdir(C)
			elif C==c:Y.exit(0)
			elif C==d:B.chdir(U)
			elif C=='renameManager':l=F(t);m=B.getcwd();B.chdir(U);n=B.getcwd()+I+l;W.move(m,n)
			else:A(e)
	if f=='3':
		A('You chose to move');A(Z)
		for E in M(O(D)):A(P(1+E)+Q+D[E])
		while G:
			H=F(R)
			if H in D:B.chdir(H+I);break
			else:A(V)
		while G:
			N();A(a);A(b);A('Type "cutManager" to move this directory');C=F(q);A(S)
			if C in B.listdir(B.getcwd()):
				if B.path.isfile(C):
					T=B.getcwd()+I+C;A('\nMove '+C+u)
					while G:
						for E in M(O(D)):A(P(1+E)+Q+D[E])
						L=F(R)
						if L in D:B.chdir(L+I);break
						else:A(V)
					while G:
						N();A('Type "pasteManager" to paste this file in current directory');J=F(q);A(S)
						if J in B.listdir(B.getcwd()):
							if B.path.isfile(C):A(g)
							else:B.chdir(J)
						elif J==h:W.move(T,B.getcwd());break
				else:B.chdir(C)
			elif C==c:Y.exit(0)
			elif C==d:B.chdir(U)
			elif C=='cutManager':
				T=B.getcwd();A('Moving the current directory')
				while G:
					for E in M(O(D)):A(P(1+E)+Q+D[E])
					L=F(R)
					if L in D:B.chdir(L+I);break
					else:A(V)
				while G:
					N();A('\nType "pasteManager" to paste this folder in current directory');J=F(v);A(S)
					if J in B.listdir(B.getcwd()):
						if B.path.isfile(C):A(g)
						else:B.chdir(J)
					elif J==h:W.move(T,B.getcwd());break
			else:A(e)
	if f=='4':
		A('You chose to copy');A(Z)
		for E in M(O(D)):A(P(1+E)+Q+D[E])
		while G:
			H=F(R)
			if H in D:B.chdir(H+I);break
			else:A(V)
		while G:
			N();A(a);A(b);A('Type "copyManager" to copy this directory');C=F('\nChoose a file to copy: ');A(S)
			if C in B.listdir(B.getcwd()):
				if B.path.isfile(C):
					T=B.getcwd()+I+C;A('Move '+C+u)
					while G:
						for E in M(O(D)):A(P(1+E)+Q+D[E])
						L=F(R)
						if L in D:B.chdir(L+I);break
						else:A(V)
					while G:
						N();A('Type "pasteManager" to copy this file in current directory');J=F(q);A(S)
						if J in B.listdir(B.getcwd()):
							if B.path.isfile(C):A(g)
							else:B.chdir(J)
						elif J==h:W.copy(T,B.getcwd());break
				else:B.chdir(C)
			elif C==c:Y.exit(0)
			elif C==d:B.chdir(U)
			elif C=='copyManager':
				T=B.getcwd();A('Copying the current directory')
				while G:
					for E in M(O(D)):A(P(1+E)+Q+D[E])
					L=F(R)
					if L in D:B.chdir(L+I);break
					else:A(V)
				while G:
					N();A('\nType "pasteManager" to copy this file in current directory');J=F(v);A(S)
					if J in B.listdir(B.getcwd()):
						if B.path.isfile(C):A(g)
						else:B.chdir(J)
					elif J==h:A(T);z=T.split(I)[-1];A0=B.getcwd()+I+z;W.copytree(T,A0);break
			else:A(e)
	if f=='5':
		while G:
			A('\n1. Permanently \n2. Recycle Bin');s=F('Would you like to permanently delete or send to Recycle Bin?: ')
			if s==o:
				A('You chose to permanently delete files/folders.\n');A(Z)
				for E in M(O(D)):A(P(1+E)+Q+D[E])
				while G:
					H=F(R)
					if H in D:B.chdir(H+I);break
					else:A(V)
				while G:
					N();A(a);A(b);A('Type "deleteManager" to permanently delete this directory');C=F(w);A(S)
					if C in B.listdir(B.getcwd()):
						if B.path.isfile(C):
							A('Are you sure you want to permanently delete this file? (YES/NO)');X=F(i)
							if X.lower()==j or k:B.unlink(C)
						else:B.chdir(C)
					elif C==c:Y.exit(0)
					elif C==d:B.chdir(U)
					elif C==x:
						A('Are you sure you want to permanently delete this folder? (YES/NO)');X=F(i)
						if X.lower()==j or k:K=B.getcwd();B.chdir(U);W.rmtree(K)
					else:A(e)
			elif s==p:
				A('You chose to temporarily delete files/folders.');A(Z)
				for E in M(O(D)):A(P(1+E)+Q+D[E])
				while G:
					H=F(R)
					if H in D:B.chdir(H+I);break
					else:A(V)
				while G:
					N();A(a);A(b);A('Type "deleteManager" to send this directory to recycle bin');C=F(w);A(S)
					if C in B.listdir(B.getcwd()):
						if B.path.isfile(C):
							A(y);X=F(i)
							if X.lower()==j or k:r.send2trash(C)
						else:B.chdir(C)
					elif C==c:Y.exit(0)
					elif C==d:B.chdir(U)
					elif C==x:
						A(y);X=F(i)
						if X.lower()==j or k:K=B.getcwd();B.chdir(U);r.send2trash(K)
					else:A(e)
		else:A('You chose wrong number')
