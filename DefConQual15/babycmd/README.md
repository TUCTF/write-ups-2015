##Baby's first: babycmd

###Overview
We are given the hostname and port ```babycmd3ad...00b.quals.shallweplayaga.me:15491``` 
as well as a program binary. First things first we download the binary and run file. 

```
$ file babycmd 
babycmd: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, stripped
```

Running the program let's us see the program accepts arguments to the commands ping, dig and host.
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

The commands seem to be executed through their respective programs so this leads us to think this 
could be a command injection challenge. The goal would be to execute our own commands instead of 
ping, dig, and host.
