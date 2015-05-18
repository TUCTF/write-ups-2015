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

# finish code here (get that file from my VM)
```

## Uncovering hidden form fields
If we look at the code for the form, we realize that inside the <form> ... </form> block there are some fields 
with type="hidden" as an attribute. Getting rid of the hidden tags reveals extra options, including a field 
labeled *nonce* with a string already in it. I don't exactly remember what I did here, but I think this will reveal a 
place to put in a value for the *nonce*. I think I just used the one given to me in the clue. You can then click the 
Sign in button below and get in.

*note: I'll work on getting the actual html from the web app. The site is currently down and I'm not 
sure if they will put it back up. I might have it downloaded though*
