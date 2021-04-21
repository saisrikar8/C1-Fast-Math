import random
import time

#Prompt 1
print("Welcome to Multiplication Game.")
print("You will be prompted to solve a math equation")
print("and you will need to answer within 3 seconds.")

#Prompt 2
ready = input('Are you ready to playy(y/n)?:\n').lower()
score = 0
#Main Game Loop
while (ready == 'y' or ready == "yes"):
  num1 = random.randint(0,12)
  num2 = random.randint(0,12)
  print("\n")
  for x in range(3):
    print(3 - x)
    time.sleep(1)

  t1 = time.time()
  question = int(input(str(num1) + " x " + str(num2) + " = "))
  t2 = time.time()
  eta = t2 - t1
  print("\n\n\nYou took " + str(eta) + " seconds")
  if ( t2 - t1 >= 3 or question != num1 * num2):
    print("YOU FAILED! :P")
  elif (question == num1 * num2):
    print("You got it!")
    score += 1
  
  print("Total Score: " + str(score))
  ready = input("Are you ready to play?(y/n)\n").lower()


print("Thanks for playing")