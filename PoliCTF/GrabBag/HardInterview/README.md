#Hard Interview 50 points

##Overview
For this challenge we were only given a url and a port 'interview.polictf.it:80' 
Upon connecting to the url on port 80 we are presented with a banner than reads Department of Defense: Restricted Access Only. It looks a lot like a bash prompt thought with username being fish and computer name being sword.

##Challenge Solution
With everything we know up until this point, something should smell a little fishy (pun intended). For those of you who have seen it, there have been a lot of references to the movie Swordfish. Keep that in mind. At the moch bash prompt my first idea was to try and get an idea of what commands were accepted. Trying '?' didn't work but typing 'help' generates the following:
'''
fish@sword:~$ help
 A very hard interview: Codename Blow...Fish
Maybe you can help me with something...
DOD d-base, 128 bit encryption....What do you think?
Maybe slide in a Trojan horse hiding a worm...
I have been told that best "crackers" in the world can do it 60 minutes, unfortunately i need someone who can do it in 60 seconds... naturally with the right incentives ;) 
If you know what I mean, tell me how a real cracker accesses to a remote super protected server...

Possible commands:
	  hacker: Write code as a real hacker
	    help: Give informations about the program
	    hint: Gives a little hint
	    exit: Loser...bye Bye
	     ssh: A tiny ssh command
	    date: A very useful and innovative feature
'''
A boat load of more references to Swordfish. Great. The hint option looks promising, let's try that one.
'''
fish@sword:~$ hint
 usage:  ssh username@address
    username: THE username
    address: a not so easily reachable IP address
Very simple...isn't it?
'''
Hmm, I feel like this is how we get the flag! These hints are kind of vague so what I did was do a little bit of Googling and watched the Swordfish interview scene (sounds pretty fitting, right?). If you watch closely during the interview scene, Hugh Jackman types some ip addresses.. If you look close enough you'll see the ip addresses are not valid ips.. I made a list of these ips:
'''
312.5.125.233
291.12.112.323
232.12.10.362
213.225.312.5
125.323.12.30
'''
Next I made an assumption about the username. I figured it was either root or admin so I began trying to run the ssh command with those parameters. I think I just got lucky because the first attempt did it. If you run ''' ssh admin@312.5.125.233 ''' you are presented with the flag.
'''
fish@sword:~$ ssh admin@312.5.125.233
 flag{H4ll3_B3rry's_t0pl3ss_sc3n3_w4s_4ls0_n0t4bl3}
'''
