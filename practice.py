import random
num = random.randint(1, 100)
while True :
    print("guess a number 1-100")
    guess = input("Your guess: ")
    i = int(guess) 
    if i == num :
        num_times += 1
        print("You Won! ")
        print("+10 points!")
        break
    elif i < num :
            print("try higher!")
    if i > num :
            print("try lower")

        
