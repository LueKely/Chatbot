
import random

tips = ["Brush Your Teeth!", "Limit sugary drinks",
        "Eat a balanced diet", "Drink Atleast 8 glasses of water a day",
        "Eat more healthy foods (and less processed food)",
        "Do some excercise",
        "If you smoke, try to quit",
        "Make sleep a priority",
        "If you drink alcohol, do so responsibly",
        "Manage stress in a healthy way",
        "Be active",
        "Check your blood pressure regularly",
        "Get vaccinated",
        "Cover your mouth when coughing or sneezing",
        "Talk to someone you trust if you're feeling down",
        "Take antibiotics only as prescribed",
        "Clean your hands properly",
        "Practice good hygiene ",]


def sayTips():
    print("Diwata: " + random.choice(tips))
