import random

def play_game():
    secret_number = random.randint(1, 50)
    print("\n==========================")
    print(" 🎮 Number Guessing Duel 🎮")
    print("==========================\n")
    print("Secret number is between 1 and 50!")
    print("Each player takes turns (1 guess each turn).\n")

    players = ["Player 1", "Player 2"]
    guesses = { "Player 1": [], "Player 2": [] }
    scores = {}

    max_rounds = 3  # total turns per player
    round_icons = ["🔵", "🟢", "🟣", "🟡", "🔴"]  # icon list for rounds

    for round_num in range(1, max_rounds + 1):
        icon = round_icons[(round_num - 1) % len(round_icons)]
        print(f"\n===== {icon} Round {round_num} {icon} =====")
        
        for player in players:
            guess = int(input(f"{player}, enter your guess: "))
            guesses[player].append(guess)

            if guess == secret_number:
                print(f"🎯 Perfect! {player} guessed the number!")
                print(f"\n✅ Secret Number was: {secret_number}")
                print(f"🏆 {player} Wins!")
                return
            elif guess < secret_number:
                print("📉 Too Low!")
            else:
                print("📈 Too High!")

    # If no one guessed exactly, decide winner by closest guess
    for player in players:
        closest = min(guesses[player], key=lambda x: abs(x - secret_number))
        scores[player] = abs(closest - secret_number)

    print("\n==========================")
    print(f"✅ Secret Number was: {secret_number}")
    print("==========================")

    if scores["Player 1"] < scores["Player 2"]:
        print("🏆 Player 1 Wins!")
    elif scores["Player 1"] > scores["Player 2"]:
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
