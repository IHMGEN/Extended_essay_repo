#! /usr/bin/python

B=print
import sys,os as A,crypt,argparse as H
def I(cryptPass,dictFile):
	A=cryptPass;D=A[0:2]
	with open(dictFile,'r')as E:
		for F in E.readlines():
			C=F.strip('\n');G=crypt.crypt(C,D)
			if G==A:B('Found Password: {0}.'.format(C));return
	B('Password Not Found.')
def C():
	C=H.ArgumentParser();C.add_argument('passwordFile',help='An encrypted password file text. Each line contains the username and hashed password.');C.add_argument('dictionaryFile',help='A word dictionary');F=C.parse_args();D=F.passwordFile;E=F.dictionaryFile
	if not(A.path.isfile(D)and A.path.isfile(E)):B("Error. File(s) doesn't exists.");exit(0)
	if not(A.access(D,A.R_OK)and A.access(E,A.R_OK)):B('Error. File(s) have improper access permissions for user.');exit(0)
	with open(D)as J:
		for K in J.readlines():G=K.split(':');L=G[1].strip(' ');B('Cracking Password For: {0}'.format(G[0]));I(cryptPass=L,dictFile=E)
if __name__=='__main__':C()
