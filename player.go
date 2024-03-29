package blackjack

type Player struct {
}

type Player struct {
	name string
	Player
	hands []*Hand
	bets 
	chips
}
func NewPlayer(name string, chips int) *Player {
	return &Player{
		name: name,
		chips: chips,
	}
}
    func (p *Player) dealHand( handIdx int, card *Card) {
        p.hands[handIdx].add(card)
	}

    func (p *Player) dropHand( handIdx int) {
        cards = p.hands[handIdx].drop()
        p.hands.pop(handIdx)
        return cards
	}
	func (p*Player) showHands(check bool) {
		for handIdx, hand := range p.hands {
			fmt.Print(handIdx)
			hand.show(check)
		}
	}


type BlackJackPlayer struct {
	Player

}

    func NewBlackJackPlayer( chips int,  name string) *BlackJackPlayer {
		return &BlackJackPlayer{
			Player: *NewPlayer(name,chips),
		} 
	}
        self.join_game(5)
        
    def join_game(self, price):
        if self.new_bet(0, price):
            self.hands.insert(0, Hand_BlackJack())

    def raise_bet(self, hand_index, price):
        if self.chips >= price:
            self.chips -= price
            self.bets[hand_index] += price

    def new_bet(self, hand_index, price):
        if self.chips > price:
            self.chips -= price
            self.bets.insert(hand_index, price)
            return True
        else:
            return False

    def split_hand(self, hand_index, card1, card2, bet):
        self.hands[hand_index].show_down()
        self.hands.insert(hand_index + 1, Hand_BlackJack())
        split_card = self.hands[hand_index].pop()
        self.deal_hand(hand_index, card1)
        self.hands[hand_index + 1].add(split_card)
        self.deal_hand(hand_index + 1, card2)
        self.new_bet(hand_index + 1, bet)

    def win(self, hand_index):
        self.chips += self.bets[hand_index]
        bet = self.bets.pop(hand_index)
        dropped_hand = self.drop_hand(hand_index)
        return dropped_hand, bet

    def lose(self, hand_index):
        bet = self.bets.pop(hand_index)
        dropped_hand = self.drop_hand(hand_index)
        return dropped_hand, bet

    def initial_command(self, hand_index):
        surrender_allow = True
        add_bet_allow = self.chips > 0
        split_allow = self.hands[hand_index].check_split_allow()
        pass_allow = True
        while True:
            command = input(
                "1.Surrender:{0}, 2.Raise_bet:{1}, 3:Split:{2}, 4:Pass:{3}\n".format(
                    surrender_allow, add_bet_allow, split_allow, pass_allow
                )
            )
            # default 4
            if (surrender_allow and command == '1') \
                or (add_bet_allow and command == '2') \
                or (split_allow and command == '3') \
                or (pass_allow and command == '4'):
                break
        return command

class Dealer_BlackJack(BlackJackPlayer):
    def __init__(self, chips=20, name='player'):
        super().__init__(chips, name) 
        self.hold_game()

    def hold_game(self):
        self.bets.insert(0, 0)
        self.hands.insert(0, Hand_BlackJack())

    def win(self, bet):
        self.chips += bet

    def lose(self, bet):
        self.chips -= bet


if __name__ == "__main__":
    from deck import Card
    dealer = Dealer_BlackJack(40, 'Chow')
    dealer.deal_hand(0, Card(12, 'spade'))
    dealer.deal_hand(0, Card(1, 'spade', True))
    dealer.deal_hand(0, Card(2, 'heart', True))
    dealer.show_hands()
