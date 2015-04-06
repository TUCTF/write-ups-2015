	# This is a python script for the qr challange for backdoor ctf on 4-1-15.
	# The challange was to get a QR code from a server (they recommended netcat in the challange)
	# and to translate it into the text value, and send it back to the server, which would then
	# give you another qr code. This continues for many times before you get a message with the flag.
	# In this code exits automatically (via exceptions, but hey it still exits).
	# This code also is not 100% accurate. It may take several runs of it to get the flag.



import os
import qrtools
import subprocess
import time
import socket
import select
class imageHelper():
	def __init__(self):
		self.net = Netcat('hack.bckdr.in',8010)
	def main(self):
		'''Concept is simple. connect to the server, get the QR code, read it and send the value back to the server for the next code.'''
		while 1:
			time.sleep(0.1)	#In case the server needed a second to breath. I was getting partial messages, so I threw this in.
			rawMsg = self.net.read()	#Read the code
			msgAry = rawMsg.split('\n')
			self.saveImage(msgAry)		#Save the text as an image so qrtools can read it. Probably an easier way, but this worked.
			qr = qrtools.QR()
			qr.decode("test.png")
			print qr.data				#Prints the value of the code
			s = self.getSum(qr.data)	#Prints the sha256sum to the concol in case we need it.
			self.net.send(qr.data+'\n')	#Send back the data from the code.
	def saveImage(self,text):
		'''Takes text from the code and saves it as an image.'''
		from PIL import Image, ImageDraw, ImageFont, ImageFilter

		#configuration
		font_size=10
		width=800
		height=800
		back_ground_color=(255,255,255)
		font_size=10
		font_color=(0,0,0)

		im  =  Image.new ( "RGB", (width,height), back_ground_color )
		draw  =  ImageDraw.Draw ( im )
		unicode_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", font_size)	#Might be different path for you.
		#You will need a mono, unicode font for this to work.
		vPos=0
		for unicode_text in text:	#'Print' every line on a new position since draw.text doesn't recognise newline characters
			draw.text ( (10,vPos), unicode_text.decode('utf-8'), fill=font_color, font=unicode_font )	#Replace the space with unicode for spacing
			vPos+=10	#font size of 10, so 10 between characters vertically

		im.save("test.png")

	def getSum(self,text):
		'''Generates the sha256sum of the text'''
		from Crypto.Hash import SHA256
		h = SHA256.new();
		h.update(text);
		print h.hexdigest()

		return h.hexdigest()

class Netcat:
	'''This is a basic socket interface I wrote on the fly. It is not the best, but it works.'''
	def __init__(self, hostname, port):
		self.hostname = hostname
		self.port = port

		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((self.hostname, self.port))
		#Need percistant connection, if you connect and disconnect every time, you won't get the flag.
	def read(self):
		'''Reads the qr code from the server'''
		qrCode=''
		self.socket.settimeout(0.5)	#I needed to set this since I was too lazy to look up select. 0.5 seemed to be the best timeout
		print 'getting new one'
		while 1:
			time.sleep(0.02)	#Again, without this I was getting weird problems with recieving full codes. This smoothed everything out.
			try:
				data = self.socket.recv(1024)	#timeout causes an exception, so it needs to be caught and in this case end the message
			except:
				break
			#Below are my previous attempts to find the end of a message. If they fail, the timeout will solve it.
			if '\n                                                                                              \n' in data:
				qrCode+=data	#Make sure you add this to the total, as it is part of the message
				break
			if len(data) < 500:
				print data
			if len(data) < 4:
				break
			qrCode+=data
		print '------------------------------------------'	#Prints it so you have some output to look at...
		print qrCode
		print '------------------------------------------'
		return qrCode
	def send(self,content):
		'''simple method to send data back to the server.'''
		self.socket.sendall(content)

if __name__ == '__main__':
	im = imageHelper()
	im.main()