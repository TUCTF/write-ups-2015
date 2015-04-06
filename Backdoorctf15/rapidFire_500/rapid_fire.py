	# This code also is not 100% accurate. It may take several runs of it to get the flag.


#Import all of the things!
import os
import qrtools
import subprocess
import time
import socket
import select
import re
import hashlib
from pwn import *
from countrycode import countrycode
import requests, sys, telnetlib, BeautifulSoup
from Crypto.Hash import SHA256
import traceback

class rapidFire():
	def __init__(self):
		time.sleep(1)
		self.net = Netcat('104.236.169.87',8008)
		#Read in the lists of things that can't be computed on the fly.
		self.primes = []
		with open('saneprimes1','r') as p:
			for i in p.readline().split(' '):
				self.primes.append(i)
		self.pi = []
		with open('pimili','r') as p:
			for i in p.readline():
				self.pi.append(i)
		self.fib = []
		with open('fib','r') as f:
			for i in f.readline().split(' '):
				self.fib.append(i)

	def main(self):
		'''get the question and send the answer back to the server for the next code.'''
		cnt = 0 	#to count the rounds
		while 1:
			try:	
				rawMsg = self.net.read()	#Read the question
				msgAry = rawMsg.split('\n')
				answer = self.getAnswer(msgAry[-2])	#Get the answer with the 2nd to last line as the question
				if answer != None:
					self.net.send(str(answer)+'\n')	#Send back the data from the code.
				cnt+=1
			except:		#This is just for fun. It will create a file listing the furthest it got
				with open('status','a') as s:
					s.write(str(cnt)+',')
				print(traceback.format_exc())
				break
	def getAnswer(self,text):
		#because python doesn't have a switch
		print 'answer: '
		if 'prime number' in text:
			return self.prime(text)
		elif 'binary' in text:
			return self.binary(text)
		elif 'natural odd numbers' in text:
			return self.naturaloddNums(text)
		elif 'natural numbers' in text:
			return self.naturalNums(text)
		elif 'digit in pi' in text:
			return self.digitPi(text)
		elif 'fibonacci' in text and 'sum' not in text:
			return self.fibonacci(text)
		elif 'fibonacci' in text:
			return self.fibonacciSum(text)
		elif 'md5 hash' in text:
			return self.md5hash(text)
		elif 'country' in text:
			return self.country(text)
		elif '2 digit code' in text:
			return self.countryCode(text)
		elif 'release year of' in text:
			return self.releaseYear(text)
		else:
			print 'unknown question!'
			print text

	def prime(self,text):
		n = re.findall(r'\d+', text)
		num = int(n[0])
		return self.primes[num]

	def binary(self,text):
		n = re.findall(r'\d+', text)
		num = int(n[0])
		return bin(num)[2:]

	def naturaloddNums(self,text):
		n = re.findall(r'\d+', text)
		num = int(n[0])
		return num**2

	def naturalNums(self,text):
		n = re.findall(r'\d+', text)
		num = int(n[0])
		return (num*(num+1))/2

	def getSum(self,text):
		h = SHA256.new();
		h.update(text);
		return h.hexdigest()

	def digitPi(self,text):
		n = re.findall(r'\d+', text)
		num = int(n[0])
		return self.pi[num]

	def fibonacci(self,text):
		#-1 is beacuse the fib list reads: 1, 1, 2, 3, 5,...
		n = re.findall(r'\d+', text)
		num = int(n[0])
		return self.fib[num-1]

	def fibonacciSum(self,text):
		n = re.findall(r'\d+', text)
		num = int(n[0])
		s=0
		s=int(self.fib[num+1]) -1	#The formula is fib[n+2]-1, but again the list has 1 twice
		return str(s)

	def md5hash(self,text):
		n = re.findall(r'\d+', text)
		num = n[1]
		m = hashlib.md5()
		m.update(num)
		d = m.hexdigest()
		return d

	def country(self,text):
		#This is the main cause of failure. Could do with some improvement
		n = text.split('country of ')[1]
		if 'British Indian Ocean Territory' in n:	#Because for some reason this doesn't work.
			return 'IO'
		params = { 'q':n }
		r = requests.get('http://www.geonames.org/search.html', params=params)
		soup = BeautifulSoup.BeautifulSoup(r.text.encode('utf8'))
		#The rest is to grab the first country that has a city with the given name.
		for tr in soup.findAll('tr'):
			tds = tr.findAll('td')
			if len(tds)!=6: continue
#			if 'united-kingdom' in tds[2]:
#			print tds[2].a['href'].strip('/countries/').split('/')
			return tds[2].a['href'].strip('/countries/').split('/')[1].split('.html')[0].replace('-', ' ').title().replace('United Kingdom','Britain').replace('Ivory Coast', 'Lacs')
		print 'I don\'t know this city, I am going to return Titty Sprinkles'
		return 'Titty Sprinkles'


	def countryCode(self, text):
		n = text.split(' digit code of ')[1]
		return countrycode(codes=n, origin='country_name', target='iso2c').replace('Tokelau','TK')
	
	def releaseYear(self, text):
		n = text.split('release year of ')[1]
		params = { 'q':n,'ref':'nv_sr_fn','s':'tt'}		#Only search movie titles on imdb. Paramaters were gathered by looking at the url
		r = requests.get('http://www.imdb.com/find?', params=params)
		soup = BeautifulSoup.BeautifulSoup(r.text.encode('utf8'))
		# Grep IMDB for all movies with that title, and select the first year in the form (dddd).
		return re.findall(r"\([0-9]{4}\)", str(soup))[0][1:-1]		#have to take off the ()

class Netcat:
	'''This is a basic socket interface using pwntools remote.'''
	def __init__(self, hostname, port):
		self.hostname = hostname
		self.port = port
		self.r = remote(self.hostname, self.port)
	def read(self):
		'''Reads the qr code from the server'''
		data=''
		print 'getting new one'
		nc = 0
		try:
			data = self.r.recv(timeout=0.35)
		except:
			pass
		if 'flag:' in data:	#We did it!
			with open('flag','w+') as flg:
				flg.write(data)
		print '------------------------------------------'	#Prints it so you have some output to look at...
		print data
		print '------------------------------------------'
		return data
	def send(self,content):
		'''simple method to send data back to the server.'''
		print 'sending: ',content
		self.r.send(content)

if __name__ == '__main__':
	im = rapidFire()
	im.main()