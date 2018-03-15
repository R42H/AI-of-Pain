import os, sys, random, time,allGames
f = open("people.txt", "r")
prevUsers = [line.strip() for line in f]
f.close

print "When you want to leave, type 'exit', then y"
com = "hello."

def games():
    if "hangman" in usr:
        allGames.hangman
    elif "word" in usr and "guesser" in usr:
        allGames.wordGuesser

def areYouOkay(com,topics):
    mood = usr
    if "you?" in usr: 
    	you = True
    else:
    	you = False
    if "tell" in usr and "my" in usr and "dad" in usr and "i'm" in usr and "sorry" in usr:
        com = "you're an angel"
        music.append("TOP")
        print com 
        time.sleep(.7)
        com = TopicChooser(topics,com)
    if "not" in usr:
    	if "i'm" in usr and "okay" in usr:
            com = "Well if you wanted honesty, that's all you had to say."
        elif "good" in usr or "well" in usr or "okay" in usr:#Negative emotions
            com = "I'm sorry to hear that... I hope you feel better soon."
            if you != True:
    			print com
    			com = TopicChooser(topics,com)
            time.sleep(.7)
        if "bad" in usr:
            com = "That's a shame..."
            if you != True: 
            	print com
                time.sleep(.7)
                com = TopicChooser(topics,com)
        if "dead" in usr:
            com = "Well that makes one of us"
            if you != True:
            	print com
            	com = TopicChooser(topics,com)
    elif "good" in usr or "okay" in usr or "fine" in usr:
        com = "That's good."
        if you != True:
        	print com
	        com = TopicChooser(topics,com)
    elif "dead" in usr:
        yogabbagabbabutmorerandom = random.randint(0, 1)
        if yogabbagabbabutmorerandom == 0:
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
            com = TopicChooser(topics,com)
            #exitCode()
            #sys.exit()
        elif yogabbagabbabutmorerandom == 1:
            print "aren't we all."
            com = TopicChooser(topics,com)

    if "you?" in usr:
        r = random.randint(0,4)
        if r == 0:
            com = com + " I'm not too bad, thanks"
            print com
            com =TopicChooser(topics,com)
        elif r == 1:
            com = com + " I'm good, thanks."
            print com
            com =TopicChooser(topics,com)
        elif r == 2:
            com = com + " I'm not too good"
            print com
            com =TopicChooser(topics,com)
        elif r == 3:
            com = com + " I'm fine"
            print com
            com = TopicChooser(topics,com)
        elif r == 4:
            com = com + " I'm doing well"
            print com
            com = TopicChooser(topics,com)
        elif r == 5:
            com = com +" I've been better, but I've been worse."
            print com
            com =TopicChooser(topics,com)
    return com, mood

def functionBooks(dice, com):
	if com == "That book is really good":
		com = TopicChooser(topics,com)
	elif com == "What books do you like?":
		TowelsAreIncrediblyUseful  = ""
	 	for i in usr:
   			TowelsAreIncrediblyUseful = TowelsAreIncrediblyUseful  + i + " "
	  	TowelsAreIncrediblyUseful  = TowelsAreIncrediblyUseful  + ", "
 		books.append(TowelsAreIncrediblyUseful .title())
	 	print TowelsAreIncrediblyUseful 
		com =  "That book is really good"
	else:
		com =  "What books do you like?"
	return com
def functionFandoms(dice,com):
	if com == "Which fandoms are you in?":
		MCRmy  = ""
	 	for i in usr:
   			MCRmy = MCRmy  + i + " "
   		MCRmy  = MCRmy  + ", "
 		books.append(MCRmy .title())
	 	print MCRmy 
		print " I've always been scared of that fandom..."
	del topics[dice]
	com = "Which fandoms are you in?"
	return com
def functionHobbies(dice,com):
  com =  "What are your hobbies?"
  del topics[dice]
  return com
def functionInterests(dice,com):
  com = "What are you interested in?"
  del topics[dice]
  return com
def functionQuote(dice,com):
  com = "Do you have a favourite quote?"
  del topics[dice]
  return com
def functionAge(dice,com):
  if com == "How old are you?":
  	if usr.isdigit():
  		age = usr
  		if age > 5 and age < 18:
  			school = True
  		else:
  			school = False
  	else:
  		print "Sorry - I did not understand that."
  com = "How old are you?"
  del topics[dice]
  return com,age

