"""
Author: Chow
Create: 2019/05/30
Last Review: 2019/06/01
"""

from player import Player
from deck import Deck

def check_player():
    pass

def compare_hands(dealer_hand, player_hand):
    pass

def game():
    '''Check all players and dealer are ready'''
    
    players = [Player(20, 'Alice'), Player(30, 'Bob'),  Player(30, 'Charlie')]
    dealer = Player(70, 'Chow', False)

    deck = Deck(2)
    deck.show(True)

    round_num = 0
    if True:
        '''New round'''
        round_num += 1
        print('Round: {0}'.format(round_num))

        '''Every player devide their bet'''
        for player_index in range(len(players)):
            players[player_index].add_bet(5)
            print(
                'Player-{0} bet {1}\n'.format(
                    players[player_index].name, 
                    players[player_index].bets
                )
            )
        print("Game Start")

        '''Deal card for dealer and each player'''
        for player_index in range(len(players)):
            players[player_index].deal_hand(0, deck.deal(True))
            players[player_index].deal_hand(0, deck.deal())
            print('Player-{0}: '.format(players[player_index].name))
            players[player_index].show_hands(True)
        dealer.deal_hand(0, deck.deal(True))         
        dealer.deal_hand(0, deck.deal())
        print('Dealer-{0}: '.format(dealer.name))
        dealer.show_hands(True)
        print()

        '''Each player make a decision'''
        for player_index in range(len(players)):
            hand_index = 0
            while hand_index < len(players[player_index].hands):
                print('Player-{0}: '.format(players[player_index].name))
                players[player_index].show_hands(True)
                '''Initiate Command'''
                command_1 = players[player_index].command_1(hand_index)
                if command_1 == '1': # surrender
                    print('Surrender')
                    players[player_index].lose()
                    dropped_hand = players[player_index].drop_hand(hand_index)
                    for card in dropped_hand:
                        deck.drop(card)
                    hand_index += 1
                elif command_1 == '2': # raise_bet
                    bet = 5
                    players[player_index].add_bet(bet)
                    print('Raise_bet:{0}'.format(bet))
                elif command_1 == '3': # split
                    print('Split')
                    card1 = deck.deal(True)
                    card2 = deck.deal(True)
                    players[player_index].split_hand(hand_index, card1, card2)

                elif command_1 == '4': # pass
                    print('Pass')
                    hand_index += 1
                else:
                    print('Do it again')

        '''Each player make a decision'''
        for player_index in range(len(players)):
            hand_index = 0
            while hand_index < len(players[player_index].hands):
                print('Player-{0}: '.format(players[player_index].name))
                players[player_index].show_hands(True)            
                command_2 = players[player_index].command_2(hand_index)
                if command_2 == '1': # Hit
                    print('Hit')
                    players[player_index].deal_hand(hand_index, deck.deal(True))
                    players[player_index].show_hands(True)
                    if players[player_index].hands[hand_index].calc_total_value() == 22:
                        print('Blast')
                        players[player_index].lose()
                        dropped_hand = players[player_index].drop_hand(hand_index)
                        for card in dropped_hand:
                            deck.drop(card)
                        hand_index += 1
                        
                elif command_2 == '2': # Stop
                    print('Stop')
                    hand_index += 1
                    
                else:
                    print('Do it again')

        '''Dealer make a decision '''
        while dealer.hands[0].calc_total_value() < 17:
            dealer.deal_hand(0, deck.deal(True))
        if dealer.hands[0].calc_total_value() == 22:
            dealer.lose()
    
if __name__ == "__main__":
    game()


