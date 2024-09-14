from art import logo
from random import choice


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def calculate_score(cards):
    score = sum(cards)

    if score == 21 and len(cards) == 2:
        return 0

    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

    return score


def compare(users_score, computers_score):
    if users_score == computers_score:
        print("It's a draw!")
    elif computers_score == 0:
        print("Computer got a blackjack! You lose! :(")
    elif users_score == 0:
        print("You got a blackjack! You win! :)")
    elif users_score > 21:
        print("You went over 21. You lose!")
    elif computers_score > 21:
        print("Computer went over. You win!")
    elif computers_score > users_score:
        print("You lose!")
    else:
        print("You win!")


def blackjack_game():
    print(logo)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            break
        else:
            continue_playing = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if continue_playing == 'y':
                user_cards.append(deal_card())
            elif continue_playing == 'n':
                break
            else:
                print("Invalid choice!")
                break

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, final score: {user_score}")
    print(f"Computer cards: {computer_cards}, final score: {computer_score}")
    compare(user_score, computer_score)


while input("Do you want to play a game of Blackjack? Type 'y' to start playing: ").lower() == 'y':
    print("\n" * 100)
    blackjack_game()
