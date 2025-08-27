import random

def generate_question():
    """Random math question generate (numbers 1 to 16 only)"""
    operators = ['+', '-', '*']
    num1 = random.randint(1, 16)
    num2 = random.randint(1, 16)
    op = random.choice(operators)

    question = f"{num1} {op} {num2}"
    answer = eval(question)
    return question, answer

def play_game():
    print("\n==========================")
    print(" 🧮 Math Quiz Duel 🧮 ")
    print("==========================\n")
    print("Two players take turns. Each correct answer = +1 point.\n")

    players = ["Player 1", "Player 2"]
    scores = {"Player 1": 0, "Player 2": 0}

    rounds = 5  # total rounds

    for round_num in range(1, rounds + 1):
        print(f"\n----- 🔢 Round {round_num} 🔢 -----")
        for player in players:
            question, answer = generate_question()
            print(f"{player}, solve: {question} = ?")
            guess = int(input("Your answer: "))

            if guess == answer:
                print("✅ Correct!")
                scores[player] += 1
            else:
                print(f"❌ Wrong! Correct answer was {answer}")

    print("\n==========================")
    print(" 📊 Final Scores 📊 ")
    for player, score in scores.items():
        print(f"{player}: {score}")
    print("==========================")

    if scores["Player 1"] > scores["Player 2"]:
        print("🏆 Player 1 Wins!")
    elif scores["Player 2"] > scores["Player 1"]:
        print("🏆 Player 2 Wins!")
    else:
        print("🤝 It's a Draw!")

# Main loop
while True:
    play_game()
    restart = input("\nDo you want to play again? (Y/N): ").strip().lower()
    if restart != 'y':
        print("👋 Thanks for playing! Bye!")
        break
