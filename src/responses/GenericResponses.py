
import random


def say_hi():
    response = ['Hello user', 'How can i help you?',
                'How may i assist you?', "Good day, How may i assist you?"]
    print('DIWATA: '+random.choice(response))


def tagalog():
    response = ['Kamusta user', 'Anong maipaglilingkod ko sayo?',
                'Ano ang maitutulong ko sayo?', "Magandang Buhay! Ano ang maitutulong ko sayo?"]
    print('DIWATA: '+random.choice(response))


def help():
    print("DIWATA: Here are some key words that you need to know!")
    print("hello/hi to greet the user")
    print("who to know the purpose the chatbot")
    print("help to find the keywords to communicate to chatbot")
    print("appointment to have checked and have schedule")
    print("equipment to compare and know what are mandatory requirements")
    print("sick to check the posibilities of symptomes that user have")
    print("tips to get some HealthTips")
    print("kamusta to greet the user in the tagalog language")
    print("Patientlist to check the list of the patients")
    print("Goodbye to close the chatbot")
    print("employees - lists all the employee in the hospital")


def introduction():
    print("DIWATA: I am Diwata Bot and i'll be your personal assistant!! Ask anything you like that i can answer!")


def prank():
    print("DIWATA: As an AI language model, I'm here to assist you. Feel free to ask any questions or let me know what you need help with, and I'll do my best to provide the information or guidance you're looking for.")
