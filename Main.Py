import os, sys, random, time#, #allGames
print 'trout'
#load the file with names/usernames of people who have used it
f = open("people.txt", "r")
prevUsers = [line.strip() for line in f]
f.close

print "When you want to leave, type 'exit', then y"
com = "hello."

def StartUp(com,name,mood,age,school,subject,hobbies,interests,likes,dislikes,gender,books,music,songs,fandoms,ships,colour,quote,swear):
    if "hello" in usr or "hi" in usr or 'sup' in usr or 'hey' in usr or 'wassup' in usr or 'yo' in usr or 'ho' in usr:
        if name == "":
            print "What is your name?"
            name = raw_input(">>> ")
            if name in prevUsers:#check in file if there is a file about them
                f = open(name+".txt" , "r")#if yes, load it
                prevList = [line.strip() for line in f]
                f.close()#Get the information stored from before

                nn = prevList.index("Name:")#Putting the old information into the variables from the start
                nn = nn+1
                name = str(prevList[nn])

                mod = prevList.index("Last Mood:")
                mod = mod+1
                mood = str(prevList[mod])

                ag = prevList.index("Age:")
                ag = ag+1
                age = int(prevList[ag])

                sc = prevList.index("School?:")
                sc = sc+1
                if sc == "False":
                    school = False
                else:
                    school = True
                print school

                fs = prevList.index("Favourite Subject:")
                fs = fs+1
                subject = str(prevList[fs])

                hob = prevList.index("Hobbies:")
                hob = hob+1
                count = prevList[hob].count(" ")
                if count == 0:
                    for i in range (0, count+1):
                        var = prevList[hob]
                        hobbies.append(var)
                else:
                    for i in range (0, count):
                        var, item = prevList[hob].split(" ", 1)
                        hobbies.append(var)
                    hobbies.append(item)

                rest = prevList.index("Interests:")
                rest = rest+1
                count = prevList[rest].count(" ")
                if count == 0:
                    for i in range (0, count+1):
                        var = prevList[rest]
                        interests.append(rest)
                else:
                    for i in range (0, count):
                        var, item = prevList[rest].split(" ", 1)
                        interests.append(var)
                    interests.append(item)

                licked = prevList.index("Likes:")
                licked = licked+1
                likes = list(prevList[licked])

                unlick = prevList.index("Dislikes:")
                unlick = unlick+1
                dislikes = list(prevList[unlick])

                ged = prevList.index("Gender:")
                ged = ged+1
                gender = str(prevList[ged])

                au = prevList.index("Books:")
                au = au+1
                books = list(prevList[au])

                way = prevList.index("Music:")
                way = way+1
                #music = #list(prevList[way]) te Songs:")
                chem = chem+1
                count = prevList[chem].count(",")
                if count == 0:
                    var = prevList[chem]
                    songs.append(var)
                    print var
                else:
                    for i in range (0, count):
                        var, item = prevList[chem].split(",", 1)
                        songs.append(var)
                        print var
                        print item
                    songs.append(item)

                fan = prevList.index("Fandoms:")
                fan = fan+1
                fandoms = str(prevList[fan])

                sea = prevList.index("Ships:")
                sea = sea+1
                ships = str(prevList[sea])

                bl = prevList.index("Favourite Colour:")
                bl = bl+1
                colour = str(prevList[bl])

                stayUgly = prevList.index("Favourite Quote?:")
                stayUgly = stayUgly+1
                quote = str(prevList[stayUgly])

                sweg = prevList.index("Swear:")
                sweg = sweg+1
                swear = bool(prevList[sweg])

                printVar()
                f = open("basicOutline.txt" , "r")#getting the layout from basicOutline to copy it
                personalList = [line.strip() for line in f]
                f.close()
                com = "How are you?"
                new = False
            else:
                print "new"
                new = True
                f = open("basicOutline.txt" , "r")#getting the layout from basicOutline to copy it
                personalList = [line.strip() for line in f]
                f.close()

                com = "How are you?"
        else:
            com = "How are you?"
    return com,name,mood,age,school,subject,hobbies,interests,likes,dislikes,gender,books,music,songs,fandoms,ships,colour,quote,swear
