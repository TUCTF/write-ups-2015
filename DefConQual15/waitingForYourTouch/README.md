# Overview
The sole web challenge this year, "Waiting for Your Touch", baisically boils down to identifying hidden elements on a 
web page and making them visible.

I should note that as I solved the challenge I didn't keep a whole lot of info that may have helped with documentation.
I'm kind of going off of memory here, so it may not be *entirely* accurate, but it is accurate to the best of my knowledge.

## A First look
The challenge asks you to visit http://waiting-for-your-touch.quals.shallweplayaga.me/. 
You are given a username and password to access the site (it changed during the competition due to technical 
difficulties with the server's web sockets). Once you log in, you are presented with two text boxes, one with 
a randomly generated hex number and another that is blank labeled "proof-of-work r" next to a Solve button. The
text below the box provides a hint as to what the whole system actually does. It says:

> "Given nonce <some other random hex string>, give us UTF-8 charachters such that MD%(nonce + r) ends with <some number> zero bits."

If you enter something into the first box, click solve next to the "proof-of-work r" box, the web application 
with try values of r, in ascending order, until that value plus the value of the box above, passed through 
the md5 hash algorithm, end with the number of zeroes specified in the clue. We can verify this with the following 
Python code:

```
import md5

hex_input = raw_input("Please input the string: ").decode('utf-8')
print hex_input
end_bits = '0'*15

r = 0
flag = True
while flag:
	hex_data = md5.new(hex_input + str(r)).hexdigest()
	print hex_data
	scale = 16 

	num_of_bits = len(hex_data) * 4

	binary_data = bin(int(hex_data, scale))

	if binary_data.endswith(end_bits):
		print "r of length " + str(r)  " succeeded!"
		flag = False
	else:
		print "tried r of length " + str(r) + ". No success "
		r += 1
```

I wrote this code up before realizing that "proof-of-concept r" did the exact same thing, but it was useful in verifying what I thought the box did.

There was a sign in button at the bottom of the page, but clicking it results in an error. In order to log in we need to make some hidden form fields visible.

## Uncovering hidden form fields
If we look at the code for the form, we realize that inside the <form> ... </form> block there are some fields 
with type="hidden" as an attribute. Getting rid of the hidden tags reveals extra options, including a field 
labeled *nonce* with a string already in it. I don't exactly remember what I did here, but I think this revealed a 
place to put in a value for the *nonce*. I think I just used the one given to me in the clue. I think there was a field for "r", which you can calculate using the proof of concept field or the python script you created. You can then click the Sign in button below and get in without an error.

*note: I'll work on getting the actual html from the web app. The site is currently down and I'm not 
sure if they will put it back up. I might have it downloaded though*
