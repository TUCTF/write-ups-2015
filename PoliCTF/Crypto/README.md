## Exorcise 50 points

## Challenge Overview
Very little is given for this challenge's description. We are told it's a simple `exorcise` and to grab the key from `exorcise.polictf.it 80`

## Challenge Solution
Admittingly this challenge took me far too long to figure out. When you connect to the service you are presented with the same initial string:
```
$ nc exorcise.polictf.it 80
2e0540472c37151c4e007f481c2a0110311204084f
```
And then the service waits for input. After you send it some data, it spits some hex encoded garbage at you. Given the name of the challenge we have to assume this is encrypted via xor.
I played around for a long while but eventually my idea was to send it a bunch of repeating data and just xor that with whatever is returned. Instead of writing code to do that though, I just used [xortool](https://github.com/hellman/xortool)

My session went as follows:
```
$ nc exorcise.polictf.it 80
2e0540472c37151c4e007f481c2a0110311204084f
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
2e0541574b6f445859436f01436f43006f43595d405c556f495f456f43585f455c546f585146556f435f5c4655546f6f59446f015e6f056f4355534d565c51574b6f445859436f01436f43006f43595d405c556f495f456f43585f455c546f585146556f435f5c4655546f6f59446f015e6f056f4355534d565c51574b6f445859436f01436f43006f43595d405c556f495f456f43585f455c546f585146556f435f5c4655546f6f59446f015e6f056f4355534d565c51574b6f445859436f01436f43006f43595d405c556f495f456f43585f455c546f585146556f435f5c4655546f6f59446f015e6f056f4355534d565c51574b6f445859436f01436f43006f43595d405c556f495f456f43585f455c546f585146556f435f5c4655546f6f59446f015e6f056f4355534d565c51574b6f445859436f01436f43006f43595d405c556f495f456f43585f455c546f585146556f435f5c4655546f6f59446f015e6f056f4355534d565c51574b6f445859436f01436f43006f43595d405c556f495f456f43585f455c546f585146556f435f5c4655546f6f59446f015e6f056f4355534d565c51574b6f445859436f01436f43006f43595d405c556f495f456f43585f455c546f585146556f435f5c58452d397f101b2a110f2d507f010002190f0206470f371d1b491e3a42003e14557f0a0618501c17301b0e17330a480e191e013b1141110a2b531b0413450f3a2647541045063a47281a16065d120404141e7f151a0c533544002b53517f111c03130445301f4f023a1a1a0b550e1d2b0d12
```
I copied the output into a file, exorcise, and then put xortool to the test. The only issue I found is that the length of the key seemed to be throwing off xortool. I ended up having to set xortool's max length manually.
My finial command simply told xortools the data was hex encoded (-x), the max length of a key can be 250 (-m 250) and the most frequent character should be `0` (30 in hex. -c 30). Xortool was easily able to find the key but sadly it took me longer than 5 seconds to solve this question.
```
$ xortool -x -m 250 -c 30 exorcise 
The most probable key lengths:
   1:   8.1%
   4:   9.5%
   6:   9.1%
   8:   8.7%
  10:   10.7%
  12:   9.8%
  15:   9.5%
  20:   11.2%
  30:   11.6%
  60:   11.7%
Key-length can be 4*n
1 possible key(s) of length 60:
flag{_this_1s_s0_simple_you_should_have_solved__it_1n_5_sec}
```