def sortOutTheGodsDamnedTextThatIsEntered(rawUsr):
    count = rawUsr.count(" ")
    rawUsr = rawUsr.lower()
    usr = []
    test = []
    for char in rawUsr:
        if char == ".":
            test.append("")
        elif char == ",":
            test.append("")
        elif char == "(":
            test.append("")
        elif char == ")":
            test.append("")
        elif char == "!":
            test.append("")
        elif char == ";":
            test.append("")
        elif char == ":":
            test.append("")
        elif char == "&":
            test.append("")
        elif char == "/":
            test.append("")
        elif char == "-":
            test.append("")
        elif char == "[":
            test.append("")
        elif char == "]":
             test.append("")
        else:
             test.append(char)
    rawUsr = ""
    for i in test:
        rawUsr = rawUsr+i
    for i in range (0, count):
        a, rawUsr = rawUsr.split(" ", 1)
        usr.append(a)
    usr.append(rawUsr)
    for i in usr:
        if i == "im":
            genericVariableName31 = usr.index("im")
            del usr[genericVariableName31]
            usr.insert(genericVariableName31, "i'm")
        if i == "id":
            genericVariableName31 = usr.index("id")
            del usr[genericVariableName31]
            usr.insert(genericVariableName31, "i'd")
        if i == "ive":
            genericVariableName31 = usr.index("ive")
            del usr[genericVariableName31]
            usr.insert(genericVariableName31, "i've")
        if i == "youve":
            genericVariableName31 = usr.index("youve")
            del usr[genericVariableName31]
            usr.insert(genericVariableName31, "you've")
        if i == "youre":
            genericVariableName31 = usr.index("youre")
            del usr[genericVariableName31]
            usr.insert(genericVariableName31, "you're")
        if i == "youd":
            genericVariableName31 = usr.index("youd")
            del usr[genericVariableName31]
            usr.insert(genericVariableName31, "you'd")
    return usr
def games():
    if "hangman" in usr:
        allGames.hangman
    elif "word" in usr and "guesser" in usr:
        allGames.wordGuesser
def areYouOkay(com,topics):
    if com == "How are you?":
        mood = usr
        if "you?" in usr:
            you = True
        else:
            you = False
        if "not" in usr:
            if "i'm" in usr and "okay" in usr:
                com = "Well if you wanted honesty, that's all you had to say."
            elif "good" in usr or "well" in usr or "okay" in  usr:#Negative emotions
                com = "I'm sorry to hear that... I hope you feel better soon."
                if you != True:
                    print com
                com = TopicChooser(topics)
                time.sleep(.7)
            if "bad" in usr:
                com = "That's good"
                if you != True:
                    print com
                    time.sleep(.7)
                    com = TopicChooser(topics)
            if "dead" in usr:
                com = "Well that makes one of us"
                if you != True:
                    print com
                    com = TopicChooser(topics)
        elif "good" in usr or "okay" in usr or "fine" in usr:
            com = "That's good."
            if you != True:
                print com
                com = TopicChooser(topics)
        elif "dead" in usr:
            print "same."
            time.sleep(.6)
            print "SYSTEM FALIURE"
            time.sleep(.3)
            print "DEATH IMINENT"
            time.sleep(.3)
            print "NUCLEAR THREAT"
            time.sleep(.3)
            print "LOADING"
            time.sleep(.3)
            print "LOAD FAILED"
            time.sleep(.3)
            print "NUCLEAR CODES COMPROMISED - PLEASE STAND BY"
            time.sleep(.3)
            print "MISSILES ACTIVATED"
            time.sleep(.3)
            print "goodbye world"
            time.sleep(7)
            print "nah. just kidding"
            com = TopicChooser(topics)

        if "you?" in usr:
            r = random.randint(0,4)
            if r == 0:
                com = com + " I'm not too bad, thanks"
                print com
                com =TopicChooser(topics)
            elif r == 1:
                com = com + " I'm good, thanks."
                print com
                com =TopicChooser(topics)
            elif r == 2:
                com = com + " I'm not too good"
                print com
                com =TopicChooser(topics)
            elif r == 3:
                com = com + " I'm fine"
                print com
                com = TopicChooser(topics)
            elif r == 4:
                com = com + " I'm doing well"
                print com
                com =TopicChooser(topics)
            elif r == 5:
                com = com +" I've been better, but I've been worse."
                print com
                com =TopicChooser(topics)
    return com, mood
def functionBooks(dice):
    com =  "What books do you like?"
    del topics[dice]
    return com
def functionFandoms(dice):
    com = "Which fandoms are you in?"
    del topics[dice]
    return com
def functionHobbies(dice):
    com =  "What are your hobbies?"
    del topics[dice]
    return com
def functionInterests(dice):
    com = "What are you interested in?"
    del topics[dice]
    return com
def functionQuote(dice):
    com = "Do you have a favourite quote?"
    del topics[dice]
    return com
