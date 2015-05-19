# Overview
The sole web challenge this year, "Waiting for Your Touch", baisically boils down to identifying hidden elements on a 
web page and making them visible, along with interpreting hints that the web app gives you.

I should note that as I solved the challenge I didn't keep a whole lot of info that may have helped with documentation. I'm kind of going off of memory here, so it may not be *entirely* accurate, but it is accurate to the best of my knowledge.

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

```python
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
If we look at the code for the form, we realize that inside the `<form> ... </form>` block there are some fields 
with type="hidden" as an attribute. Getting rid of the hidden tags reveals extra options, including a field 
labeled *nonce* with a string already in it. I don't exactly remember what I did here, but I think this revealed a 
place to put in a value for the *nonce*. I think I just used the one given to me in the clue. I think there was a field for "r", which you can calculate using the proof of concept field or the python script you created. You can then click the Sign in button below and get in without an error.

## Inside the application
The application now says you are logged in with a username that matches the nonce field from the previous page. There is a message in bold that says

> The button is *not* waiting for your touch

The page also says something along the lines of "you are too young to create new users" and has a timer that is counting up the number of seconds since login. Quite interesting, and it indicates that users can be modified and created from the app. We also see the "Proof-of-work r" field with a solve button, but no name field visible as there was initally.

The hints seem to indicate that we must create, or at least modify, users. Since we are "too young", we need to trick the app into thinking that we have been a user for longer than we actually are.

There is a button on the page that says **click**. Although we don't know this yet, clicking the button will yield the flag. Unfortunately, the button is disabled. You can enable it by removing the button's *disabled* field in the HTML, but if you try to click it, an error results. I think it may have said something about being too young, but I'm not sure.

There is a toolbar at the top of the application, with links to **high scores**, **edit user**, and **log out**. **High scores** didn't prove to be all that useful. May have just been a place to showcase all the user accounts "created" or something. I didn't look too far into it. **Edit user** is where the magic happens.


## The Edit User tab

At first glance all that we can see is **Name** and ""Proof-of-work r", just as before. But inspecting the HTML reveals some commented out code that lets you change the "Created at" date.

```html
<!--
<p>
<label for="user_created_at">Created at</label>
<input disabled="disabled" type="text" value="2015-05-17 19:15:09 +0000" name="user[created_at]" id="user_created_at" />
</p>
-->
```

Simply remove the `<!--` and `-->`, as well as the disabled field, and you can modify your user's creation date. Just set it to something really high and then go back to the main page, and ...











