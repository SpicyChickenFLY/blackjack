"""
Author: Chow
Create: 2019/05/30
Last Review: 2019/06/01
"""

import deck

class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        if card.face_up:
            self.cards.append(card)
        else:
            self.cards.insert(0, card)
        
    def pop(self):
        return self.cards.pop()

    def drop(self):
        cards = self.cards
        self.cards = []
        return cards

    def check_split_allow(self):
        if len(self.cards) == 2\
            and self.cards[0].value == self.cards[1].value:
            return True

    def calc_total_value(self):
        pass

    def show_down(self):
        for card in self.cards:
            if card.face_up:
                card.flip()

    def show(self, check=False):
        for card in self.cards:
            card.show(check)
            print(' ', end='')
        print('')

class Player:  
    def __init__(self, chips=20, name='player'):
        self.hands = [Hand()]
        self.status = []
        self.chips = chips
        self.bets = 0
        self.name = name

    def split_hand(self, hand_index, card1, card2):
        self.hands[hand_index].show_down()
        self.hands.insert(hand_index + 1, Hand())
        split_card = self.hands[hand_index].pop()
        self.deal_hand(hand_index, card1)
        self.hands[hand_index + 1].add(split_card)
        self.deal_hand(hand_index + 1, card2)
        
    def deal_hand(self, hand_index, card):
        self.hands[hand_index].add(card)

    def drop_hand(self, hand_index):
        return self.hands[hand_index].drop()

    def add_bet(self, price):
        if self.chips > price:
            self.chips -= price
            self.bets += price
            return True
        else:
            return False
    
    def win(self):
        self.chips += self.bets
        self.bets = 0

    def lose(self):
        self.bets = 0

    def command_1(self, hand_index):
        add_bet_allow = self.chips > 0
        split_allow = self.hands[hand_index].check_split_allow()
        command = input(
            "1.surrender, 2.raise_bet:{0}, 3:split:{1}".format(
                add_bet_allow, split_allow
            )
        )
        return command

    def command_2(self):
        pass

    def show_hands(self, check=False):
        for hand_index, hand in enumerate(self.hands):
            print("hands-{0}: ".format(hand_index), end='')
            hand.show(check)

if __name__ == "__main__":
    dealer = Player(40)
    dealer.deal_hand(0, deck.Card(12, 'spade'))
    dealer.deal_hand(0, deck.Card(1, 'spade', True))
    dealer.deal_hand(0, deck.Card(2, 'heart', True))
    dealer.show_hands()