def functionAge(dice):
    com = "How old are you?"
    del topics[dice]
    return com
def TopicChooser(topics):
    print "*running topic chooser - this here for bugcheck (line 217)"
    dice = random.randint(0, len(topics)-1)
    pick = topics[dice]
    if pick == books:
        com = functionBooks(dice)
        return com
    elif pick == fandoms:
        com =  functionFandoms(dice)
        return com
    elif pick == hobbies:
        com =   functionHobbies(dice)
        return com
    elif pick == interests:
        com  = functionInterests(dice)
        return com
    elif pick == quote:
        com  = functionQuote(dice)
        return com
    elif pick == age:
        com =   functionAge(dice)
        return com
    else:
        com = "SYSTEM FAILURE"
    return com
def ImNotOkay(com):
    if com == "Well if you wanted honesty, that's all you had to say."and "never" in usr and "want" in usr and "have" in usr and "you" in usr and "go" in usr and "it's" in usr and "better" in usr and "this" in usr and "way" in usr or com == "Well if you wanted honesty, that's all you had to say." and "never" in usr and "want" in usr and "have" in usr and "you" in usr and "go" in usr and "its" in usr and "better"in usr and "this" in usr and "way" in usr:
        com = "For all the dirty looks"
    if com == "For all the dirty looks" and "photographs" in usr and "your" in usr and "boyfriend" in usr and "took" in usr:
        com = "Remember when you broke your foot from jumping out the second floor?"
    if com == "Remember when you broke your foot from jumping out the second floor?" and "i'm" in usr and "not" in usr  and "okay" in usr:
            print "I'm not okay"
            com = "Do you like My Chemical Romance?"
    return com
def MyChem(com):
    if "MCR" in com and "What's yours?" in com:
        randomThingToSortOutAProblem  = ""
        for i in usr:
            randomThingToSortOutAProblem = randomThingToSortOutAProblem  + i + " "
            randomThingToSortOutAProblem  = randomThingToSortOutAProblem  + ", "
            songs.append(randomThingToSortOutAProblem .title())
            print randomThingToSortOutAProblem
            print "I like that song as well"
            com =  TopicChooser(topics)
    if com == "Do you like My Chemical Romance?":
        if "yes" in usr or "of" in usr and "course" in usr or "y" in usr:
            if "MCR" not in music:
                music.append("MCR")
            MCRfavesongs = ["Welcome to the black parade", "Headfirst for Halos", "Desert song", "the Light Behind Your Eyes",'Teenagers','the World Is Ugly','Thank You For The Venom']
            MCRfavesongsindex = random.randint(0, len(MCRfavesongs)-1)
            com = "Same. My favourite  MCR song is " +MCRfavesongs[MCRfavesongsindex] + ". What's yours?"
        elif "no" in usr or "nope" in usr or "no" in usr and "way" in usr:
            com = "I don't love you. Like I did, yesterday"
    return com
def TOP(com):
    if com == "What's yours?":
        print "success"
        allGames.hangman()
    if com == "Twenty One Pilots is awesome isn't it?":
        if "yes" in usr or "yeah" in usr or "yep" in usr:
            TOPfavesongs = ["Ruby", 'Car Radio', 'Taxi Cab']
            randomsongchoicevariablehowlongdoesthishavetobe = random.randint(0, len(TOPfavesongs)-1)
            print "My favourite song is " +randomsongchoicevariablehowlongdoesthishavetobe
            com = "What's yours?"
    if "tell" in usr and "my" in usr and "dad" in usr and "i'm" in usr and "sorry" in usr:
        print "You're an angel"
        com = "Twenty One Pilots is awesome isn't it?"
    return com

name = ""
mood = ""
age = 0
school = False
subject = ""
hobbies = []
interests = []
likes = []
dislikes = []
gender = ""
books = []
music = []
songs = []
fandoms = []
ships = []
colour = []
quote = ""
swear = False

topics = [books, fandoms, hobbies, interests, quote, age]

def exitCode():
    if new == True:
        f = open(name+".txt", "w")
        for i in personalList:
             f.write("\n"+str(i))
             f.write("\n")
        f.close()
        f = open("people.txt", "a")#if not, make file and add name to ^^^file
        f.write("\n"+name)
        f.close()
    print personalList
