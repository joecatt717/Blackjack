import random

suit = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return str(self.rank) + " of " + str(self.suit)

'''
This code was used to test if the following cards would be printed (Works fine!)
This prints a copy of each instance of Card(), and it gets the value for those cards correctly.

for s in suit:
    for r in rank:
        print(Card(s,r))
        print(Card(s,r).value)

'''

class Deck:

    def __init__(self):
        self.cards = []
        for s in suit:
            for r in rank:
                self.cards.append(Card(s,r))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop(0)

'''
This code was used to test if the deck would be printed (Works fine!)
This creates a new deck "deck"
shuffles the deck
then prints the deck card by card (after shuffled)
then it prints a card that is then removed from the deck...

deck = Deck()
deck.shuffle()
for i in range(len(deck.cards)):
    print(deck.cards[i])
print("---------------------------------------------------------------")
print(deck.deal_one())
'''

class Hand:

    def __init__ (self, name):
        self.name = name
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
        if self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def bust(self):
        if self.value > 21:
            return True
        else:
            return False
            
        
    def print_hand(self):
        x = len(self.cards)
        print(f"{self.name}'s Hand:")
        for i in range(x):
            if self.name == "Dealer" and i == 0:
                print("Hidden Card")
            else:
                print(self.cards[i], self.cards[i].value)
        print("\n")
        if self.name != "Dealer":
            print(f'   Hand Value = {self.value}')
        else:
            print("   Hand Value = Unknown...")

'''
    class Chips:

        def __init__(self):
            self.total = 100
            self.bet = 0
            self.winnings = 0

        def win_bet(self):
            self.total += self.bet
            self.winnings += 1

        def loss_bet(self):
            self.total -= self.bet
            self.winnings += 1
'''


'''
for i in range(len(deck.cards)):
    print(deck.cards[i])
print("---------------------------------------------------------------")
'''

def deal_cards():
    deck = Deck()
    deck.shuffle()
    dealer = Hand("Dealer")
    player = Hand("Player One")
    for i in range(2):
        player.add_cards(deck.deal_one())
        dealer.add_cards(deck.deal_one())

    dealer.print_hand()
    print("-------------------------------------------")
    player.print_hand()

    while dealer.value < 14:
        dealer.add_cards(deck.deal_one())
        if dealer.value > 21:
            dealer.bust = True

    while player.value <= 21:
        player_choice = input("Would you like to hit or stay: ")
        if player_choice[0].lower() == "h":
            player.add_cards(deck.deal_one())
            print("-------------------------------------------")
            player.print_hand()
        elif player_choice[0].lower() == "s":
            break
    
    if player.value > 21:
        print("Player BUST!")
        player.bust = True


    if player.bust == True:
        print("   Dealer Wins!")
        win = False
    elif dealer.bust == True and player.value < 21:
        print("Dealer BUST! \n   Player Wins!")
        win = True
    elif player.value > dealer.value:
        print(f"{player.value} beats {dealer.value}: Player Wins!")
        win = True
        pass
    elif player.value <= dealer.value:
        print(f"{player.value} is less than {dealer.value}: Dealer Wins!")
        win = False
        pass

    return win

PLAY = True
cash = 100

while PLAY == True:
    game_on = input("Would you like to play a round? yes or no...")
    if game_on[0].lower() == "y":
        
        print(f"Your current purse is: {cash}")
        bet = int(input("What would you like to bet: "))

        try:
            while bet > cash or bet <= 0:
                bet = int(input("That was too much... Try again. "))
        except TypeError:
            print("Invalid bet amount")

        win = deal_cards()
        if win == True:
            cash += bet
        elif win == False:
            cash -= bet
    else:
        PLAY = False

    if cash <= 0:
        print("Player is out of money...")
        PLAY = False