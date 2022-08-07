import random
from turtle import clear
import urllib.request
from re import findall
import re
import os
import time
import requests

class Word_bank_location:

    def hardcoded_lst(self):
        '''Hard coded word bank method'''
        bank = ['cantaloupes',"apple", "banana", "cherry", "pomegranates", "orange", "kiwi", "melon", "mango", "orange"]
        return bank

    
    def get_bank_from_file(self):
        '''Word bank from a file method'''
        file_path = 'list_of_fruits.txt'
        file_exists = os.path.exists(file_path)
        if file_exists:                                                 #error checks that file exists
            with open(file_path) as file:
                bank = file.readlines()
                bank = [item.rstrip() for item in bank]
            return bank

        else:
            print('File does not exist')

 
    def regex_from_HTML(self):
        '''Webscrape into a temp local website to get data'''
        url = "[LOCATION OF FILE ON COMP]"
        #url ='[LOCATION OF FILE ON COMP]'
        response = urllib.request.urlopen(url)
        html = response.read()
        htmlStr = html.decode()
        regex_bank =[]

        pattern = findall("\d{1,3}[.]\s[A-Z]*[a-z]\w*", htmlStr)        #pattern to find the words in page
        for item in pattern:
            regex_bank.append(item[3:])                                 #remove leading digits
        return regex_bank

    
    def regex_from_string(self):
        '''Scrape data from a very long string method'''
        string = '1. Grape Purus ut faucibus pulvinar elementum integer. Duis convallis convallis 2. Cherry  Purus ut faucibus pulvinar elementum integer. Duis convallis convallis 3. Watermelon Purus ut faucibus pulvinar elementum integer. Duis convallis convallis 4. Banana Purus ut faucibus pulvinar elementum integer. Duis convallis convallis 5. Orange Purus ut faucibus pulvinar elementum integer. Duis convallis convallis 6. Pomegranate Purus ut faucibus pulvinar elementum integer. Duis convallis convallis 7. Lemon Purus ut faucibus pulvinar elementum integer. Duis convallis convallis 8. Papaya Purus ut faucibus pulvinar elementum integer. Duis convallis convallis 9. Grapefruit Purus ut faucibus pulvinar elementum integer. Duis convallis convallis 10. Pineapple Purus ut faucibus pulvinar elementum integer. Duis convallis convallis'
        pattern = '\d{1,3}[.]\s[A-Z]*[a-z]\w*'                          #pattern to find the words in string
        regex_string_bank =[]

        result = re.findall(pattern, string) 

        for index in range(len(result)):
            result[index] = result[index][3:]                           #remove leading digits
        regex_string_bank = result            

        return regex_string_bank

    
    def word_bank_source(self, selection):
        '''logic to return appropriate word bank source'''
        source_of_word_bank =Word_bank_location                     #instance so that I could use methods
        if selection ==1:
            bank = source_of_word_bank.hardcoded_lst(self)
        if selection==2:
            bank =source_of_word_bank.regex_from_HTML(self)
        if selection ==3:
            bank=source_of_word_bank.regex_from_string(self)
        if selection ==4:
            bank=source_of_word_bank.get_bank_from_file(self)
        return bank




class All_clear_and_display_menus():

    def Weather(self):
        #input the city name
        city_location = input('input the city name: ')
 
        url = 'https://wttr.in/{}'.format(city_location)
        view_weather_requests = requests.get(url)

        print(view_weather_requests.text[:320])



    def menu(self):
        print('*'*40)
        print('\t\t Hangman')
        print('*'*40)
        print('\n')
        

    def clrscr(self):
        # Check if Operating System is Mac and Linux or Windows
        if os.name == 'posix' or os.system('cls'):
            os.system('clear')
        # else:
        #     #
        #     # Else Operating System is Windows
        #     os.system('cls')



    def find_special_chars(self, guess):
        special_char_flag = False
        if(bool(re.match('^[a-zA-Z0-9]*$',guess))==True):
            special_char_flag = False
        else:
            # print("invalid")
            special_char_flag = True
        return special_char_flag


 
    def display(self, temp, letters):
        '''displays the used letters'''
        print("".join(temp))
        print('\nUsed Letters')
        print(letters)    



    def get_bank(self):      
        '''gets bank location'''
        all_clear_instance = All_clear_and_display_menus                #instance so that I could use methods
        number_of_choice_avail =5
        print(f"Player: {self.name.title()} \t\tExtra turns: {self.turns}")
        num_str = input('1. Word bank from a hard coded list \n2. Word bank from a HTML regex \n3. Word bank from a string regex \n4. Word bank read in from a text file \nEnter a selection for word bank list from 1-4: ').lower()
        if (num_str.isdigit()):
            if int(num_str)<number_of_choice_avail and int(num_str)> 0:

                num_str= int(num_str)
            else:
                print(f"The input: {num_str}, is out of range, please try again")
                all_clear_instance.clrscr(self)
                all_clear_instance.menu(self)
                return all_clear_instance.get_bank(self)
        else:
            print(f"The input: {num_str}, is Invalid, please try again")
            all_clear_instance.clrscr(self)
            all_clear_instance.menu(self)
            return all_clear_instance.get_bank(self)
        bank = Word_bank_location.word_bank_source(self,num_str)
        return bank



    def length_and_word(self):
        length_display_menu_instance =All_clear_and_display_menus               #instance so that I could use methods
        length_display_menu_instance.clrscr(self)
        length_display_menu_instance.menu(self)

        bank = length_display_menu_instance.get_bank(self)
        # bank = source_lst()                                   #<---test bank

        temp_word_array =[]

        if len(bank)<=0:
            print(f"\tthe list: {bank} is empty.")
        else:
            for index in range(len(bank)):
                casted_word_list = str(bank[index])                 #casts all objects in list to a string if they werent so before
                if casted_word_list.isalpha() == False:
                    bank.remove(bank[index])                        #error checks that every part of string is contains no special characters or numbers
                    bank.insert(index,'')
                else:
                    temp_word_array.append(bank[index])

            bank = temp_word_array
        word = random.choice(bank)                                  #displays word in end if incorrectly guessed
        lower_cased_word = list(word.lower())                       # keeps word lowercased and gets indexed for game play
        length = len(set(lower_cased_word))                         #duplicate letter removal
        return word, lower_cased_word, length                       #returning random word, length of word and the list of words
        


