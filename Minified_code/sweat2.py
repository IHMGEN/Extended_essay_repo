E=print
D=range
C=int
from multiprocessing import Pool,cpu_count as B
import argparse as F,math,sys
G=1024*1024
def H(x):
	while True:
		for A in D(1,C(math.sqrt(x))+1):
			if x%A==0:x**x
		x**x
def J():D=False;A=F.ArgumentParser(description='CPU and Memory stressermade in python');A.add_argument('-m','--memory',type=C,default=1024,help='The amount of memory in megabytes to eat',required=D);A.add_argument('-c','--cores',type=C,default=B(),help='The amount of logical cores to stress',required=D);E=A.parse_args();return E
if __name__=='__main__':
	A=parse_command_args().cores;K='L'*G*parse_command_args().memory
	if A>B():E(f"Too many threads running! You are only able to run {B()} threads at a time!");sys.exit(1)
	E(f"Stressing {A} cores");I=Pool(A);I.map(H,D(A))
