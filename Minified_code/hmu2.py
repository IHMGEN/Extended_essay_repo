E=str
B=print
import argparse as G,socket as A,threading as F
def H(tgt_host,tgt_ports):
	C=tgt_host
	try:D=A.gethostbyname(C)
	except A.herror:B(f"[-] Cannot resolve {C}: Unknown host");return
	try:E=A.gethostbyaddr(D);B(f"\n[+] Scan Results for: {E[0]}")
	except A.herror:B(f"\n[+] Scan Results for: {D}")
	A.setdefaulttimeout(1)
	for G in tgt_ports:H=F.Thread(target=I,args=(C,int(G)));H.start()
def I(tgt_host,tgt_port):
	C=tgt_port;D=F.Semaphore()
	with A.socket(A.AF_INET,A.SOCK_STREAM)as E:
		try:E.connect((tgt_host,C));E.send(b'ViolentPython\r\n');G=E.recv(100).decode('utf-8');D.acquire();B(f"[+] {C}/tcp open");B(f"   [>] {G}")
		except OSError:D.acquire();B(f"[-] {C}/tcp closed")
		finally:D.release()
if __name__=='__main__':D=G.ArgumentParser(usage='port_scan.py TARGET_HOST -p TARGET_PORTS\nexample: python3 port_scan.py scanme.nmap.org -p 21,80');D.add_argument('tgt_host',type=E,metavar='TARGET_HOST',help='specify target host (IP address or domain name)');D.add_argument('-p',required=True,type=E,metavar='TARGET_PORTS',help='specify target port[s] separated by comma (no spaces)');C=D.parse_args();C.tgt_ports=E(C.p).split(',');H(C.tgt_host,C.tgt_ports)
