import re
import random
from Title import say_title_name


say_title_name()

def say_hi():
   response = ['Hello user', 'How can i help you?', 'How may i assist you?']
   print('DIWATA: '+random.choice(response) )

def help():
    print("DIWATA: Here are some key words that you need to know!")

def introduction():
    print("DIWATA: I am Diwata Bot and i'll be your personal assistant!! Ask anything you like that i can answer!")

def prank():
    print("DIWATA: As an AI language model, I'm here to assist you. Feel free to ask any questions or let me know what you need help with, and I'll do my best to provide the information or guidance you're looking for.")

def split_messages(message):
    return re.split(r'\s+|[,;?!.-]\s*',message.lower())


def find_value_in_dict(array, dictionary):
   for key in array:
        if key in dictionary:
            function = dictionary[key]
            function()  # Execute the function
        
hello = True

def farewell():
    print("DIWATA: goodbye, I hope that i have assited you!!")
    global hello
    hello = False
    
   

my_dic = {'hello':say_hi,"who":introduction,"help":help, "prank":prank, 'goodbye':farewell }


def main():
      while True:
        user_input = input("USER: ")
        find_value_in_dict(split_messages(user_input),my_dic)
        if hello == False: break



if __name__ == '__main__':  
    main()




