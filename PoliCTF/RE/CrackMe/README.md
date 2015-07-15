## Crack Me If You Can 100 Points

## Challenge Overview 
This challenge starts you off with the usual taunt: `John bets nobody can find the passphrase to login!`. 
After you decrypt and unpack the tar file you are presented with an app that is aptly named `crack_me_if_you_can.apk`. 

## Challenge Solution
To begin this challenge, I immediately looked online for an android decompiler. I believe I used 
[this](http://www.decompileandroid.com/) one. This presented me with some pseudo source code for the app. In the 
folder `src/it/polictf2015/` you will find four files: `LoginActivity.java`, `a.java`, `b.java`, and `c.java`. 

Inside LoginActivity.java you will find a line of code that looks like such:
```java
if (a(getApplicationContext(), 2) || a(getApplicationContext(), "flagging{It_cannot_be_easier_than_this}") || a(getApplicationContext(), false) || a(getApplicationContext(), 2.7799999999999998D))
```
I hate to say it but it really can get easier than that because that is not the flag. If you poke around in that file 
long enough you'll come across this method:
```java
    private boolean a(String s)
    {
        if (s.equals(c.a(it.polictf2015.b.a(it.polictf2015.b.b(it.polictf2015.b.c(it.polictf2015.b.d(it.polictf2015.b.g(it.polictf2015.b.h(it.polictf2015.b.e(it.polictf2015.b.f(it.polictf2015.b.i(c.c(c.b(c.d(getString(0x7f0c0038))))))))))))))))
        {
            Toast.makeText(getApplicationContext(), getString(0x7f0c003c), 1).show();
            return true;
        } else
        {
            return false;
        }
    }
```
Given the obscurity involved I would say this has something to do with the solution. Looking at the method 
closely you'll see it is simply performing certain transformations on a string. The first thing to do 
with this sort of challenge is to now write a program to do those same transformations. From here I went and copied every 
method mentioned in the above ```if``` statement and added it to my own java program. 
Once finished I ended up with this: (please excuse my wonderful naming scheme)
```java
class keygen {
    public static void main(String[] args) {
        
        System.out.println(cDota(bDota(bDotb(bDotc(bDotd(bDotg(bDoth(bDote(bDotf(bDoti(cDotc(cDotb(cDotd(getString(0x7f0c0038)))))))))))))));
        
    }
    
    public static String cDotd(String s)
    {
        return s.replace("spdgj", "yb%e");
    }
    public static String cDotb(String s)
    {
        return s.replace("aat", "his");
    }
    public static String cDotc(String s)
    {
        return s.replace("buga", "Goo");
    }
    public static String cDota(String s)
    {
        return s.replace("aa", "ca");
    }



    public static String bDoti(String s)
    {
        return s.replace("=", "_");
    }
    public static String bDotf(String s)
    {
        return s.replaceFirst("\\}", "");
    }
    public static String bDote(String s)
    {
        return s.replaceFirst("\\{", "");
    }
    public static String bDoth(String s)
    {
        return s.replaceFirst("R", "f");
    }
    public static String bDotg(String s)
    {
        return s.replaceFirst("c", "f");
    }
    public static String bDotd(String s)
    {
        return s.replace("]", "");
    }
    public static String bDotc(String s)
    {
        return s.replace("[", "");
    }
    public static String bDotb(String s)
    {
        return s.replace("%", "");
    }
    public static String bDota(String s)
    {
        return s.replace("c", "a");
    }
}
```
Stepping back we can see we that the original program is performing certain transformations on 
a string and we have created our own java program that will perform those same transformations. All that's 
missing is the string needed to perform the transformations on. This is were I initially got stuck and moved 
on to solving a different problem. Another team member (darkstructures) later told me he used a different 
decompiler and it included the needed string either in the AndroidManifest.xml or the LoginActivity.java file 
and was able to solve the problem with that information. 
After looking back on it, I could have just done a string dump on the app file and looked for strings containing characters 
seen in some of the transformations. Let's look in the app for strings containing `spdgj` from the method cDotd. 
```bash
$ strings crack-me-if-you-can.apk | grep spdgj
ee[[c%l][c{g}[%{%Mc%spdgj=]T%aat%=O%bRu%sc]c%ti[o%n=Wcs%=No[t=T][hct%=buga[d=As%=W]e=T%ho[u%[%g]h%t[%}%
```
Now doesn't that look interesting? Let's plug it into our script and see what it spits out. If you simply change 
the `getString(0x7f0c0038)` in the above script to 
`ee[[c%l][c{g}[%{%Mc%spdgj=]T%aat%=O%bRu%sc]c%ti[o%n=Wcs%=No[t=T][hct%=buga[d=As%=W]e=T%ho[u%[%g]h%t[%}%` and run it, 
you get `eeflag{Maybe_This_Obfuscation_Was_Not_That_Good_As_We_Thought}` as the output. Sure enough the flag is 
`flag{Maybe_This_Obfuscation_Was_Not_That_Good_As_We_Thought}`
