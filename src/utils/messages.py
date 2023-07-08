import re

# splits your response into an array


def split_messages(message):
    return re.split(r'\s+|[,;?!.-]\s*', message.lower())

# puts in the array of responses and checks it into the dectionary if it
# exists


def find_value_in_dict(array, dictionary):
    for key in array:
        if key in dictionary:
            function = dictionary[key]
            return function()  # Execute the function
    print("DIWATA: Whoopsies look like i do not know what you are talking about")
    return
