x = 10
y = 10*x

def q1():
  print(question)
question = input("is (X*Y) greater than 100? : ")
if(question) == 'yes':
  print('This is incorrect, please try again')
if(question) == 'no':
  print('Then what is the answer?')
  answer = input(" ")
  if(answer) == '100':
    print("Correct!")
    exit()
  if not(answer) == '100':
    print("That's not it chief...")
© 2019 GitHub, Inc.
