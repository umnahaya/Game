import random

questions = [
    {"emoji": "🦁👑", "answer": "lion king", "display": "The Lion King"},
    {"emoji": "🕷️👨", "answer": "spiderman", "display": "Spider-Man"},
    {"emoji": "🍎🥧", "answer": "apple pie", "display": "Apple Pie"},
    {"emoji": "🐝🍯", "answer": "honey", "display": "Honey"},
    {"emoji": "🌧️🌈", "answer": "rainbow", "display": "Rainbow"},
    {"emoji": "🐈", "answer": "cat", "display": "Cat"},
    {"emoji": "🧊🍦", "answer": "ice cream", "display": "Ice Cream"},
    {"emoji": "🌙⭐", "answer": "night sky", "display": "Night Sky"},
]

random.shuffle(questions)
score = 0

print("Welcome to Guess the Emoji!")
print("Guess what the emojis represent.\n")

for question in questions:
    print("Emoji:", question["emoji"])
    guess = input("Your answer: ").strip().lower()

    if guess == question["answer"]:
        print("Correct!\n")
        score = score + 1
    else:
        print("Incorrect. The answer was:", question["display"], "\n")

print("Game Over!")
print("Your final score is:", score, "out of", len(questions))
