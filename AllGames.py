
import os, sys, random, time
def wordGuesser():
  def UpperOrNot():
      caps = raw_input("upper, lower or both?")
      if caps == "upper":
          p_c.extend(alphaUpper)
      elif caps == "lower":
          p_c.extend(alphaLower)
      elif caps == "both":
          p_c.extend(alphaUpper)
          p_c.extend(alphaLower)

  password = raw_input("What is the password (for testing)")
  maxChars = input("What is the maximum number of characters?")
  minChars = input("What is the minimum number of characters?")
  p_c = []

  alphaLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  alphaUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  numbers = ['0','1','2','3','4','5','6','7','8','9']
  done = False
  while done == False:
      ans1 = raw_input("alpha, alnum or numbers")
      if ans1 == "alpha":
           UpperOrNot()
      elif ans1 == "alnum":
          UpperOrNot()
          p_c.extend(numbers)
      elif ans1 == "numbers":
          p_c.extend(numbers)
      ect = raw_input("Does it contain spaces?    y/n")
      if ect == "y":
          p_c.append(" ")
      print p_c
      dono = raw_input ("Is this correct?")
      if dono == "y" or dono == "yes":
          done = True
  print "WAIT..."
  for i in range (3):
      time.sleep(0.3)
      print "LOADING..."

  solved = False
  l = len(p_c)
  if maxChars >= 1 and minChars <= 1:
      print "Checking 1 char"
      for a in range (0,l):
          word = p_c[a]
          if word == password:
              solved = True
              print "The password is: " + word
              sys.exit()
      print "Not 1 char"
  if maxChars >= 2 and minChars <= 2:
      print "Checking 2 chars"
      for b in range (0,l):
          for a in range (0,l):
              word = p_c[b]+p_c[a]
              if word == password:
                  solved = True
                  print "The password is: " + word
                  sys.exit()
  print "Not 2 chars"
  if maxChars >= 3 and minChars <= 3:
      print "Checking 3 chars"
      for c in range (0, l):
          for b in range (0,l):
              for a in range (0,l):
                  word = p_c[c]+p_c[b]+p_c[a]
                  if word == password:
                      solved = True
                      print "The password is: " + word
                      sys.exit()
      print "Not 3 chars"
  if maxChars >= 4 and minChars <= 4:
      print "Checking 4 chars"
      for d in range (0, l):
          for c in range (0, l):
              for b in range (0,l):
                  for a in range (0,l):
                      word = p_c[d]+p_c[c]+p_c[b]+p_c[a]
                      if word == password:
                          solved = True
                          print "The password is: " + word
                          sys.exit()
      print "Not 4 chars"
  if maxChars >= 5 and minChars <= 5:
      print "Checking 5 chars"
      for e in range (0, l):
          for d in range (0, l):
              for c in range (0, l):
                  for b in range (0,l):
                      for a in range (0,l):
                          word = p_c[e]+p_c[d]+p_c[c]+p_c[b]+p_c[a]
                          if word == password:
                              solved = True
                              print "The password is: " + word
                              sys.exit()
      print "Not 5 chars"
  if maxChars >= 6 and minChars <= 6:
      print "Checking 6 chars"
      for f in range(0, l):
          for e in range (0, l):
              for d in range (0, l):
                  for c in range (0, l):
                      for b in range (0,l):
                          for a in range (0,l):
                              word = p_c[f]+p_c[e]+p_c[d]+p_c[c]+p_c[b]+p_c[a]
                              if word == password:
                                  solved = True
                                  print "The password is: " + word
                                  sys.exit()
      print "Not 6 chars"
  if maxChars >= 7 and minChars <= 7:
      print "Checking 7 chars"
      for g in range(0,l):
          for f in range(0, l):
              for e in range (0, l):
                  for d in range (0, l):
                      for c in range (0, l):
                          for b in range (0,l):
                              for a in range (0,l):
                                  word = p_c[g]+p_c[f]+p_c[e]+p_c[d]+p_c[c]+p_c[b]+p_c[a]
                                  if word == password:
                                      solved = True
                                      print "The password is: " + word
                                      sys.exit()

      print "Not 7 chars"
  if solved == False:
      print
      print "FAILED"


