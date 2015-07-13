PoliCTF 2015
JOHN IN THE MIDDLE
100 Points - SOLVED
Can John hijack your surfin'? :) 
GPG key: GhairfAvvewvukDetolicDer-OcNayd#
Download


The task “JOHN IN THE MIDDLE” was a forensics challenge. As was the case with many of the other challenges, you were 
required to download the gpg file, decrypt it with the given gpg key, append the file type .tar.gz and untar it. Once 
this is accomplished, you are left with a pcap file which makes sense with the above clue: 

                                        “Can John hijack your surfin'? :)”.

The first step with a pcap file is to load it into [Wireshark](https://www.wireshark.org/download.html). If you have any experience with CTFs you are familiar 
with Wireshark, but on the off chance you are completely new to the scene, Wireshark is primarily a network traffic 
analyzer. It allows you to either analyze traffic in real time or to open saved packet capture files (pcap files). 
There are rare occasions where pcap files contain information other than network traffic such as mouse movements, but 
we won’t go into that right now.

So, we load Wireshark and open the [john-in-the-middle.pcap](john-in-the-middle.pcap) file. As expected, we are greeted with network traffic. 
Thankfully, this pcap is not very large. In most cases, pcap files used in challenges will be extremely large.

The first step I always perform is to do a search for the word “flag” just in case the flag is in the traffic in plain 
text. It very rarely is, but I would sure feel stupid for wasting a ton of time if it was. The search for “flag” returns 
nothing so I go to step two: Scroll through the packets and look for reference to files or anything else that pops out 
at me. After a couple of seconds of scrolling, I notice that there are indeed files being passed in the traffic: I see 
at least one .png. 

At this point, if you have found files in the pcap, it is generally beneficial to export them. This is really easy to do 
since Wireshark does it all for you. 

        1.	Click “File”
        2.	Scroll over “Export Objects”
        3.	Click on “HTTP”
        4.	Click “Save All”
        5.	Choose location to save them (type a folder name)
        6.	Click “OK”
        
Now that the files have been exported, navigate to the location you exported them to and take a look at them. The first 
thing to look for is text files or files with the names “flag”, “secret”, etc. The exported files did not contain any of 
those things, but there were quite a few pictures. 

My next thought was that steganography is used quite a bit in CTFs, so let us check out the pictures. For the uninitiated, 
steganography is the act or art of hiding data, text, or other files inside pictures. There are many ways of doing this, 
like hiding it in the hex of the picture, or performing some editing magic to hide text directly in the picture. In order 
to check for the latter of the two, we regularly use [StegSolve](https://www.wechall.net/de/forum/show/thread/527/Stegsolve_1.3/). 

To open StegSolve, I use terminal:

        1.	Navigate to StegSolve’s location
        2.	Type java –jar StegSolve.jar
        3.	Use StegSolve to open the target file

I chose to look at logo.png first since it is rather common to find logo’s in challenges. Once opened, I scrolled to the 
right and within seconds I noticed some hidden text in the picture. I continued to scroll right until I hit the random 
color maps which revealed the flag brilliantly:

                                                Flag{J0hn_th3_Sn1ff3r}

