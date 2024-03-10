import random as r

class Hangman():

    def __init__(self):
        self.chances_left = 5
        self.has_won = False
        self.words = [
                {'hint':'fruit','value':'mango'},
                {'hint':'colour','value':'red'},
                {'hint':'country','value':'india'},
                {'hint':'animal','value':'giraffe'},
                {'hint':'stock','value':'sensex'},
                {'hint':'city','value':'london'},
                {'hint':'insect','value':'ant'},
                {'hint':'vegetable','value':'raddish'},
                {'hint':'food','value':'cheese'},
                {'hint':'plant','value':'cactus'},
                {'hint':'sports','value':'chess'},
                {'hint':'A foul','value':'tackle'},
                {'hint':'movie','value':'ironman'},
                {'hint':'soft-drink','value':'coke'},
                {'hint':'video game','value':'valorant'},
                {'hint':'an element','value':'sulphur'}
            ]
    
    def welcome_to_game(self):
        print('*' * 35)
        print("Welcome to the Hangman game!")
        print('*' * 35)
        print()
        self.shuffle()

    def shuffle(self):
        r.shuffle(self.words)
        self.select_word()
    
    def select_word(self):
        selected_dictionary = self.words.pop()
        self.hint = selected_dictionary['hint']
        self.word = selected_dictionary['value']
        print(f"Let's Begin!")
        print(f"\nYour Hint is : {self.hint.upper()} | {len(self.word)} words!")
        print(f'You have {self.chances_left} Chances')

        '''To create blank spaces handling list before printing it''' 
        self.blank_space_handler() 
        self.word_characters = [x for x in self.word]
        self.get_input()

    def is_valid_input(self,user_input):
        if self.user_input.isalpha() and len(self.user_input) == 1:
            return True
        else:
            print("You must enter a character!")
            return False
    
    def check_letter(self,user_input):
        letter_to_check = user_input
        if letter_to_check in self.word_characters:
            index = self.word_characters.index(letter_to_check)
            self.word_characters[index] = ""
            self.blank_list[index] = letter_to_check
            return True
        
        else:
            self.chances_left -= 1
            print(f"'{self.user_input}' is not in the word!  Try again")
            return False

    def get_input(self):
        while self.chances_left > 0 and not self.has_won:
            print("*" * 35)
            print(f"Number of Chances Left: {self.chances_left}")
            print(self.print_list(self.blank_list))
            print()
            # self.print_list(self.blank_list)
            self.user_input = input("Enter a letter : ").lower()
            if self.is_valid_input(self.user_input):
                self.check_letter(self.user_input)
                self.check_winner()
            else:
                continue
        return False
    
    def check_winner(self):        
        if self.print_list(self.blank_list) == self.word:
            print('\n')
            print(self.print_list(self.blank_list))
            print("*" * 35)
            print(f"You have guessed the word '{self.word}'!")
            print("You're good at this! '")
            print("\nThanks for playing! ")
            self.has_won = True
            return True
        elif self.chances_left == 0:
            print()
            print('*' * 35)
            print(f'Looks like you ran out of chances :( ')
            print(f"\nCorrect word was : {self.word}")
            print("\nBetter luck next time !")
            print()
            print("*" * 35)
            return True
        return False
    
    def blank_space_handler(self):
        self.blank_list = []
        for x in range(len(self.word)):
            self.blank_list.append(' _ ')
        return 
    
    def print_list(self,list):
        self.progress = ""
        for x in list:
            self.progress += x
        return self.progress

hangman = Hangman()
hangman.welcome_to_game()
