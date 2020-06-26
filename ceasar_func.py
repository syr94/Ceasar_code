def codeCeasar(text, key):                              # cipher ceasar function only for letters
    new_word = []                                       #creating new var for coded word
    new_letter = ''                                     #creating new var for coded letter
    for i in text:                                      # letter by letter coding text
      if ord(i)>=65 and ord(i)<=90:                     # coding for Uppercase ASCII
        new_letter = chr((((ord(i)-65) + key)%26)+ 65)  # normilize ord int of UpperCase, after that mod of len alphabet (y = x + k(mod N)) N - power of alphabet
        new_word.append(new_letter)                     # appending coded letter
      elif ord(i)>=97 and ord(i)<=122:                  # coding for LowerCase ASCII
        new_letter = chr((((ord(i)-97) + key)%26)+ 97)  # normilize ord int of LowerCase, after that mod of alphabet
        new_word.append(new_letter)                     # appending coded letter
      else:                                             # for symbols and numbers (not letters)
        new_word.append(i)                              # appending symbols and numbers
    return ''.join(new_word)                            # returning new coded text as string type

def decodeCeasar(text, key):                            # uncode ceasar  function only for letters
    new_word = []                                       #creating new var for decoded word
    new_letter = ''                                     #creating new var for decoded letter
    for i in text:                                      # letter by letter decoding text
      if ord(i)>=65 and ord(i)<=90:                     # decoding for Uppercase ASCII
        new_letter = chr((((ord(i)-65) - key)%26)+ 65)  # normilize ord int of UpperCase, after that mod of len alphabet (y = x + k(mod N)) N - power of alphabet
        new_word.append(new_letter)                     # appending decoded letter
      elif ord(i)>=97 and ord(i)<=122:                  #coding for LowerCase ASCII
        new_letter = chr((((ord(i)-97) - key)%26)+ 97)  # normilize ord int of LowerCase, after that mod of alphabet
        new_word.append(new_letter)                     # appending decoded letter
      else:                                             # for symbols and numbers (not letters)
        new_word.append(i)                              # appending symbols and numbers
    return ''.join(new_word)                            # returning new decoded text as string type


get_values = True                                       # bool var for while to avoid wrong keys
while(get_values):                                      # starting iterations while right text is not be inputed
  try:                                                  # try to avoid wrong keys
    row = input("input your text\n")                    # text to code/decode
    user_key = int(input("input your key\n"))           # key
    get_values = False                                  # if key is number than we can stop while
    coded_text = codeCeasar(row, user_key)              # coded text from func 
    print(coded_text)                                   # printing result
    print(decodeCeasar(coded_text, user_key))           # printing decoded text
  except(ValueError):                                   # if key was not number than alert about that user 
    print("you need to put number key")                 # by this