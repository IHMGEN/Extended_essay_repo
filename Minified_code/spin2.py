G='{ip:20} {mac:20} {type:10}'
F='response'
E=False
C=print
import requests as A
A.packages.urllib3.disable_warnings()
D='https://sandboxapic.cisco.com/api/v1'
H='devnetuser'
I='Cisco123!'
def J(url):B='/ticket';C={'username':H,'password':I};D={'content-type':'application/json'};url+=B;G=A.post(url,json=C,headers=D,verify=E).json();return G[F]['serviceTicket']
def K(token,url):B='/host';C={'X-AUTH-TOKEN':token};url+=B;D=A.get(url,headers=C,verify=E).json();G=D[F];return G
L=J(D)
M=K(L,D)
C('Client List from APIC-EM')
C(G.format(ip='IP Address',mac='MAC Address',type='Type'))
for B in M:C(G.format(ip=B['hostIp'],mac=B['hostMac'],type=B['hostType']))