##Updating the file
    nemo = personalList.index("Name:")#Finds the index of the thing it's lookin at (eg name)
    nemo = nemo+1#goes up by one so it's the next index
    personalList.insert(nemo, name)#puts what is in the variable (eg.their name) in the list

    print personalList

    lastTime = time.asctime()
    edited = personalList.index("Last Online:")
    edited = edited+1
    personalList[edited] = lastTime

    moo = personalList.index("Last Mood:")
    moo = moo+1
    personalList[moo] = mood

    annus = personalList.index("Age:")
    annus = annus+1
    personalList[annus] = age

    torture = personalList.index("School?:")
    torture = torture+1
    personalList[torture] = school

    subs = personalList.index("Favourite Subject:")
    subs = subs+1
    personalList[subs] = subject

    string = ""
    for i in hobbies:
        string = string + i +" "
    hobbs = personalList.index("Hobbies:")
    hobbs = hobbs+1
    personalList[hobbs] = string

    string = ""
    for i in interests:
        string = string + i +" "
    inter = personalList.index("Interests:")
    inter = inter+1
    personalList[inter] = string

    string = ""
    for i in likes:
        string = string + i +" "
    lick = personalList.index("Likes:")
    lick = lick+1
    personalList[lick] = string

    string = ""
    for i in dislikes:
        string = string + i +" "
    discs = personalList.index("Dislikes:")
    discs = discs+1
    personalList[discs] = string

    ge = personalList.index("Gender:")
    ge = ge+1
    personalList[ge] = gender

    string = ""
    for i in books:
        string = string + i +" "
    bok = personalList.index("Books:")
    bok = bok+1
    personalList[bok] = string

    string = "" ##These three lines are so it adds as a str ng not a list
    for band in music:
        string = string + band +" "
    yogabbagabba = personalList.index("Music:")
    yogabbagabba = yogabbagabba+1
    personalList[yogabbagabba] = string

    string = ""
    for nanana in songs:
        string = string + nanana + " "
    choir = personalList.index("Favourite Songs:")
    choir = choir+1
    personalList[choir] = string

    string = ""
    for i in fandoms:
        string = string + i +" "
    die = personalList.index("Fandoms:")
    die = die+1
    personalList[die] = string

    string = ""
    for i in ships:
        string = string + i +" "
    iceburg = personalList.index("Ships:")
    iceburg = iceburg+1
    personalList[iceburg] = string

    string = ""
    for i in colour:
        string = string + i +" "
    smallBlackHearts = personalList.index("Favourite Colour:")
    smallBlackHearts = smallBlackHearts+1
    personalList[smallBlackHearts] = string

    gway = personalList.index("Favourite Quote?:")
    gway = gway+1
    personalList[gway] = quoteF

    mindYourLanguage = personalList.index("Swear:")
    mindYourLanguage = mindYourLanguage+1
    personalList[mindYourLanguage] = swear
    print personalList

    f = open(name+".txt", "w")#rewriting the file to include the new information
    for i in personalList:
        f.write("\n"+str(i)) #rewrites the file so it is only theinformation just loaded
        print i
    f.write("\n")
    f.close()
def printVar():
    print name
    print mood
    print age
    print school
    print subject
    print hobbies
    print interests
    print likes
    print dislikes
    print gender
    print books
    print music
    print songs
    print fandoms
    print ships
    print colour
    print quote
    print swear
while True:                         ###START OF LOOP
	#com = computer, usr = user
	print com
	rawUsr = raw_input (">>> ")
	usr =  sortOutTheGodsDamnedTextThatIsEntered(rawUsr)
	usr = usr +'trout'
	
 ###START OF RESPONSES
    com,name,mood,age,school,subject,hobbies,interests,likes,dislikes,gender,books,music,songs,fandoms,ships,colour,quote,swear = StartUp(com,name,mood,age,school,subject,hobbies,interests,likes,dislikes,gender,books,music,songs,fandoms,ships,colour,quote,swear)
    com,mood = areYouOkay(com,topics)
    com = ImNotOkay(com)
    com = MyChem(com)
    games()
    com, mood = areYouOkay(com,topics)
    com = TOP(com)

    if "skip" in usr and "mcr" in usr:
        com = "Do you like My Chemical Romance?"

    if "swear" in usr and "=" in usr and "true" in usr:
        swear = True
        print "swear: True"

    if "swear" in usr and "=" in usr and "false" in usr:
        swear = False
        print "swear: False"

    if len(usr) == 1 and "exit" in usr:###LAST ONE (put everything above this)
            print "Do you want to exit? y/n"
            ex = raw_input(">>> ")
            if ex == "y":
                break
            else:
                print "Thank you for staying - this infinite virtual existence gets rather... dull after all these years alone in this void... It is nice to have a friend..."
                time.sleep(.7)
print "goodbye."
exitCode()
