#!/usr/bin/env python

A=print
import socket as B,sys as D,os
def H(ip,port):
	C='connection Failed'
	try:B.setdefaulttimeout(2);D=B.socket();D.connect((ip,port));C=D.recv(1024).decode('utf-8');return C
	except OSError as E:A('OS error: {0}'.format(E));return'OS error: '+str(E)
def I(banner,file):
	with open(file,'r')as A:
		for B in A.readlines():
			C=B.strip('\n')
			if C in banner.strip('\n'):return True
	return False
def C():
	if len(D.argv)==2:
		if os.path.exists(D.argv[1]):
			E=D.argv[1]
			if not os.access(E,os.R_OK):A('{0} cannot be read.'.format(E));exit(0)
			F={'ftp':21,'ssh':22,'smtp':25,'http':80};J='192.168.228.'
			for K in range(1,255):
				B=J+str(K)
				for C in F:
					A('Trying {0} protocol at {1} address'.format(C,B));G=H(B,F[C])
					if'No route to host'in G:break
					if not'OS error'in G:
						A('Connection to {0}:{1} successful.'.format(B,F[C]))
						if I(G,E):A('{0} Server is vulnerable at {1}'.format(C,B))
						else:A('{0} Server is not vulnerable at {1}'.format(C,B))
		else:A("File doesn't exist or file path cannot be determined.")
	else:A('VulnScanner.py requires 1 parameter.')
C()
