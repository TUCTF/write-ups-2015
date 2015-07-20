## John The Dropper 100 Points

## Challenge Overview
The description for this challenge was: 
```
I am afraid John is in trouble. I feel he needs help but I can't find any message from him.
dropper.polictf.it
About John The Dropper: John does not need a port to communicate
```

This challenge stumped us for quite some time. After trying a couple of things, one of us noticed certain pings were being dropped. The pattern of dropped packets did not change so we knew this was part of the problem. We ended up pinging `dropper.polictf.it` about 1000 times and saw after ~500, no more ping packets were dropped. This is were we got stuck for a good bit, turns out sleep helps a lot because come morning we got it. The statement `I am afraid John is in trouble. I feel he needs help but I can't find any message from him` really had me thinking it was morse code. After a lot of staring, a lot of caffeine, and a pure whim, we finally made the seemingly random pattern spell out the begginning of a message. At that point we knew it was just a matter of scripting it. 


## Challenge Solution
The first section of the ping data looked like this:
```
64 bytes from 52.18.119.20: icmp_seq=0 ttl=51 time=138.221 ms
64 bytes from 52.18.119.20: icmp_seq=1 ttl=51 time=139.060 ms
Request timeout for icmp_seq 2
64 bytes from 52.18.119.20: icmp_seq=3 ttl=51 time=149.801 ms
Request timeout for icmp_seq 4
64 bytes from 52.18.119.20: icmp_seq=5 ttl=51 time=139.272 ms
Request timeout for icmp_seq 6
64 bytes from 52.18.119.20: icmp_seq=7 ttl=51 time=154.396 ms
64 bytes from 52.18.119.20: icmp_seq=8 ttl=51 time=135.580 ms
Request timeout for icmp_seq 9
Request timeout for icmp_seq 10
Request timeout for icmp_seq 11
64 bytes from 52.18.119.20: icmp_seq=12 ttl=51 time=135.926 ms
Request timeout for icmp_seq 13
Request timeout for icmp_seq 14
Request timeout for icmp_seq 15
64 bytes from 52.18.119.20: icmp_seq=16 ttl=51 time=138.165 ms
Request timeout for icmp_seq 17
Request timeout for icmp_seq 18
Request timeout for icmp_seq 19
64 bytes from 52.18.119.20: icmp_seq=20 ttl=51 time=146.318 ms
64 bytes from 52.18.119.20: icmp_seq=21 ttl=51 time=137.234 ms
Request timeout for icmp_seq 22
64 bytes from 52.18.119.20: icmp_seq=23 ttl=51 time=136.761 ms
Request timeout for icmp_seq 24
64 bytes from 52.18.119.20: icmp_seq=25 ttl=51 time=141.535 ms
Request timeout for icmp_seq 26
64 bytes from 52.18.119.20: icmp_seq=27 ttl=51 time=136.211 ms
64 bytes from 52.18.119.20: icmp_seq=28 ttl=51 time=135.184 ms
64 bytes from 52.18.119.20: icmp_seq=29 ttl=51 time=135.941 ms
64 bytes from 52.18.119.20: icmp_seq=30 ttl=51 time=135.376 ms
64 bytes from 52.18.119.20: icmp_seq=31 ttl=51 time=135.436 ms
```

Fom this we guessed that two successful pings meant the end of a morse code unit, one successful ping was the divider between the individual dots and dashes and five successful was the end of that word/phrase. Using that logic,  
