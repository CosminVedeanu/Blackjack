import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value= values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value +=values[card.rank]
        if card.rank == 'Ace':
            self.aces+=1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass


def take_bet():
    pass


def hit(deck, hand):
    pass


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    pass


def show_some(player, dealer):
    pass


def show_all(player, dealer):
    pass


def player_busts():
    pass


def player_wins():
    pass


def dealer_busts():
    pass


def dealer_wins():
    pass


def push():
    pass


while True:
    # Print an opening statement

    # Create & shuffle the deck, deal two cards to each player

    # Set up the Player's chips

    # Prompt the Player for their bet

    # Show cards (but keep one dealer card hidden)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand

        # Show cards (but keep one dealer card hidden)

        # If player's hand exceeds 21, run player_busts() and break out of loop

        break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

        # Show all cards

        # Run different winning scenarios

        # Inform Player of their chips total

        # Ask to play again

    break