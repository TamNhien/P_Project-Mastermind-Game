import random

num = random.randrange(1000, 10000)

def play_guessing_game():
    n = int(input("Guess the 4 digit number: "))
    ctr = 0
    
    while n != num:
        ctr += 1
        count = 0
        n_str = str(n)
        num_str = str(num)
        correct = []
        
        for i in range(4):
            if n_str[i] == num_str[i]:
                count += 1
                correct.append(n_str[i])
                
        if count < 4 and count != 0:
            print("Not quite the number. But you dit get ", count, " digit(s) correct!")
            print("Also these numbers in your input were correct: ", end='')
            print(*correct)
            
            n = int(input("Enter your next choice of numbers: "))
        elif count == 0:
            print("None of numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))
            
    print("You've become a Mastermind!")
    print("It took you only", ctr, "tries.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_guessing_game()
        
play_guessing_game()
            