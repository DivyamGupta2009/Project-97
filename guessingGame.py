import random
n = random.randint(1,10)
guess = 5
while(guess>0):
    a = int(input("Guess a number(between 1 and 10): "))
    if (a>10):
        print("Guess a number between 1 and 10!")
        guess = guess-1
    elif(a<0):
        print("Guess a number between 1 and 10!")
        guess = guess-1
    elif(a<n):
        print("Guess a higher number.")
        guess = guess-1
    elif(a>n):
        print("Guess a lower number.")
        guess = guess-1
    #elif(guess==0):
       # print("Oh no. You ran out of guesses! The number was",n)
    elif(a == n):
        print("Congrats! You won!")
        break
    while guess == 0:
        print("Oh no. You ran out of guesses! The number was",n)
        break
        
    
