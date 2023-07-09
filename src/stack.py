class HospitalChatbot:
    def __init__(self):
        self.stack = []

    def add_patient(self):
        name = input("Enter patient's name: ")
        age = input("Enter patient's age: ")
        condition = input("Enter patient's condition: ")
        self.stack.append({"name": name, "age": age, "condition": condition})

    def next_patient(self):
        if len(self.stack) == 0:
            print("No more patients")
        else:
            patient = self.stack.pop()
            print("Next patient:", patient["name"])

    def show_patients(self):
        print("Patients in queue:")
        for patient in self.stack[::-1]:
            print("name :", patient["name"], ",age :",
                  patient["age"], ",condition :", patient["condition"])

    def search_patient(self):
        name = input("Enter patient's name: ")
        for patient in self.stack:
            if patient["name"] == name:
                print("Patient found:", patient)
                return
        print("Patient not found")

    def remove_patient(self):
        name = input("Enter patient's name: ")
        for i in range(len(self.stack)):
            if self.stack[i]["name"] == name:
                del self.stack[i]
                print("Patient removed")
                return
        print("Patient not found")

    def update_patient(self):
        name = input("Enter patient's name: ")
        for i in range(len(self.stack)):
            if self.stack[i]["name"] == name:
                age = input("Enter new age: ")
                condition = input("Enter new condition: ")
                self.stack[i]["age"] = age
                self.stack[i]["condition"] = condition
                print("Patient updated")
                return
        print("Patient not found")


chatbot = HospitalChatbot()


def run():
    while True:
        print("\nPatient List")
        print("1. Add patient")
        print("2. Show next patient")
        print("3. Show all patients")
        print("4. Search for a patient")
        print("5. Remove a patient")
        print("6. Update a patient")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if (choice == '7'):
            break
        else:
            if choice == '1':
                chatbot.add_patient()
            elif choice == '2':
                chatbot.next_patient()
            elif choice == '3':
                chatbot.show_patients()
            elif choice == '4':
                chatbot.search_patient()
            elif choice == '5':
                chatbot.remove_patient()
            elif choice == '6':
                chatbot.update_patient()
