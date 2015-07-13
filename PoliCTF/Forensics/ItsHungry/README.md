## Its Hungry 100 points
```
PoliCTF 2015
Hidden Challenge – 100 points
Old McDonald had a farm. Old McDonald liked chiptune. He also needed to remind its daughter to take care about a zombie 
animal. But he wanted to do it discreetly, so he wrote this song. Can you find the message? (all lowercase, no spaces) 
N.B. flag is not in format flag{.+}
```

## Challenge Overview
This challenge was explained to be a hidden challenge and than the above, no other hints were given. 

## Challenge Solution
Chiptune is the genre describing the art of piecing together a song from old video game sounds. 
This led us to download the music file that played in the background on the main page of PoliCTF 2015: 

        [oldmcdonald.flac](oldmcdonald.flac?raw=true)

The first thing we tried was to open it in [Audacity](http://www.fosshub.com/Audacity.html/audacity-win-2.1.0.exe) and attempt a vocal removal. This yielded no results, so we decided
to take a look at the spectrogram of the audio. This showed three locations that seemed suspect. Zooming in on the first 
revealed text that said:

        THE FLAG IS… NOT HERE! KEEP LISTENING!

Well, that’s disappointing. So, we look at the second. The second turns out to be dots and dashes….. Morse Code! So, we 
go to an online morse code translator and enter what we were given and we get:

        YOUAREOVERCOMPLICATINGJUSTLISTEN

And again…. Disappointing. We zoom in on the last questionable location and get…. A troll face. So, the trick to this 
challenge is not in the spectrogram. The next thing we noticed were the notes being played in the beginning. We decided 
to cut them out using Audacity and export them to a wav file. 

From here, we were curious to discover what letter notes were being used. The problem is, there is no easy way of doing 
it. We did some research and it turns out there is a program called [MidiSheetMusic](http://sourceforge.net/projects/midisheetmusic/?source=typ_redirect) that takes in a midi file and outputs 
sheet music…. And letter notes. 

This prompted research into how to convert our wav file to a midi file. This led us to discover a program called [WaoN](http://kichiki.github.io/waon/index.html), a 
wave-to-notes transcriber. In order to convert our wav file to a midi file, we:

        1.	Opened Command Prompt
        2.	Navigated to the WaoN source directory
        3.	Executed the command waon –i {input file}.wav –o {output file}.midi

The program took about 3 seconds. Now that we had a midi to work with, we opened MidiSheetMusic and imported our midi 
into it. Once it was open we clicked on “Notes” on the toolbar, hovered over “Show Note Letters” and clicked on 
“Letters”. Voila! We now have letter notes from our audio selection.

The resulting letters were:

        FEEDDADEADDBBEEEEF

This, unfortunately, was not the flag. However, from it we were able to deduce that the flag was probably:

        FEEDADEADBEEF

Voila and Presto! We have the flag! 
