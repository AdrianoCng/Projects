import random

money = 100

# Check if the bet amount is valid
def check_bet(bet_amount):
    if (money < bet_amount):
        print("You don't have enough money");
        return False;
    if (bet_amount <= 0):
        print("Your bet must be atleast 1");
        return False;



def flip_coin(bet_amount, choice):
    check_bet(bet_amount);
    num = random.randint(1, 2);
    guess = choice.lower();
    face = "heads" if num == 1 else "tails";

    print("You flip a coin: it's " + face + "!");
    if (guess == face):
        print("You have chosen " + guess + " and you win " + str(bet_amount)+ "\n");
        return bet_amount;
    else:
        print("You have chosen " + guess + " and you lose " + str(bet_amount)+ "\n");
        return bet_amount * -1;


def play_cho_han(bet_amount, choice):
    check_bet(bet_amount);
    dice1 = random.randint(1, 6);
    dice2 = random.randint(1, 6);
    total = dice1 + dice2;
    guess = choice.lower();
    target = "even" if total % 2 == 0 else "odd";

    print("you roll the dice and the total is " + str(total));
    if (guess == target):
        print("You have chosen " + guess + " you win " + str(bet_amount) + "\n");
        return bet_amount;
    else:
        print("You have chosen " + guess + " you lose " + str(bet_amount) + "\n");
        return bet_amount * -1;


def pick_card(bet_amount):
    check_bet(bet_amount);
    # Build a deck
    suit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
    deck = [suit, suit, suit, suit];

    # Player pick a random card from the deck
    suit_index_player = random.randint(0, 3);
    card_index_player = random.randint(0, 12);
    player_card = deck[suit_index_player].pop(card_index_player);

    # Opponent pick a random card from the deck
    suit_index_computer = random.randint(0, 3);
    card_index_computer = random.randint(0, (len(deck[suit_index_computer]) - 1));  # we need deck[suit] length because if we draw from the same suit as the player our card index could be out of range
    computer_card = deck[suit_index_computer].pop(card_index_computer);

    print("You pick " + str(player_card) + " and your opponent pick " + str(computer_card));
    if (player_card > computer_card):
        print("You win " + str(bet_amount) + "\n");
        return bet_amount;
    elif (player_card == computer_card):
        print("It is a tie" + "\n");
        return 0;
    else:
        print("You lose " + str(bet_amount) + "\n");
        return bet_amount * -1;


# Player can bet on red/black || even/odd || first/second/third dozen || the number
def play_roulette(bet_amount, choice):
    check_bet(bet_amount);
    red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36];
    black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35];
    first_dozen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
    second_dozen = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24];
    third_dozen = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36];
    
    # We need to create a wheel if we want more realistic odds because of the double 00
    wheel = [00, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36];
    winning_number = wheel[random.randint(0, 37)];

    is_even = (choice == "even" and winning_number % 2 == 0);
    is_odd = (choice == "odd" and winning_number % 2 != 0);
    is_red = (choice == "red" and winning_number in red_numbers);
    is_black = (choice == "black" and winning_number in black_numbers);
    is_first_dozen = (choice == "first dozen" and winning_number in first_dozen);
    is_second_dozen = (choice == "second dozen" and winning_number in second_dozen);
    is_third_dozen = (choice == "third dozen" and winning_number in third_dozen);
    is_outside_bet = (choice == "red" or choice == "black" or choice == "odd" or choice == "even");
    

    print("You bet " + str(bet_amount) + " on " + str(choice));
    print("the winning number is " + str(winning_number));

    # This if block is not necessary but it's useful to display more information about the winning number
    if (winning_number in red_numbers):
        print("red");
    if (winning_number in black_numbers):
        print("black");
    if (winning_number % 2 == 0 and winning_number != 0):
        print("even");
    if (winning_number % 2 != 0):
        print("odd");

    # Determine if the player wins and pays out depending on the bet
    if (winning_number == 0 and int(choice) != 0):   # We need to check this first because we don't want to pay out if the player bets on even
        if (is_outside_bet):
            print("Your outside bet lose half. You lose " + str(bet_amount/2) + "\n");
            return (bet_amount / 2) * -1;
        print("You lose " + str(bet_amount) + "\n");
        return bet_amount * -1;
    elif (is_red or is_black or is_even or is_odd):
        print("You win " + str(bet_amount) + "\n");
        return bet_amount;
    elif (is_first_dozen or is_second_dozen or is_third_dozen):
        print("You win " + str(bet_amount * 2) + "\n");
        return bet_amount * 2;
    elif (choice == winning_number):
        print("You win " + str(bet_amount * 35) + "\n");
        return bet_amount * 35;
    else:
        print("You lose " + str(bet_amount) + "\n");
        return bet_amount * -1;
        


#Call your game of chance functions here
money += flip_coin(15, "tails");
money += play_cho_han(10, "even");
money += pick_card(25);
money += play_roulette(10, "even");
print(money);