import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_cards):
    scores = sum(list_cards)
    if scores == 21 and len(list_cards) == 2:
        return 0
    if scores > 21 and 11 in list_cards:
        list_cards.remove(11)
        list_cards.append(1)
    return scores


def compare(u_score, c_score):
    if u_score == c_score:
        print("It's a draw")
    elif c_score == 0:
        print("User Looses")
    elif u_score == 0:
        print("User won")
    elif u_score > 21:
        print("User Looses")
    elif c_score > 21:
        print("User won")
    else:
        if u_score > c_score:
            print("User won")
        else:
            print("User loose")


def play_game():
    print(f"{logo}\n")
    user_card = []
    computer_card = []

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    is_game_over = False
    computer_score = -1
    user_score = -1
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your Card's {user_card} And The Current Score: {user_score}")
        print(f"Computer's First Card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Do You Want To Draw Another Card. say 'y' or 'n': ")
            if choice == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your's final card's {user_card} And The Final Score: {user_score}")
    print(f"Computer's Final Hand {computer_card} And The Final Score {computer_score}")

    compare(user_score,computer_score)

    restart = input("Do You Want To Restart the Game? y/n: ")
    if restart == 'y':
        play_game()


play_game()
