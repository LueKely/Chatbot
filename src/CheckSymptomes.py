import classes
import utils

switch = classes.MySwitch()
Symptoms = classes.MySymptoms()


def result():
    Symptoms.compare_symptomes()
    Symptoms.get_conclusion()


my_dic = {"here": Symptoms.set_symptomes,
          "see": Symptoms.get_symptomes, "results": result, "exit": switch.change_value}


def run():
    print("DIWATA: You have initialized the Symptomes diagnosis")

    while True:
        if switch._value == False:
            break
        else:
            userInput = input("USER: ")
            utils.find_value_in_dict(utils.split_messages(userInput), my_dic)
