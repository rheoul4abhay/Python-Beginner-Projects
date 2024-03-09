import random as r

class Game():
    
    def __init__(self):
        self.min_limit = 0
        self.max_limit = 0
        self.generated_number = 0
        self.number_of_turns = 0

    def welcome_message(self):
        print("Welcome to the number guessing game!")
        print('*' * 35)
        print()

    def choose_difficulty(self):
        made_choice = ''
        choices = ['easy','normal','hard']
        while made_choice not in choices:
            print('*' * 35)
            made_choice = input("Enter difficulty (Easy,Normal or Hard) : ").lower()
            if(made_choice not in choices):
                print("You must enter a valid choice!")
                print()
        print(f"Chosen Difficulty : {made_choice.upper()} !")
        print()
        if made_choice == 'easy':
            self.number_of_turns = 8
        elif made_choice == 'normal':
            self.number_of_turns = 6
        else : self.number_of_turns = 5

    def choose_range(self):
        try:
            self.min_limit = int(input("Enter minimum number in range : "))
            self.max_limit = int(input("Enter maximum number in range : "))
            print()

        except ValueError as error:
            print("You must enter a number!")
            print()
            self.choose_range()

    def generate_number(self):
        self.generated_number = r.randint(self.min_limit,self.max_limit)
    
    def input_choices(self):
        self.current_turn = 0
        while self.number_of_turns > 0  :
            self.current_turn += 1
            correct_input = False
            print(f"Chances left : {self.number_of_turns}")
            while not correct_input :
                try:
                    self.user_input = int(input(f"Choose a number : "))
                    correct_input = True
                except ValueError as Exception:
                    print("You must  enter a number!")
                    print("Try again!")
                    print()
            if self.check_for_win() : return self.play_again()
            self.number_of_turns -= 1 
        print(f"You Lose! Correct Number was {self.generated_number}.\nBetter Luck Next Time!")
        self.play_again()

    def check_for_win(self):
            if(self.user_input == self.generated_number):
                print("*" * 35)
                print(f"\nCongrats! You guessed the number right.")
                print(f"Number of turns taken : {self.current_turn}")
                return True
            elif self.user_input > self.generated_number :
                print("You guessed too high!")
                print()
                return False
            else :
                print("You guessed too small!")
                print()
                return False
            
    def play_again(self):
        restart_input = ''
        while restart_input not in ['yes','no']:
            print()
            restart_input = input("Want to play again? (Yes/No) : ").lower()
            if restart_input == "yes":
                print('*' * 35)
                print()
                self.start()
            elif restart_input == "no" : 
                self.game_over()
                break 
            else : 
                print("Enter either 'Yes' or 'No' !")
                continue

    def game_over(self):
        print(f"Thanks for playing !")
        print()
        return

    def start(self):
        self.welcome_message()
        self.choose_difficulty()
        self.choose_range()
        self.generate_number()
        self.input_choices()
    
game = Game()
game.start()
