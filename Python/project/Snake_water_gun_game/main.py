# Snake Water Gun game

def game():
    import random # For generating random computer choices


     # Starting point of game
    print("===Welcome to Snake, Water and Gun game===")
    num = int(input("Enter 1 for start:"))
    score = 0 
    if num == 1:
        # Game menu 
        while True:
            print("Game start\nChose your option\n1.Snake\n2.Water\n3.Gun")
            user_option = int(input("Enter your option:"))

            computer_option = random.randint(1,3) 

            if user_option == computer_option:
                print(f"Your option= {user_option}\nComputer option= {computer_option}")
                print("Game draw")
            
            elif user_option == 1 and computer_option == 2:
                print(f"Your option= {user_option}.Snake\nComputer option= {computer_option}.Water")
                print("Snake beats the water")
                print("You Won")
                score = score+1

            elif user_option ==2 and computer_option ==3:
                print(f"Your option= {user_option}.Water\nComputer option= {computer_option}.Gun")
                print("The water beats the gun")
                print("You Win")
                score = score+1 

            elif user_option ==3 and computer_option ==1:
                print(f"Your option= {user_option}.Gun\nComputer option= {computer_option}.Snake")
                print("The gun beats the snake")
                print("You Win")
                score = score+1

            elif user_option == 1 and computer_option == 3:
                print(f"Your option= {user_option}.Snake\nComputer option= {computer_option}.Gun")
                print("The snake can't beat the gun")
                print("You Loss")
            
            elif user_option ==2 and computer_option ==1:
                print(f"Your option= {user_option}.Water\nComputer option= {computer_option}.Snake")
                print("The water can't beats the Snake")
                print("You Loss")
                
            elif user_option ==3 and computer_option ==2:
                print(f"Your option= {user_option}.Gun\nComputer option= {computer_option}.Water")
                print("The Gun can't beat the Water")
                print("You Loss")
            
            else:
                print("Enter valid option")
            print("current Score =",score)
            
            try:
                # Reading high score from file
                with open("hiscore.txt") as f:
                    hiscore  = f.read()
                    if hiscore!= "":
                        hiscore = int(hiscore)
                    else:
                        hiscore = 0
            except FileNotFoundError:
                # If file not found, stop the game
                print("hiscore.txt not found! create a file")
                break


            # If current score is higher than stored high score, update the file 
            if (score>=hiscore):
                with open("hiscore.txt", "w") as f:
                    f.write(str(score))

            with open("hiscore.txt") as f:
                print(f"High Score = {f.read()}")
            

             # Ask player to play again or quit
            choice = input("Enter 1 to play again, or any other key to quit: ")
            if choice != "1":
                print("Thanks for playing!")
                break 
            
# Run the game if script is executed directly
if __name__ == "__main__":
    game()

            
        

        