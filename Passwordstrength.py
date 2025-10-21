import re
import string
password = ""
caps_score = 0
small_letter_score = 0
digit_score = 0
special_char = 0
attempt = 0
flag = True
while flag:
  password = input("Enter your password: ")
  if len(password) >= 8:
     for i in password:
       if re.search("[A-Z]",i):
        caps_score +=1
       elif re.search("[a-z]",i):
        small_letter_score +=1
       elif re.search(r'\d',i):
         digit_score +=1
       elif i in string.punctuation:
          special_char =+1

  if( caps_score >=1 and small_letter_score >=1 and digit_score >=1 and special_char >=1 ):
        print("Your Password is valid:"+ password)
        flag = False
  else:
        print("Kindly enter a valid password")
        flag = True
        attempt +=1

  if(attempt == 3):
    print("You have reached your maximum attempt Try after sometime")
    flag = False







