import random 

game = ["Stone", "Scissor", "Paper"]

while True:
    print("Choice:")
    print("Scissor")
    print("Stone")
    print("Paper")
    
    
    ch1 = input("Enter your choice: ")
    ch2 = random.choice(game)
     
    if ch1 != 'Stone' and ch1 != 'Scissor' and ch1 != 'Paper':
        print("Wrong input. Try again")
    else:
        if ch1 == 'Stone' and ch2 == 'Paper':
            print("You lose!")
        if ch1 == 'Stone' and ch2 == 'Scissor':
            print("You win!")
        if ch1 == 'Stone' and ch2 == 'Stone':
            print("Draw")        
        if ch1 == 'Scissor' and ch2 == 'Stone':
            print("You lose!")
        if ch1 == 'Scissor' and ch2 == 'Paper':
            print("You win!")
        if ch1 == 'Scissor' and ch2 == 'Scissor':
            print("Draw")
        if ch1 == 'Paper' and ch2 == 'Stone':
            print("You win!")
        if ch1 == 'Paper' and ch2 == 'Paper':
            print("Draw")
        if ch1 == 'Paper' and ch2 == 'Scissor':
            print("You lose!")