import random
import json

class GameManager:
    def __init__(self):
        self.attempts = 0
        self.highscore = self.load_highscore()
        self.dificulty = self.load_level()
        
        
    def generate_secret_number(self):
        return random.randint(1, 100)
    
    
    def load_level(self):
        try:
            with open('game_data.json', 'r') as file:
                game_data = json.load(file)
            self.dificulty = game_data.get('level', 1)
        except FileNotFoundError:
            self.dificulty = 1
        
        
        return self.dificulty
        
        
    def load_highscore(self):
        print("highscore loaded")
        try:
            with open("game_data.json", "r") as file:
                game_data = json.load(file)
        except FileNotFoundError:
            game_data = {'highscore': 0}
            
        highscore = game_data['highscore']
        with open("game_data.json", "w") as file:
            json.dump(game_data, file, indent=2)
        
        return highscore
    
            
    def reset_high_score(self):
        with open("game_data.json", 'r') as file:
            game_data = json.load(file)
        game_data['highscore'] = 0
        with open("game_data.json", 'w') as file:
            json.dump(game_data, file, indent=2)
    
    def play_game(self):
        secret_number = self.generate_secret_number()
        attempts = 0
        if self.dificulty == 1:
            dificulty = 10
        elif self.dificulty == 2:
            dificulty = 5
        else:
            dificulty = 3
            
        while attempts < dificulty:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            if user_guess < secret_number:
                print("The number is higher than your guess")
            elif user_guess > secret_number:
                print("The number is lower than your guess")
            else:
                print("Congratulations! You guessed the number correctly")
                score = 100 - (attempts * 5)
                if score > self.highscore:
                    self.set_highscore(score)
                    print(f"New high score is achived: {score}")
                else:
                    print(f"Your score: {score}")
                break
        else:
            print(f"Sorry! You have exhausted all your attempts. The number was {secret_number}")
        
        next_round = input('Do you want to play again? y/n: ')
        if next_round.lower() != 'n':
            self.play_game()
        else:
            print("Thanks for playing! come back again")
        
        
    
    def display_welcome_message(self):
        print("\n" + "=" * 50)
        print(" Welcome to Number Guessing Game CLI Application")
        print(" Guess the number between 1 and 100")
        print(" The computer will tell you if the number is higher or lower")
        print(" Try to guess the number in the fewest attempts")
        
        
    def change_level(self):
        try:
            with open('game_data.json', 'r') as file:
                game_data = json.load(file)
            print("\nCurrent level is: ", game_data.get('level', 1))
        except FileNotFoundError:
            print("level is not setted yet let's create it.")
            game_data = {}
            
        print("1. Easy level (10 attempts)")
        print("2. Medium level (5 attempts)")
        print("3. Hard level (3 attempts)")
        choice = input("Enter your choice: ")
        game_data['level'] = choice
        with open('game_data.json', 'w') as file:
            json.dump(game_data, file, indent=2)
        
        print("level setted successfully!!")
        
    def set_highscore(self, score):
        with open("game_data.json", "r") as file:
            game_data = json.load(file)
        game_data['highscore'] = score
        
        with open("game_data.json", "w") as file:
            json.dump(game_data, file, indent=2)
            
        self.highscore = score
        


    def game_setting(self):
        print("\n" + "=" * 50)
        print("1. Change level")
        print("2. Reset high score")
        print("3. Exit")
        conta = True
        
        while conta:
            choice = input("Enter your choice: ")
            if choice == '1':
                self.change_level()
                conta = False
            elif choice == '2':
                self.reset_high_score()
                conta = False
            elif choice == '3':
                exit()
                conta = False
            else:
                print("Invalid choice!!")
                print("Please choose from the given options only")
                print("1. Change level")
                print("2. Reset high score")
                print("3. Exit")
                conta = True
                