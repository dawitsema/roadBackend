
from game_manager import GameManager

gamemanager = GameManager()

def display_welcome_message():
    print("\n" + "=" * 50)
    print("")
    print("\tWelcome to Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    print("")
    print("=" * 50)
    
display_welcome_message()
while True:
    print('1. play new game')
    print("2. view highscore")
    print("3. reset highscore")
    print("4. game settings")
    user_choice = input("Enter your choice: ")

    if user_choice == '1':
        gamemanager.play_game()
    elif user_choice == '2':
        print(f"Highscore: {gamemanager.load_highscore()}")
    elif user_choice == '3':
        gamemanager.reset_high_score()
        print("Highscore reset successfully")
    elif user_choice == '4':
        gamemanager.game_setting()
    
    to_leave = input("Do you want to continue? y/n : ")
    if to_leave.lower() == 'n':
        break
    

    
