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

Fom this we guessed that two successful pings meant the end of a morse code unit, one successful ping was the divider between the individual dots and dashes and five successful was the end of that word/phrase. Using that logic, the above section decoded to `... --- ...` or `--- ... ---`. One of those represents `SOS` and the other `OSO`. Naturally we chose the `SOS` route which corresponded to 3 drops equating a dash (-) and a single drop represented a dot/dit (.)

After this determination. All that was left was scripting the process and finding the flag. We did this using a two step process, first converting our ping data to 1's and 0's (1's being successful pings and 0's being the dropped packets) and then converting this data to morse code. From there it was trivial to convert to ascii. I did not convert to binary (I received the data from a team member) but it could be generated from the ping results with similar code to the following:
```python
result = ""
with open('ping-data', 'r') as f:
  for x in f.readlines():
    if x.split(" ")[0] == "Request":
      result += "0"
    else:
      result += "1"
```
The binary result I was given is:
```
10101011000100010001101010111110001101010101101011010101111101011010101111100011010101011011111010100010110100010101101000110001000101101000100010100011010110001100010101010100011010110101011000101010101000110001011011010101000110110100010110001010101010001100011000100010001100010001000110001010101010001101000101011010001100011011000101010101000110101000101100010001000110100010110001010101010001101000110001010101010000100010101101000101100010001000110100010001011010001000101000100011111111111111111111111111
```
Note: This output generated from the attached ping results is slightly different. A few of the ping packets were unintentionally dropped but the above binary is correct.

My python code began by reading the dinary data in and then replacing the repetitve phrases with the corresponding meanings we dervived above. 
```python
f = open("drop.txt", "r")
s = f.readlines()[0]

morse = s.replace("11111", "\n").replace("0000", "- ").\
          replace("000", "-").replace("11", " ").replace("1", "").replace("0", ".")
```
  Note: We had an incident where one packet was unintentionally dropped which is why `replace("0000", "- ")` is included above.

I then did the translation from morse to ascii by using this dictionary I found online
```python
# Copied and updated from: http://code.activestate.com/recipes/578407-simple-morse-code-translator-in-python/
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.', '-': '-....-', '{': '.--.-', 
        '}': '.--.--'
        }
```
  Note: I had to add the curly braces and the hyphen.
  
The next step involved breaking up the morse by word and then by each morse unit and doing a dictionary lookup. There may be a better way to do the lookup process but this works.
```python
flag = ""

for word in morse.split("\n"):

    for unit in word.split(" "):
        for char in CODE:
            if CODE[char] == unit:
                flag += char
    # This is where the 5 11111's were
    flag += "\n"

# Hint said flag was lowercase
print flag.lower()

# RyanAiden
```

The decode data was:
```
sos
this
is
the
flag{it-is-never-too-late-for-a-drop}
```
