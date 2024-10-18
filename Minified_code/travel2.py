#!/usr/bin/env python3
P='text/html'
O=b'<hr>\n'
N=b'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">'
M=IOError
I='text/plain'
H='Content-Length'
G='Content-type'
C=print
E='/'
D=str
F=len
__version__='0.1'
__all__=['SimpleHTTPRequestHandler']
__author__='bones7456'
__home_page__='http://li2z.cn/'
import os as A,posixpath as J,http.server,urllib.request,urllib.parse,urllib.error,cgi,shutil as Q,mimetypes as B,re
from io import BytesIO as K
import socket as L
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
	server_version='SimpleHTTPWithUpload/'+__version__
	def do_GET(A):
		B=A.send_head()
		if B:A.copyfile(B,A.wfile);B.close()
	def do_HEAD(B):
		A=B.send_head()
		if A:A.close()
	def do_POST(B):
		E,F=B.deal_post_data();C((E,F,'by: ',B.client_address));A=K();A.write(N);A.write(b'<html>\n<title>Upload Result Page</title>\n');A.write(b'<body>\n<h2>Upload Result Page</h2>\n');A.write(O)
		if E:A.write(b'<strong>Success:</strong>')
		else:A.write(b'<strong>Failed:</strong>')
		A.write(F.encode());A.write(('<br><a href="%s">back</a>'%B.headers['referer']).encode());I=A.tell();A.seek(0);B.send_response(200);B.send_header(G,P);B.send_header(H,D(I));B.end_headers()
		if A:B.copyfile(A,B.wfile);A.close()
	def deal_post_data(C):
		H=False;J=C.headers['content-type']
		if not J:return H,"Content-Type header doesn't contain boundary"
		K=J.split('=')[1].encode();E=int(C.headers['content-length']);B=C.rfile.readline();E-=F(B)
		if not K in B:return H,'Content NOT begin with boundary'
		B=C.rfile.readline();E-=F(B);G=re.findall('Content-Disposition.*name="file"; filename="(.*)"',B.decode())
		if not G:return H,"Can't find out file name..."
		L=C.translate_path(C.path);G=A.path.join(L,G[0]);B=C.rfile.readline();E-=F(B);B=C.rfile.readline();E-=F(B)
		try:I=open(G,'wb')
		except M:return H,"Can't create file to write, do you have permission to write?"
		D=C.rfile.readline();E-=F(D)
		while E>0:
			B=C.rfile.readline();E-=F(B)
			if K in B:
				D=D[0:-1]
				if D.endswith(b'\r'):D=D[0:-1]
				I.write(D);I.close();return True,"File '%s' upload success!"%G
			else:I.write(D);D=B
		return H,'Unexpect Ends of data.'
	def send_head(B):
		C=B.translate_path(B.path);I=None
		if A.path.isdir(C):
			if not B.path.endswith(E):B.send_response(301);B.send_header('Location',B.path+E);B.end_headers();return
			for F in('index.html','index.htm'):
				F=A.path.join(C,F)
				if A.path.exists(F):C=F;break
			else:return B.list_directory(C)
		K=B.guess_type(C)
		try:I=open(C,'rb')
		except M:B.send_error(404,'File not found');return
		B.send_response(200);B.send_header(G,K);J=A.fstat(I.fileno());B.send_header(H,D(J[6]));B.send_header('Last-Modified',B.date_time_string(J.st_mtime));B.end_headers();return I
	def list_directory(C,path):
		try:list=A.listdir(path)
		except A.error:C.send_error(404,'No permission to list directory');return
		list.sort(key=lambda a:a.lower());B=K();J=cgi.escape(urllib.parse.unquote(C.path));B.write(N);B.write(('<html>\n<title>Directory listing for %s</title>\n'%J).encode());B.write(('<body>\n<h2>Directory listing for %s</h2>\n'%J).encode());B.write(O);B.write(b'<form ENCTYPE="multipart/form-data" method="post">');B.write(b'<input name="file" type="file"/>');B.write(b'<input type="submit" value="upload"/></form>\n');B.write(b'<hr>\n<ul>\n')
		for F in list:
			L=A.path.join(path,F);I=M=F
			if A.path.isdir(L):I=F+E;M=F+E
			if A.path.islink(L):I=F+'@'
			B.write(('<li><a href="%s">%s</a>\n'%(urllib.parse.quote(M),cgi.escape(I))).encode())
		B.write(b'</ul>\n<hr>\n</body>\n</html>\n');Q=B.tell();B.seek(0);C.send_response(200);C.send_header(G,P);C.send_header(H,D(Q));C.end_headers();return B
	def translate_path(F,path):
		B=path;B=B.split('?',1)[0];B=B.split('#',1)[0];B=J.normpath(urllib.parse.unquote(B));D=B.split(E);D=[A for A in D if A];B=A.getcwd()
		for C in D:
			G,C=A.path.splitdrive(C);H,C=A.path.split(C)
			if C in(A.curdir,A.pardir):continue
			B=A.path.join(B,C)
		return B
	def copyfile(A,source,outputfile):Q.copyfileobj(source,outputfile)
	def guess_type(B,path):
		C,A=J.splitext(path)
		if A in B.extensions_map:return B.extensions_map[A]
		A=A.lower()
		if A in B.extensions_map:return B.extensions_map[A]
		else:return B.extensions_map['']
	if not B.inited:B.init()
	extensions_map=B.types_map.copy();extensions_map.update({'':'application/octet-stream','.py':I,'.c':I,'.h':I})
def R(HandlerClass=SimpleHTTPRequestHandler,ServerClass=http.server.HTTPServer):E=L.gethostname();B=L.gethostbyname(E);B=D(B);A='http://'+B+':8000/';A=D(A);A=A.replace(' ','');C('Press CTRL + C to stop\n');C('Can be accessed from the local network via <<  ',A,'  >>\n');C('Local address:');http.server.test(HandlerClass,ServerClass)
if __name__=='__main__':R()
