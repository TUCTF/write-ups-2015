from pwn import *

r = remote("mathwhiz_c951d46fed68687ad93a84e702800b7a.quals.shallweplayaga.me", "21249")

number = {'one':1,'two':2, 'three':3,}

count = 1
while (True):
 
 s = r.recv()
 
 if count == 1001:
  print s
  break

 # print s.strip("\n")
 s = s.replace(" =", "").replace("[", "(").replace("]", ")").replace("{","(").replace("}",")").replace("\n", "").replace("^","**")
 t = s.split(" ")
 x = ""

 for word in t:
  if number.has_key(word.lower().strip("()")):
   if "(" in word:
    x += "("
    x += str(number[word.lower().strip("()")])
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
