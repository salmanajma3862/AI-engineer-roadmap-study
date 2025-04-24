class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What is the color of apples?\n(a) Red\n(b) Purple\n(c) Orange\n(d) Blue\n",
    "What is the color of bananas?\n(a) Red\n(b) Purple\n(c) Yellow\n(d) Blue\n",
    "What is the color of strawberries?\n(a) Red\n(b) Purple\n(c) Yellow\n(d) Blue\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)


"""""
class Country:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

countries =[
    Country("Pakistan", "Islamabad"),
    Country("India", "New Delhi"),
    Country("Bangladesh", "Dhaka"),
]

def country_capital_guess(countries):
    score = 0
    for country in countries:
        answer = input(f"What is the capital of {country.name}? ")
        if answer.lower() == country.capital.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The capital of {country.name} is {country.capital}.")
    print(f"Your final score is: {score}/{len(countries)}")
    score = 0

country_capital_guess(countries)
"""
