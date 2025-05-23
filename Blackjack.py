import random
import os
import platform

# ANSI styles for color and bold (works in most modern terminals)
BOLD = '\033[1m'
RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'

# ASCII Art Title
art = r'''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/                    
'''

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    print("\n" + "═" * 50)
    if user_score == computer_score:
        return f"{YELLOW}▶ It's a draw! 🙃{RESET}"
    elif computer_score == 0:
        return f"{RED}▶ You lose. Dealer has Blackjack! 😱{RESET}"
    elif user_score == 0:
        return f"{GREEN}▶ You win with a Blackjack! 🃏😎{RESET}"
    elif user_score > 21:
        return f"{RED}▶ You went over. You lose. 💥{RESET}"
    elif computer_score > 21:
        return f"{GREEN}▶ Dealer busts. You win! 🎉{RESET}"
    elif user_score > computer_score:
        return f"{GREEN}▶ You win! 🥳{RESET}"
    else:
        return f"{RED}▶ You lose. Dealer wins. 😤{RESET}"

def print_hand(player, cards, score):
    print(f"{player}'s Hand: {cards} | Score: {score}")

def play_game():
    clear()
    print(CYAN + art + RESET)
    print(f"\n{BOLD}★ WELCOME TO TERMINAL BLACKJACK ★{RESET}")
    print("═" * 50)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print()
        print_hand("👦 Your", user_cards, user_score)
        print(f"🤖 Dealer's First Card: [{computer_cards[0]}]")
        print("\n" + "─" * 50)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input(f"{BOLD}▶ Type 'y' to hit or 'n' to stand: {RESET}").lower()
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Dealer draws cards
    while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    # Final scores
    print("\n" + "═" * 50)
    print_hand("👦 Your", user_cards, calculate_score(user_cards))
    print_hand("🤖 Dealer", computer_cards, calculate_score(computer_cards))
    print("═" * 50)

    # Final result
    print(compare(calculate_score(user_cards), calculate_score(computer_cards)))
    print("═" * 50 + "\n")

# Loop game
while input(f"{BOLD}▶ Do you want to play Blackjack? (y/n): {RESET}").lower() == 'y':
    play_game()
