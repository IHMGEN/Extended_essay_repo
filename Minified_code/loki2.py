C=SystemExit
import argparse as D,os
from core import PacketSniffer as E
from output import OutputToScreen as F
A=D.ArgumentParser(description='Network packet sniffer')
A.add_argument('-i','--interface',type=str,default=None,help='Interface from which Ethernet frames will be captured (monitors all available interfaces by default).')
A.add_argument('-d','--data',action='store_true',help='Output packet data during capture.')
B=A.parse_args()
if os.getuid()!=0:raise C('Error: Permission denied. This application requires administrator privileges to run.')
F(subject=(G:=E()),display_data=B.data)
try:
	for H in G.listen(B.interface):0
except KeyboardInterrupt:raise C('[!] Aborting packet capture...')
