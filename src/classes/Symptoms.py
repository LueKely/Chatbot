class MySymptoms:
    def __init__(self) -> None:
        self._db = {"common cold": {"fever", "cough", "high temperature"},
                    "COVID 19": {"no sense of taste", "cough", "high temperature", "fever"},
                    "diarrhea": {"abdominal cramps", "abdominal pain", "watery stools"}}

        self._symptomes = ""
        self._arr = []
        self._set = set([])
        self._conclusion = []
        self._union = set([])

    def set_symptomes(self):

        self._symptomes = input(
            "DIWATA: Please insert your symptoms and seperate them into a comma \nUSER: ")
        if (self.compare_symptomes != ""):
            self._arr.extend(self._symptomes.split(','))
            for item in self._arr:
                self._set.add(item.lower())
        else:
            print("DIWATA: Please insert your symtomes")

    def get_symptomes(self):
        if (len(self._set) != 0):
            print("DIWATA: These are your symptoms that you are experiencing")
            print(self._set)
            print("DIWATA: Please get professional help for further info")
        else:
            print("DIWATA: Looks like this is not in our database")

    def compare_symptomes(self):
        # loops through the keys
        for key in self._db:
            self._union = self._set.intersection(self._db[key])
            if len(self._union) >= round(len(self._db[key])*0.5):
                self._conclusion.append(key)

    def get_conclusion(self):
        print("DIWATA: Here are the possible outcomes:")
        print(self._conclusion)
