#!/usr/bin/env python

D='cisco'
C=str
import sys
from argparse import ArgumentParser as E
from ncclient import manager as F
import xml.dom.minidom
if __name__=='__main__':A=E(description='Select options.');A.add_argument('--host',type=C,required=True,help='The device IP or DN');A.add_argument('-u','--username',type=C,default=D,help='Go on, guess!');A.add_argument('-p','--password',type=C,default=D,help='Yep, this one too! ;-)');A.add_argument('--port',type=int,default=830,help='Specify this if you want a non-default port');B=A.parse_args();G=F.connect(host=B.host,port=B.port,username=B.username,password=B.password,device_params={'name':'csr'});H='\n                      <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">\n                          <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">\n                          </native>\n                      </filter>\n                      ';I=xml.dom.minidom.parseString(C(G.get_config('running',H)));print(I.toprettyxml(indent='  '))
