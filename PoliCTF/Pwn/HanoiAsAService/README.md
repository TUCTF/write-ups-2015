## HANOI As A Service 50 points
```
PoliCTF 2015
HANOI AS A SERVICE
50 Points - SOLVED
Check out our shiny new HaaS platform!
nc haas.polictf.it 80
```

## Challenge Overview
The challenge, "HANOI AS A SERVICE" was a pwn challenge. You are given a link to a server running a towers of HANOI 
service (big surprise). With pwn challenges, the purpose is to "pwn" a server or system by breaking the "sandbox" or 
program and gaining access to files or services that you were not intended to be able to access.

## Challenge Solution
When you first netcat to haas.polictf.it, you are greeted with:

Welcome to the Hanoi-as-a-Service cloud platform!
How many disks does your tower have?

It is impossible at this point to tell anything about the system we remoted into, so we enter input to see what is 
happening. Since the service is supposed to be able to work the Tower of Hanoi problem, we enter the number 3 to 
start with. It responds with:

        * Move top disk from a to b
        * Move top disk from a to c
        * Move top disk from b to c
        * Move top disk from a to b
        * Move top disk from c to a
        * Move top disk from c to b
        * Move top disk from a to b

That is just what we would expect from a HAAS. The next step is to try to break it, so we try a larger number: 100. 
The service responds with:

        Hey, this problem is too big for my poor mind...

So we have not yet broken it. It is programmed to reject numbers too high for it. Next we try irrational input such 
as -1. The response is:

        ERROR: Prolog initialisation failed:
        ERROR: Out of local stack

Bingo! We broke it. From these error messages, we notice that the language used to program the service is Prolog. 
Let’s attempt to break it a little more to get a better idea of what is going on. To do so, we try to enter a special 
character such as %. This yielded:

        ERROR: Prolog initialisation failed:
        ERROR: Syntax error: Unexpected end of clause
        ERROR: hanoi(  
        ERROR: ** here **
        ERROR: . 

Excellent! Now we can try different prolog commands an attempt to force the service to perform actions it was not 
intended to. Upon research, I discover that Prolog functions are in the form of func(args) and end with a comma. This 
agrees with the above output and confirms that Prolog is indeed the language being used.

Based on the above information, we decide to provide the input the program desires and then close the function, place 
a comma and run a second function. Based on research, the prolog command “exec()” allows us to run bash commands in 
the form of exec(ls). So our first input is:

        0),exec(ls

The resulting output gave us the directory listing of “/” meaning we are in the root directory of a linux machine. What 
it did not give us however is the flag. Our next step is to determine what our username is, so we run:

        0),exec(whoami

This tells us our username is: ctf. Based on the linux folder structure, we decide to check the contents of the ctf user’s 
home directory:

        0),exec(ls(’home/ctf’)

We can see a single directory: “haas”. So let’s check it out:

        0),exec(ls(‘home/ctf/haas’)

Which reveals:

        haas
        haas-proxy.py
        jhknsjdfhef_flag_here

At this point, we can taste victory:

        0),exec(cat(‘home/ctf/haas/jhknsjdfhef_flag_here’)

And, VICTORY!

                                        flag{Pr0gramm1ng_in_l0g1c_1s_c00l}
