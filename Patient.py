class SymptomChecker:
    def __init__(self, question, yes_node=None, no_node=None, illness=None):
        self.question = question
        self.yes_node = yes_node
        self.no_node = no_node
        self.illness = illness

    def traverse(self):
        print(self.question)
        answer = input("Enter 'yes' or 'no': ").lower()

        if answer == 'yes':
            if self.yes_node is None:
                print("You might have", self.illness)
            else:
                self.yes_node.traverse()
        elif answer == 'no':
            if self.no_node is None:
                print("You seem to be fine.")
            else:
                self.no_node.traverse()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            self.traverse()


# Constructing the symptom checker tree
sore_throat = SymptomChecker("Do you have a sore throat?")
cough = SymptomChecker("Do you have a cough?")
fever = SymptomChecker("Do you have a fever?")
headache = SymptomChecker("Do you have a headache?")
no_symptoms = SymptomChecker("No symptoms. You are healthy!")

# Connecting the nodes
sore_throat.yes_node = cough
sore_throat.no_node = no_symptoms
cough.yes_node = fever
cough.no_node = no_symptoms
fever.yes_node = headache
fever.no_node = no_symptoms
headache.yes_node = SymptomChecker("You might have a common cold.")
headache.no_node = SymptomChecker("You might have the flu.")

# Starting the symptom checker
sore_throat.traverse()