class Board():
    '''sets board and calls other functions'''
     
     
    def __init__(self, name, turns):                                ## user data upon creation
        self.name = name
        self.turns = turns

    def get_details(self):
       return f"Name = {self.name}\nTurns = {self.turns}"

    def board(self):
        additional_turns = self.turns
        initial_turns = 9
        all_clear_menu_board_instance =All_clear_and_display_menus
        try:
            word, lower_cased_word, length =all_clear_menu_board_instance.length_and_word(self)


            ## Checks letters in word to match on word selected
            word_list =[]
            letters = []
            for i in range(len(word)):
                word_list.append('_')
            print(" ".join(word_list))
            turns =length
            counter = initial_turns+additional_turns                  #<-------change here

            # determines if you win or lose game based on turns remaining or if u guess the right word
            start = time.time()                                             #begin time
            while turns > 0 and counter >0:
                
                print('Hint: Its a fruit')
                
                guess = input('Guess a letter: ')
                if guess.isalpha() and guess in lower_cased_word:
                    if guess in letters:
                        print('try again')
                    else:
                        letters.append(guess)
                        
                        while guess.lower() in lower_cased_word:            #gets user input as lower 
                            all_clear_menu_board_instance.clrscr(self)        #clear screen
                            located = lower_cased_word.index(guess)
                            word_list[located]=guess                        #matches word in temp array with word in current
                            lower_cased_word.pop(located)
                            lower_cased_word.insert(located,"_")
                        #print(f"Turns remaining: {turns}")                 #how many guess of letters is in word

                        turns -= 1
                            
                    if turns ==0:
                        print('You Won')
                        done = time.time()                              #end time
                        elapsed = done - start                          #gets the time
                        print(f"Time it took to guess word was {elapsed:.2f}")
                        time.sleep(1)
                else:
                    if len(guess) >1 or all_clear_menu_board_instance.find_special_chars(self,guess): #<-change
                        all_clear_menu_board_instance.clrscr(self)
                        print('Try again')
                        print(f"{guess} is not valid character\n")
                        counter -=1
                        print(f"Turns remaining: {counter}")
                    else:
                        all_clear_menu_board_instance.clrscr(self)
                        print('Try Again')
                        counter -=1                                             #guesses based on the actual hangman game
                        print(f"Turns remaining: {counter}")
                        if guess.isdigit():
                            print(f"{guess} is not valid character\n")

                        elif guess not in letters:
                            letters.append(guess)
                            
                    
                        if counter ==0:
                            all_clear_menu_board_instance.clrscr(self)            #clear screen
                            print('You Lost')
                            print(f"The word was: {word}")
                            print(f"{self.name.title()} thank you for playing Hangman. Too bad you've lost. Better luck next time")
                            time.sleep(1)
                all_clear_menu_board_instance.display(self,word_list, letters)             
                        
        #if any error happens or empty list 
        except:
            print('Something went wrong')
            if word ==0 or length ==0:
                print(f"The word: {word} has the length of {length} therefore list must be empty")




#----------------------------not in classes ---------------------------------------

def set_num_of_players():
    '''Sets number of players for game'''
    clear_it =All_clear_and_display_menus()
    clear_it.clrscr()
    clear_it.menu()
    flag = ''
    while flag != False:
        num_of_players = input('Enter num of players: ')
        if num_of_players.isdigit() != False:
            flag = False
        else:
            print('enter a correct number\n')

    set_players_turns(num_of_players)


def set_players_turns(num_of_players):
    '''Gets the num of players and makes instances'''
    instances = []

    for x in range(int(num_of_players)):
        flag = ''
        name_flag =''
        while name_flag != False:
                name = input('Enter player name: ')
                if len(name) > 0:
                    name_flag = False
                else:
                    print('Enter a name')
        while flag != False:
            turns = input('Enter num of guess allowed: ')
            print('\n')
            if turns.isdigit() != False:
                    flag = False
            else:
                print('Enter a correct number')

        instances.append(Board(name, turns))
    get_players_info(instances)


def get_players_info(instances):
    '''Takes in a number of players and begins games based on that'''
    print('Players:')
    for index in range(len(instances)):
        print(str(index+1)+": "+instances[index].get_details())
        get_name_from_input = instances[index].name
        get_turns_from_input = instances[index].turns
        int_cast_turns = int(get_turns_from_input)                      #cast input to int to it can be manip for turns
        start_game = Board(get_name_from_input, int_cast_turns)
        start_game.board()
        
        print('\n')


# set_num_of_players()
# start_game = Start_play('boots',10)
# start_game.board()