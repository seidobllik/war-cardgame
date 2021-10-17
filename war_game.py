from deck import Deck


class War():
    '''
    The card game War consists of two players. Both players start with 26
    cards in their hand. Each turn is called a battle. For each battle,
    both players discard the top card in their hand, and the player with
    the higher value card wins, and takes both cards. If the two cards are
    equal in value, the players start a war, in which they both discard three
    cards, then battle with the fourth card. The winner of that battle takes
    all of the discarded cards. If there is another tie, another war is
    started, and the process continues until there is a winner. If a player
    runs out of cards during a war, the last card is played in the battle.

    The game ends when one player has no more cards. 
    '''
    deck = None
    deck_size = 0
    player_one = None
    player_two = None
    discard_pile = None
    battle_count = 0
    war_count = 0

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.deck_size = len(self.deck)
        self.player_one = Deck([])
        self.player_two = Deck([])
        self.discard_pile = Deck([])
        while len(self.deck) > 0:
            self.player_one.return_card(self.deck.draw_card())
            self.player_two.return_card(self.deck.draw_card())
        self.battle_count = 0
        self.war_count = 0
    
    def reset(self):
        '''
        Resets the game.

            args:
                None
            
            returns:
                None
        '''
        self.__init__()
    
    def war(self):
        '''
        Deals 3 cards into the discard pile per player.

            args:
                None
            
            returns:
                None
        '''
        self.war_count += 1
        cards_to_sacrifice = 3
        while cards_to_sacrifice > 0:
            player_one_sacrifice = '---'
            player_two_sacrifice = '---'
            if len(self.player_one) > 1:
                self.discard_pile.return_card(self.player_one.draw_card())
                player_one_sacrifice = '###'
            if len(self.player_two) > 1:
                self.discard_pile.return_card(self.player_two.draw_card())
                player_two_sacrifice = '###'
            cards_to_sacrifice -= 1
            print(f'{player_one_sacrifice}  ~~~~~  {player_two_sacrifice}')
    
    def battle(self):
        '''
        Discards one card per player, and finds the winner between the two cards.

            args:
                None
            
            returns:
                None
        '''
        self.battle_count += 1
        player_one_card = self.player_one.draw_card()
        player_two_card = self.player_two.draw_card()
        winner_index = None
        if player_one_card > player_two_card:
            winner_index = 0
        elif player_one_card < player_two_card:
            winner_index = 1
        elif player_one_card == player_two_card:
            winner_index = 2
        else:
            raise Exception(f'There was no winner between {player_one_card} and {player_two_card}')
        winner = [self.player_one, self.player_two, self.discard_pile][winner_index]
        print(f'{player_one_card}  <--->  {player_two_card}')
        print('-{}--{}--{}-'.format('win' if winner == self.player_one else '---',
                                    'WAR' if winner == self.discard_pile else '----',
                                    'win' if winner == self.player_two else '---'))
        for card in [player_one_card, player_two_card]:
            winner.return_card(card)
        return winner
    
    def play(self):
        '''
        Starts the game, and displays the winner.

            args:
                None

            returns:
                None
        '''
        while (len(self.player_one) < self.deck_size and
               len(self.player_two) < self.deck_size):
            battle_victor = self.battle()
            if battle_victor == self.discard_pile:
                self.war()
                # If the last battle was a tie, but it used the last card in a players hand, 
                # return that card to their hand to be used in the next battle. This immitates
                # the game mechanic of a player having no more cards, so the last card that player
                # played is used until a player wins.
                if len(self.player_one) == 0:
                    self.player_one.return_card(self.discard_pile.cards.pop(-2))
                if len(self.player_two) == 0:
                    self.player_two.return_card(self.discard_pile.cards.pop(-1))
            else:
                while len(self.discard_pile) > 0:
                    battle_victor.return_card(self.discard_pile.draw_card())
                    battle_victor.shuffle()
            if self.battle_count % self.deck_size == 0:
                # To avoid infinite games, shuffle the cards regularly.
                self.player_one.shuffle()
                self.player_two.shuffle()
        
        game_winner = {self.player_one: 'Player 1', self.player_two: 'Player 2'}[battle_victor]

        print('#'*15)
        print(f'{game_winner} wins'.center(15))
        print('#'*15)
        print('info'.center(15, '-'))
        print(f'Total battles: {self.battle_count}')
        print(f'Total wars: {self.war_count}')
        print('-'*15)


if __name__ == '__main__':
    game = War()
    game.play()