from card import Card
import random


class Deck():
    '''
    The Deck object holds many cards, and allows for the cards to be randomly drawn (to simulate drawing the top card),
    as well as for cards to be returned to the deck.
    '''
    cards = []

    def __init__(self, cards=None):
        '''
        A Deck can be initialized to a full deck based on Card.VALID_VALUES and Card.VALID_SUITS if no cards argument 
        is passed, or can be initialized to any size by using a list of existing cards.

            args:
                cards (list): A list of pre-existing Card objects. 
            
            returns:
                None
        '''
        self.cards = []
        if cards != None:
            for card in cards:
                self.cards.append(Card(card.value, card.suit))
        else:
            for suit in Card.VALID_SUITS:
                for value in Card.VALID_VALUES:
                    self.cards.append(Card(value, suit))

    def __len__(self):
        return len(self.cards)
    
    def shuffle(self):
        '''
        Shuffles the deck.

            args:
                None
            
            returns:
                None
        '''
        random.shuffle(self.cards)

    def draw_card(self):
        '''
        Removes the card at index zero from the deck.

            args:
                None

            returns:
                Card object that was removed from the deck.
        '''
        card = self.cards.pop(0)
        return Card(card.value, card.suit)

    def return_card(self, card):
        '''
        Returns a Card object to end of the Deck.

            args:
                card (Card): The Card object to be returned to the Deck.
            
            returns:
                None
        '''
        if not isinstance(card, Card):
            raise TypeError(f'{card} is not of Type Card.')
        self.cards.append(Card(card.value, card.suit))


if __name__ == '__main__':
    print('Testing the creation on multiple decks.')
    deck_a = Deck()
    deck_b = Deck()
    deck_c = Deck()
    for i in range(len(deck_a)):
        print(deck_a.cards[i], deck_b.cards[i], deck_c.cards[i])

    print('-'*20)
    print('Testing the creation of a deck using pre-existing cards.')
    cards = []
    for value in Card.VALID_VALUES:
        for suit in Card.VALID_SUITS:
            cards.append(Card(value, suit))
    random.shuffle(cards)
    deck_d = Deck(cards[:26])
    deck_e = Deck(cards[26:])
    for i in range(len(deck_d)):
        print(deck_d.cards[i], deck_e.cards[i])

    print('-'*20)
    print('Testing the ability to draw and return cards.')
    for i in range(5):
        card = deck_d.draw_card()
        deck_e.return_card(card)
    for i in range(31):
        print('' if i >= len(deck_d) else deck_d.cards[i], '' if i >= len(deck_e) else deck_e.cards[i])
