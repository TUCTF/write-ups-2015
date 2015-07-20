## John The Dropper 100 Points

## Challenge Overview
The description for this challenge was: 
```
I am afraid John is in trouble. I feel he needs help but I can't find any message from him.
dropper.polictf.it
About John The Dropper: John does not need a port to communicate
```

This challenge stumped us for quite some time. After trying a couple of things, one of us noticed certain pings were being dropped. The pattern of dropped packets did not change so we knew this was part of the problem. We ended up pinging `dropper.polictf.it` about 500 times and saw after ~400 no more ping packets were dropped. This is were we got stuck for a good bit, turns out sleep helps a lot because come morning we got it. The statement `I am afraid John is in trouble. I feel he needs help but I can't find any message from him.` really had me thinking it was morse code. After a lot of staring, a lot of caffeine, and a pure whim, we finally made the seemingly random pattern spell out the begginning of a message. At that point we knew it was just a matter of scripting it. 


## Challenge Solution
TO-DO