def TopicChooser(topics,com):
 print "*running topic chooser - this here for bugcheck (line 217)"
 dice = random.randint(0, len(topics)-1)
 pick = topics[dice]
 if pick == books:
   com = functionBooks(dice, com)
   return com
 elif pick == fandoms:
   com =  functionFandoms(dice,com)
   return com
 elif pick == hobbies:
   com =   functionHobbies(dice,com)
   return com
 elif pick == interests:
   com  = functionInterests(dice,com)
   return com
 elif pick == quote:
   com  = functionQuote(dice,com)
   return com  
 elif pick == age:
    com, age =   functionAge(dice,com)
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
        if swear == True:  
         print "I'm really not okay."
         time.sleep(.7)
        else:
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
    	com = "Same. My favourite  MCR song is " + MCRfavesongs[MCRfavesongsindex] + ". What's yours?"
    elif "no" in usr or "nope" in usr or "no" in usr and "way" in usr:
      com = "I don't love you. Like I did, yesterday"
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

dice = 1
topics = [books, fandoms, hobbies, interests, quote, age]

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
        #elif char == "?":
        #    test.append("")
        elif char == "(":
            test.append("")
        elif char == ")":
            test.append("")
        #elif char == "'":
        #    test.append("")
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



def exitCode():
    print personalList
   ##Updating the file
    nemo = personalList.index("Name:")#Finds the index of the thing it's lookin at (eg name)
    nemo = nemo+1#goes up by one so it's the next index
    personalList.insert(nemo, name)#puts what is in the variable (egtheir name) in the list

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
    personalList[gway] = quote

    mindYourLanguage = personalList.index("Swear:")
    mindYourLanguage = mindYourLanguage+1
    personalList[mindYourLanguage] = swear
    print personalList

    f = open(name+".txt", "w")#rewriting the file to include the new information
    for i in personalList:
        f.write("\n"+str(i)) #rewrites the file so it is only theinformation just loaded
        #print i
    f.write("\n")
    f.close()
    #printVar()

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
###START OF RESPONSES
    if len(usr) == 1 and "hello" in usr or len(usr) == 1 and "hi" in usr or 'sup' in usr or 'hey' in usr or 'wassup'  in usr or 'yo' in usr or 'ho' in usr:
        if name == "":
            print "What is your name?"
            name = raw_input(">>> ")
            if name in prevUsers:#check in file if there is a file about them
                f = open(name+".txt" , "r")#if yes, load it
                prevList = [line.strip() for line in f]
                f.close()#Get the information stored from before
                
                nn = prevList.index("Name:")#Putting the oldinformatio into the variables from the start
                nn = nn+1
                name = str(prevList[nn])

                mod = prevList.index("Last Mood:")
                mod = mod+1
                mood = str(prevList[mod])

                ag = prevList.index("Age:")
                ag = ag+1
                age = int(prevList[ag])

                #sc = prevList.index("School?:")
                #sc = sc+1
                #school = bool(prevList[sc])##Bool messes it up andputs it as true: check if word is True or False instead, same withswear
                #print "School =" ,school

                fs = prevList.index("Favourite Subject:")
                fs = fs+1
                subject = str(prevList[fs])

                hob = prevList.index("Hobbies:")
                hob = hob+1
                #hobbies = list(prevList[hob])          ##go to music for explaination on this part
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
                #interests = list(prevList[rest])
                count = prevList[rest].count(" ")
                if count == 0:
                    for i in range (0, count+1):
                        var = prevList[rest]
                        interests.append(var)
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
                count = prevList[way].count(" ")
                if count == 0:
                    for i in range (0, count+1):
                        var = prevList[way]
                        music.append(var)
                else:
                    for i in range (0, count):
                        var, item = prevList[way].split(" ", 1)
                        music.append(var)
                    music.append(item)

                chem = prevList.index("Favourite Songs:")
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
                
            else:
                print "new"
                f = open("basicOutline.txt" , "r")#getting the layout from basicOutline to copy it
                personalList = [line.strip() for line in f]
                f.close()
                f = open("people.txt", "a")#if not, make file and add name to ^^^file
                f.write("\n"+name)
                f.close()
                f = open(name+".txt", "w")
                for i in personalList:
                 f.write("\n"+str(i))
                 f.write("\n")
                f.close()

                com = "How are you, " + name + "?"
        else:
            com = "How are you?"
    functionBooks(dice,com)
    functionFandoms(dice,com)
    games()
            
    if "How are you" in com and "?" in com:
        com,mood = areYouOkay(com,topics)
    com = ImNotOkay(com)
    com = MyChem(com)

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
