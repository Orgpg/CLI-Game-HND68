import time
import random

def play_game():
    sentences = [
        "Python is fun to learn",
        "I love playing CLI games",
        "Typing speed matters a lot",
        "Command line interface is powerful",
        "Practice makes perfect",
        "Speed typing improves coding skills",
        "Errors slow you down in typing races",
        "Consistency is the key to success",
        "Gamers love competing on the terminal",
        "Learning by doing makes you stronger"
    ]

    print("\n==========================")
    print(" ⌨️ Typing Speed Race ⌨️ ")
    print("==========================\n")
    print("Two players will race by typing the given sentence correctly.\n")

    sentence = random.choice(sentences)
    print(f"👉 Sentence to type:\n\n   \"{sentence}\"\n")

    players = ["Player 1", "Player 2"]
    results = {}

    for player in players:
        input(f"Press Enter when {player} is ready...")

        start_time = time.time()
        typed = input(f"{player}, type here: ")
        end_time = time.time()

        time_taken = round(end_time - start_time, 2)

        if typed.strip() == sentence:
            print(f"✅ Correct! {player} took {time_taken} seconds.\n")
            results[player] = time_taken
        else:
            print(f"❌ Wrong typing! {player} gets disqualified.\n")
            results[player] = float("inf")

    print("\n==========================")
    print(" ⏱️ Race Results ⏱️ ")
    for player, result in results.items():
        if result == float("inf"):
            print(f"{player}: ❌ Wrong typing")
        else:
            print(f"{player}: {result} seconds")
    print("==========================")

    # Decide Winner
    if results["Player 1"] < results["Player 2"]:
        print("🏆 Player 1 Wins!")
    elif results["Player 2"] < results["Player 1"]:
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