def hangman():
  album = []
  star = []
  guessed = []
  playing = True
  attempts = 12
  caps = True
  os.system("clear")
  def GetAGuess():
      print
      print str(attempts) + " goes attempts left"
      Attempts()
      print
      print toPrint
      print
      inputo = raw_input("What letter would you like to guess?")         #E
      guess = inputo.lower()#e >>>Nope. #E
      inputo = inputo.upper()
      if guess == "exit":
          sys.exit()
      return guess, inputo

  def Attempts():
      if attempts == 1:
          print '''
  __________
  \| /     |
   |/      O
   |      /|\

   |       |
   |     _/ \_
   |\

   -----

  '''
      elif attempts == 2:
          print '''
  __________
  \| /     |
   |/      O
   |      /|\

   |       |
   |     _/
   |\

   -----

  '''
      elif attempts == 3:
          print '''
  __________
  \| /     |
   |/      O
   |      /|\

   |       |
   |
   |\

   -----

  '''
      elif attempts == 4:
          print '''
  __________
  \| /     |
   |/      O
   |      /|
   |
   |
   |\

   -----

  '''
      elif attempts == 5:
          print '''
  __________
  \| /     |
   |/      O
   |
   |
   |
   |\

   -----

  '''
      elif attempts == 6:
          print '''
  __________
  \| /     |
   |/
   |
   |
   |
   |\

   -----

  '''
      elif attempts == 7:
          print '''
  __________
  \| /
   |/
   |
   |
   |
   |\

   -----

  '''
      elif attempts == 8:
          print '''
  __________
  \|
   |
   |
   |
   |
   |\

   -----

  '''
      elif attempts == 9:
          print '''
  __________
   |
   |
   |
   |
   |
   |
   -----

  '''
      elif attempts == 10:
          print '''

   |
   |
   |
   |
   |
   |
   -----

  '''
      elif attempts == 11:
          print '''


   -----

  '''
      elif attempts == 12:
          print '''

  '''


  f = open("hangmanwords.txt","r")
  wordList = [line.strip() for line in f]
  f.close()
  randomPeopleAreConfusing = random.randint(0,len(wordList)-1)
  word1 = wordList[randomPeopleAreConfusing]
  word = word1

  for char in word:
      album.append(char)
  for char in word:
      if char == " ":
          star.append(" ")
      elif char == ".":
          star.append(".")
      elif char == ",":
          star.append(",")
      elif char == "?":
          star.append("?")
      elif char == "(":
          star.append("(")
      elif char == ")":
          star.append(")")
      elif char == "'":
          star.append("'")
      elif char == "!":
          star.append("!")
      elif char == ";":
          star.append(";")
      elif char == ":":
          star.append(":")
      elif char == "&":
          star.append("&")
      elif char == "/":
          star.append("/")
      elif char == "-":
          star.append("-")
      else:
          star.append("*")

  while playing == True: #loop for when you are having multiple goes
      toPrint = ""
      for i in range(len(star)):
          toPrint = toPrint+star[i]
      if "*" not in star:
          print "you won"
          playing == False
          break
      guess, inputo = GetAGuess()
      count = 0
      for i in word:
          if inputo == guess:
              caps = False
          elif inputo == guess.upper():
              caps = True
          if guess in album:
              indexGuess = album.index(guess)
              del star[indexGuess]
              star.insert(indexGuess,guess)
              del album[indexGuess]
              album.insert(indexGuess,"#")
              guessed.append(guess)
              if count == 0:
                  count = count+1
                  os.system("clear")
                  print guess+" is in the word."
              count = count+1
          if inputo in album:
              indexGuess = album.index(inputo)
              del star[indexGuess]
              star.insert(indexGuess,inputo)
              del album[indexGuess]
              album.insert(indexGuess,"#")
              guessed.append(guess)
              if count == 0:
                  count = count+1
                  os.system("clear")
                  print guess+" is in the word."
              count = count+1
          if guess in guessed:
              if count == 0:
                  os.system("clear")
                  print "Already guessed "+guess
                  count = count+1
          else:
              if count == 0:
                  count = count+1
                  os.system("clear")
                  print guess+" is not in the word."
                  attempts = attempts-1
                  toPrint = ""
                  guessed.append(guess)
          if attempts == 0:
              playing = False
              print '''
  __________
  \| /     |
   |/      O
   |      /|\

   |       |
   |     _/ \_
   |\

   -----

  '''
              print "Goes remaining = 0. You lost."
              sys.exit()
  toPrint = ""
  for i in range(len(star)):
      toPrint = toPrint+star[i]
  print toPrint
