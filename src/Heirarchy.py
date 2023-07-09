import classes

# Create employees
ceo = classes.MyEmployee("Anunciacion Lue Kely D.", "CEO")
cto = classes.MyEmployee("Joe Biden", "CTO")
cfo = classes.MyEmployee("Guadalupe Richo ", "CFO")
manager1 = classes.MyEmployee("Rodriguez Gonzales", "Manager")
manager2 = classes.MyEmployee("Bob Wilson", "Manager")
developer1 = classes.MyEmployee(
    "Mia Rosa de la Comilda Rodriguez la Hermanos", "Developer")
developer2 = classes.MyEmployee("Michael Clark", "Developer")
accountant = classes.MyEmployee("Sara Thompson", "Accountant")

# Build organizational hierarchy
ceo.add_subordinate(cto)
ceo.add_subordinate(cfo)
cto.add_subordinate(manager1)
cto.add_subordinate(manager2)
manager1.add_subordinate(developer1)
manager1.add_subordinate(developer2)
cfo.add_subordinate(accountant)

# Function to print the organizational hierarchy recursively


def print_hierarchy(employee, level=0):
    print("    " * level + f"- {employee.name} ({employee.position})")
    for subordinate in employee.subordinates:
        print_hierarchy(subordinate, level + 1)


# Print the organizational hierarchy starting from the CEO

def run():
    print_hierarchy(ceo)
