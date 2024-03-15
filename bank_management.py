import random

data = [
        {'new_user_name':'rohit','password':'aQ12Gjk@','available_balance':1000},
        ]

class Bank:

    def __init__(self,bank,user):
        self.bank_name = bank
        self.new_user_name = user
        self.have_registered = False
        self.new_user_entry = None
        print('*' * 50)
        print('')
        print(f'Welcome to {self.bank_name.upper()}, how can we help you today?')
        print('')
        print('*' * 50)

    def welcome(self):
        print('\n1.Deposit Money ')
        print('2.Withdraw Money ')
        print('3.Check Balance ')
        print('4.Register New User')
        print('')
        self.get_input()

    def get_input(self):

        try:
            user_input = int(input('Enter a choice between 1-4 : '))
            if  user_input in  [1,2,3,4]:
                self.choose_facility(user_input)
            else:
                raise ValueError
        except ValueError:
            print('Please enter a valid choice between 1-4')
            print('\n')
            self.get_input()       

    def choose_facility(self,input):
        if self.have_registered:
            user_input = input
            if user_input == 1:
                self.get_deposit(self.new_user_name)
            elif user_input == 2:
                self.get_withdraw(self.new_user_name)
            elif user_input == 3:
                self.print_balance(self.new_user_name)
            else:
                self.register()
                self.want_to_continue()
        else:
            self.fetch_data(self.new_user_name)

    def fetch_data(self,new_user_name):

        for entry in data:
            '''We need to first check if there is an entry in the data list abt user'''
            if entry.get('new_user_name') == new_user_name:
                return True
        #If we reached here means no data with given username found!
        print('')
        print('Oops! Looks like you haven\'t registered yet! ' )
        self.register()

    def get_deposit(self,new_user_name):
        if self.have_registered:
            print("You chose 'Deposit' facility")
            print('')
            try:
                deposit_input = int(input('Enter Amount to be deposited: '))
                if deposit_input > 50000:
                    print("Max limit for each deposit is '50,000'.")
                    print('')
                    print('Try again! ')
                    print('')
                    self.get_deposit(self.new_user_name)
                elif deposit_input <= 0:
                    print('Deposit amount must be greater than 0!')
                else :
                    self.new_user_entry['available_balance'] += deposit_input
                    print('')
                    print(f'Your account credited by {deposit_input} successfully!')
                    print(f'Available Balance : {self.new_user_entry['available_balance']}.')
                    self.want_to_continue()
            except ValueError:
                    print('Enter a valid Amount to Deposit!')
                    self.get_deposit(new_user_name)

    def get_withdraw(self,new_user_name):
        if self.have_registered:
            print('You chose "Withdraw" facility')
            print('')
        try:
            withdraw_input = int(input('Enter Amount to withdraw : '))
            if withdraw_input <= 0:
                print('Withdrawl amount must be greater than 0!')
                self.get_withdraw(self.new_user_name)
            elif withdraw_input > self.new_user_entry['available_balance']:
                print('Not sufficient account balance to withdraw!')
                self.get_withdraw(self.new_user_name)
            else:
                self.new_user_entry['available_balance'] -= withdraw_input
                print('')
                print(f'Your Account Debited for {withdraw_input} successfully!')
                print(f'Available Balance : {self.new_user_entry['available_balance']}.')
                print('')
                print('You may collect the cash from machine!')
                print('')
                self.want_to_continue()
        except ValueError:
            print('Enter a valid Amount to Withdraw')
            self.get_withdraw()
    
    def print_balance(self,new_user_name):
        if self.have_registered:
            print('You chose "Check Balance" facility')
            print('')
            print('*'*30)
            print('')
            print(f'Hello {new_user_name}')
            print(f'Your Current Account Balance is : {self.new_user_entry['available_balance']}')
            print('')
            print('*'*30)

    def register(self):
        print('')
        print('Let\'s get you registered with us ...')
        print('')
        try:
            input_name = input('Enter your name : ').lower()
            if input_name[0] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                print('')
                print('*'*30)
                print(f'Welcome {input_name.upper()}')
                user_password = self.generate_password()
                print('')
                print(f'Your generated password is : {user_password}')
                print('')
                data.append({'username':input_name,'password':user_password,'available_balance':0})
                self.new_user_entry = {'username':input_name,'password':user_password,'available_balance':0}
                self.have_registered = True
                print('You\'re now registered successfully')
                print(f'Thanks for choosing our bank services.')
                print('')
                print('*' * 30)
                print('')
                self.welcome()
                self.get_input()
            else:
                raise ValueError
        except ValueError:
            print('You must enter a valid username that begin with an alphabet!')
            self.register()

    def generate_password(self):
        pwd = ''
        characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','_']
        '''Lets generate a unique 6 digit password for new users'''
        for i in range(6):
            random.shuffle(characters)
            ch = random.choice(characters)
            pwd += ch
        return pwd
    
    def want_to_continue(self):
        try:
            post_input = input('Want to continue? (Yes/No)').lower()
            if post_input == 'yes':
                self.welcome()
            elif post_input == 'no':
                self.say_goodbye()
            else:
                raise ValueError
        except ValueError :
            print('You must enter either "yes" or "no" !')
            self.want_to_continue()

    def say_goodbye(self):
        print('')
        print('*' * 60)
        print(f'We are glad to assist you. Thanks for visiting. Goodbye')
        print('')

bank = Bank('State Bank','Abhay')
bank.welcome()
