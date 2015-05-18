##Baby's first mathwiz

###Overview
We are given the hostname and port ```mathwhiz_c951d46fed68687ad93a84e702800b7a.quals.shallweplayaga.me:21249```. 
Upon connecting to the service we are presented with a math problem of the following 
format, ```3 + 1 = ```. Upon entering the solution we are presented with another question. 
If the answer isn't entered in quick enough, their service kicks you off. Since this 
is a highly repetitve challenge, I decided to code a solution in python.

###Let's get to it
Python has a wonderful function (eval) that will evaluate a string and give you back the result. 
This is exactly what I needed! This first attempt at a solution connected to the service, 
received the equation to solve, stripped the equals sign off the end and sent back the 
result of eval on that string. 
```python
from pwn import *

r = remote("mathwhiz_c951d46fed68687ad93a84e702800b7a.quals.shallweplayaga.me", "21249")

while (True):

 s = s.replace(" =", "")
 ans = str(eval(x))
 print "Answer: " + ans
 r.send(ans + "\n")
  
r.close()
```
Unfortunately after several rounds the script was erroring out. The format of the question 
was being changed to include '[]' inplace of parentheses. Making this modification would 
work for a few more rounds and then a new error would occur. Same issue, '{}' instead of 
parenthese. After this fix '^' was being used to represent exponentiation so I replaced 
all '^' with '**'. The next trick was the usage of words to represent numbers. Doing a lookup 
in a python dictionary was the easiest solution since all numbers appeared to be either 1, 2, or 3. 
The last trick they threw out was the combination of words and parenthese. After implementing 
that fix, the code ran for a thousand rounds. Final code was:
```python
from pwn import *

r = remote("mathwhiz_c951d46fed68687ad93a84e702800b7a.quals.shallweplayaga.me", "21249")

number = {'one':1,'two':2, 'three':3,}

count = 1
while (True):
 
 s = r.recv()
 
 if count == 1001:
  print s
  break

 s = s.replace(" =", "").replace("[", "(").replace("]", ")").replace("{","(").replace("}",")").replace("\n", "").replace("^","**")
 t = s.split(" ")
 x = ""

 for word in t:
  if number.has_key(word.lower().strip("()")):
   if "(" in word:
    x += "(" + str(number[word.lower().strip("()")])
   elif ")" in word:
    x += str(number[word.lower().strip("()")]) + ")"
   else:
    x += str(number[word.lower().strip("()")])
  else:
   x += word

 ans = str(eval(x))
 #print "Answer: " + ans
 r.send(ans + "\n")
 count += 1
  
r.close()
#RyanAiden
```
The flag was ```Fara says you are a FickenChucker and you'd better watch Super Trooper 2```
