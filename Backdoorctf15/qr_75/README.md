# qr 75 points

##Overview
When you run
~ nc hack.bckdr.in 8010
You will get back what looks to be a version 10 QR code

At this point there are a couple options to solve this.
I chose a very inefficient route, but one that I believed would take the least effort on my end.
This is all programmed in python 2.x

##Netcat
The url and port can be opened with the socket module.
Then you can use recv to get the qr code from the server.
Adding a timeout of 0.5 to the socket will let you know when the server is done sending the qr code.
You should really use select, but I was lazy.
Once you have the reply, the socket send command will send your message to the server.

##Qr code:
This is where I went the long way around.
I split the qr code up to an array based on newlines
I then created a picture 800x800 using PIL
So then we had to print the text into the image.
We have to use a mono, unicode font in order to represent the qr code correctly.
I selected DejaVuSansMono since it was the first Google result.
Then simply loop through the qr array and print the lines 10 pts appart vertically
(since I set the font size to 10)
Then save the image.
Now we have an image of the qr code, we can use qrtools to read it in, and give us text
(yes, we are going from sockets->textQR->imageQR->OCRQR->QRvalue->flag)
Again, complicated, but it worked. most of the time.
Then we use socket.send to send the code back to the server which would then give us the next qr code.

##Code Overview (psudo code):
	Set up my Netcat class to connect to the server
	While true:
		get qr-text from server
		make it an image
		analize image with qrtools
		send result back to server

Eventually (I think after 20 or 50 ones) you will not get a qr code.
Instead of a QR code, you get back
	Congratulations. Flag is [Redacted]
