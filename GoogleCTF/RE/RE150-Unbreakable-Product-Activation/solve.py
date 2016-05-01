from z3 import *
import os

# Binwalk was used to extract the binary out of the given archive
# Using Hex-Rays, we get a messy decompilation of each comparison function

# After a ton of cleaning of the C code using Sublime Text's regex feature,
# the result is a comparison expression for each byte. Throw these into
# Z3 and let the magic of SMT solvers do the problem for us.

solver = Solver()

# Make 50 byte objects (BitVec allow the XOR operation)
for i in range(0, 51):
    globals()['b%i' % i] = BitVec('b%i' % i, 8)

    # Ensure only ASCII input
    solver.add(globals()['b%i' % i] >= 32)
    solver.add(globals()['b%i' % i] <= 126)

solver.add(b0 == b6 + (b38 ^ b30) - b8)
solver.add(b1 == (b42 ^ (b38 ^ b20 ^ b19)))
solver.add(b2 == b35 + b36 - b19 - b3 - b44)
solver.add(b3 == b19 + (b17 ^ (b41 - b10 - b10)))
solver.add(b4 == b33 - b21)
solver.add(b5 == (b4 ^ (b4 ^ b8 ^ b39)))
solver.add(b6 == (b14 ^ (b10 + b25 - b39)))
solver.add(b7 == b32 + (b15 ^ b1))
solver.add(b9 == (b24 ^ b7))
solver.add(b10 == b32 + (b49 ^ b17) - b4)
solver.add(b11 == (b42 ^ b38) - b17 - b8)
solver.add(b12 == b14 + b8)
solver.add(b13 == b45 + b20)
solver.add(b14 == b9 + (b20 ^ (b25 - b48)))
solver.add(b15 == b18 - b31)
solver.add(b16 == (b24 ^ b46))
solver.add(b17 == ((b50 ^ b14) ^ (b47 + b2 + b13)))
solver.add(b18 == b0 + b36 + b44 - b3 )
solver.add(b19 == (b41 ^ b30) - b25 - b28)
solver.add(b20 == (b25 ^ b44))
solver.add(b21 == b25 + ((b28 + b22) ^ (b39 ^ b21)) )
solver.add(b22 == (b31 ^ (b44 - b4 - b12)) - b30)
solver.add(b23 == (b39 ^ (b32 - b14)))
solver.add(b24 == (b21 ^ (b0 ^ b18 ^ b21)))
solver.add(b25 == b18 + b4 + (b12 ^ b17) - b11)
solver.add(b26 == (b32 ^ b46) + b49 + b20)
solver.add(b27 == b36 + b25 + b39 - b48)
solver.add(b28 == (b14 ^ b15))
solver.add(b29 == b1 + b35 - b42)
solver.add(b30 == b8 - b31 - b30 - b24)
solver.add(b31 == (b42 ^ (b15 + b18 - b29)))
solver.add(b32 == b14 + b5 + b15 - b44)
solver.add(b33 == (b20 ^ (b45 - b15)) - b32)
solver.add(b34 == (b3 ^ b33) - b20 - b10)
solver.add(b34 == (b3 ^ b33) - b20 - b10)
solver.add(b35 == (b44 ^ (b6 - b43)) + b1 - b44)
solver.add(b36 == (b49 ^ (b31 + b25 - b28)))
solver.add(b37 == b11 + (b34 ^ b31) - b34)
solver.add(b38 == b42 + (b27 ^ b36) - b5)
solver.add(b39 == (b37 ^ b8))
solver.add(b40 == (b44 ^ (b7 + b28)) - b10)
solver.add(b41 == (b20 ^ (b7 ^ b17 ^ b26)))
solver.add(b42 == b50 + b1 - b28)
solver.add(b43 == b46 + b33 - b15)
solver.add(b44 == ((b24 + b42 + b16) ^ (b45 ^ b21)))
solver.add(b45 == b22 - b40)
solver.add(b46 == b12 - b46 - b7 - b35)
solver.add(b47 == (b39 ^ (b15 + b26)) - b12)
solver.add(b48 == (b11 ^ (b15 - b8)))
solver.add(b49 == (b27 ^ b37))
solver.add(b50 == ((b13 + b8 + b17) ^ (b24 ^ b15)))

print("Solving...")

# Solve the equations
solver.check()
modl = solver.model()

# Create an ASCII string from the resulting bytes
res = ""
for i in range(0,51):
    obj = globals()['b%i' % i]
    c = modl[obj].as_long()
    print('b%i: %x' % (i, c))
    res = res + chr(c)

# Result: CTF{0The1Quick2Brown3Fox4Jumped5Over6The7Lazy8Fox9}
print("Result: " + res);

# Pass it to the executable to ensure it passes
os.system("./76.elf \"%s\"" % res)
