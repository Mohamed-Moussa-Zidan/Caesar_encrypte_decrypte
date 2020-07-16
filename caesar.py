import sys
p=''
if(sys.argv[1]=='-k' and sys.argv[2].isdigit() and sys.argv[3]=='-p'):
  for i in sys.argv[4]:
    if(not i.isalpha()): #checking for the alphabet
      p=''.join(i) #printing it whithout any change
    else:
      if(i.isupper()): #checking for the uppercase alphabet
        p=p+''.join(chr((((ord(i)-ord('A'))+int(sys.argv[2])) % 26)+ord('A'))) #turn the char to int and adding it to the key and vice versa (for the uppercase)
      else:
        p=p+''.join(chr((((ord(i)-ord('a'))+int(sys.argv[2])) % 26)+ord('a'))) #turn the char to int and adding it to the key and vice versa (for the lowercase)
  print(p)
  #print(''.join((i) if not i.isalpha() else (chr((((ord(i)-ord('A'))+int(x[2])) % 26)+ord('A')) if i.isupper() else (chr((((ord(i)-ord('a'))+int(x[2])) % 26)+ord('a')))) for i in x[4])) //one line code for the algorithm
elif( sys.argv[1]=='-k' and sys.argv[2].isdigit() and sys.argv[3]=='-c'):#the inverse of the above (subtracting the key)
  for i in sys.argv[4]:
    if(not i.isalpha()):
      p=''.join(i)
    else:
      if(i.isupper()):
        p=p+''.join(chr((((ord(i)-ord('A'))-int(sys.argv[2])) % 26)+ord('A')))
      else:
        p=p+''.join(chr((((ord(i)-ord('a'))-int(sys.argv[2])) % 26)+ord('a')))
  print(p)
  #print(''.join((i) if not i.isalpha() else (chr((((ord(i)-ord('A'))-int(x[2])) % 26)+ord('A')) if i.isupper() else (chr((((ord(i)-ord('a'))-int(x[2])) % 26)+ord('a')))) for i in x[4]))
else: print("Please Enter Right Syntax")
