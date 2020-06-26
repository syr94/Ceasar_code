class CeasarCode:                                           # Class of word that you want to code. Coding only letters
  def __init__(self, text):                                 # Initializing new object of class CeasarCode
    self.text = text                                        # initializing with the word you want to code
    self.key = 0                                            # initialize a zero code to avoid errors that could be
  
  def setKey(self):                                         # method of class to set user key
    right_number = True                                     # bool var for while to avoid wrong keys
    while(right_number):                                    # starting iterations while right key is not be inputed
      try:                                                  # try to avoid wrong keys
        self.key = int(input("Please input your key\n"))    # inputing a word that user want to choose
        right_number = False                                # if key is number than we can stop while
      except:                                               # if key was not number than alert about that user 
        print("please input integer number")                # by this
    

  def code(self):                                           # coding method for Ceasar Class word
    new_word = []                                           # creating new var for coded word
    new_letter = ''                                         # creating new var for coded letter
    for i in self.text:                                     # letter by letter coding text
      if ord(i)>=65 and ord(i)<=90:                         # coding for Uppercase ASCII
        new_letter = chr((((ord(i)-65) + self.key)%26)+ 65) # normilize ord int of UpperCase, after that mod of len alphabet (y = x + k(mod N)) N - power of alphabet
        new_word.append(new_letter)                         # appending coded letter
      elif ord(i)>=97 and ord(i)<=122:                      # coding for lowercase ASCII
        new_letter = chr((((ord(i)-97) + self.key)%26)+ 97) # normilize ord int of LowerCase, after that mod of alphabet
        new_word.append(new_letter)                         # appending coded letter
      else:                                                 # for symbols and numbers (not letters)
        new_word.append(i)                                  # appending symbols and numbers
    self.text = ''.join(new_word)                           # returning new decoded text as string type

  def decode(self):                                         # decoding method for Ceasar Class word
    new_word = []                                           # creating new var for decoded word
    new_letter = ''                                         # creating new var for decoded letter
    for i in self.text:                                     # letter by letter decoding text
      if ord(i)>=65 and ord(i)<=90:                         # decoding for Uppercase ASCII
        new_letter = chr((((ord(i)-65) - self.key)%26)+ 65) # normilize ord int of UpperCase, after that mod of len alphabet (y = x + k(mod N)) N - power of alphabet
        new_word.append(new_letter)                         # appending decoded letter
      elif ord(i)>=97 and ord(i)<=122:                      # decoding for lowercase ASCII
        new_letter = chr((((ord(i)-97) - self.key)%26)+ 97) # normilize ord int of LowerCase, after that mod of alphabet
        new_word.append(new_letter)                         # appending decoded letter
      else:                                                 # for symbols and numbers (not letters)
        new_word.append(i)                                  # appending symbols and numbers
    self.text = ''.join(new_word)                           # returning new decoded text as string type


finish = True                                               # for while to finish programm only when user want
while(finish):                                              # starting this while_1
  user_word = input("Please input a word\n")                # inputing a word that you want to code
  word = CeasarCode(user_word)                              # Initializing class for coding this word
  choice = input("do you want to code or decode your word? code/decode\n") # Asking to what we must do?
  if choice == "code":                                      # if choice is code, than activating code method
    word.setKey()                                           # setting key method
    word.code()                                             # calling code method
  elif choice =='decode':                                   # if choice is decode, than activating decode method
    word.setKey()                                           # setting key method
    word.decode()                                           # calling decode method
  else:
    print("You inputed wrong choice")                       # if choice is not code or decode reasking
  print("Your text now =\"",word.text,"\"")                 # printing result
  end_programm = True                                       # to pause programm and asking user
  while(end_programm):                                      # does he want to start another iteration while_2
    choice = input("Do you want to end coding? y/n \n")     # choice of finish programm
    if choice == "y":                                       # if choice is "y" than end programm
      finish = False                                        # False to main bool of while_1
      break                                                 # and breaking this while_2
    elif choice == "n":                                     # if choice is "n" than only breaking while_2
      break                                                 # breaking while_2
    else:                                                   # end if answer is not "y" or "n" than 
      print("unknown answer")                               # print about this problem and start another iteration of while_2