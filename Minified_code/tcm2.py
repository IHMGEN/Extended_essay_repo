D=str
B=print
import re,http.client,time,os,argparse as E
from urllib.parse import urlparse as F
def G(url):
	J='GET';I='analysis';G=200;H=F(url)[1];A=F(url)[2]
	if I not in A:
		while G!=302:
			with http.client.HTTPConnection(H)as C:C.request(J,A);E=C.getresponse();G=E.status;B('[+] Scanning file...')
			time.sleep(15)
	B('[+] Scan Complete.');A=A.replace('file',I)
	with http.client.HTTPConnection(H)as C:C.request(J,A);E=C.getresponse();K=E.read()
	L=re.findall('Detection rate:.*\\)',K);M=L[1].replace("&lt;font color='red'&gt;",'').replace('&lt;/font&gt;','');B(f"[+] {D(M)}")
def H(filename):
	C=filename;B('[+] Uploading file to NoVirusThanks...');F=open(C,'rb').read();G={'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryF17rwCZdGuPNPT9U'};A='------WebKitFormBoundaryF17rwCZdGuPNPT9U';A+=f'\r\nContent-Disposition: form-data; name="upfile"; filename="{D(C)}"';A+='\r\nContent-Type: application/octet stream\r\n\r\n';A+=F;A+='\r\n------WebKitFormBoundaryF17rwCZdGuPNPT9U';A+='\r\nContent-Disposition: form-data; name="submitfile"\r\n';A+='\r\nSubmit File\r\n';A+='------WebKitFormBoundaryF17rwCZdGuPNPT9U--\r\n'
	with http.client.HTTPConnection('vscan.novirusthanks.org')as E:E.request('POST','/',A,G);H=E.getresponse();I=H.getheader('location')
	return I
if __name__=='__main__':
	C=E.ArgumentParser(usage='python3 virus_check.py FILENAME');C.add_argument('filename',type=D,metavar='FILENAME',help='specify the name of the file');I=C.parse_args();A=I.filename
	if not os.path.isfile(A):B(f"[+] {A} does not exist.");exit(0)
	else:J=H(A);G(J)
