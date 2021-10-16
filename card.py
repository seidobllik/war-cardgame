class Card():
    '''
    Each Card object has a value and a suit.
    '''
    VALID_SUITS = tuple(('\u2660', '\u2661', '\u2662', '\u2663'))
    VALID_VALUES = tuple(('2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'J', 'Q', 'K', 'A'))
    value = ''
    suit = ''

    def __init__(self, value, suit):
        '''
        Use Card.VALID_VALUES and Card.VALID_SUITS to create each card.

            args:
                value (str): A value from VALID_VALUES.
                suit (str): A suit from VALID_SUITS.
            
            returns:
                None
        '''
        if value not in self.VALID_VALUES:
            raise ValueError(f'{value.__repr__()} is not a valid value.')
        if suit not in self.VALID_SUITS:
            raise ValueError(f'{suit.__repr__()} is not a valid suit.')
        self.value = value
        self.suit = suit

    def __str__(self):
        return '{}{}'.format(self.value.rjust(2, ' '), self.suit)
    
    def __eq__(self, other):
        return self.VALID_VALUES.index(self.value) == self.VALID_VALUES.index(other.value)

    def __ne__(self, other):
        return self.VALID_VALUES.index(self.value) != self.VALID_VALUES.index(other.value)

    def __gt__(self, other):
        return self.VALID_VALUES.index(self.value) > self.VALID_VALUES.index(other.value)
    
    def __ge__(self, other):
        return self.VALID_VALUES.index(self.value) >= self.VALID_VALUES.index(other.value)

    def __lt__(self, other):
        return self.VALID_VALUES.index(self.value) < self.VALID_VALUES.index(other.value)

    def __le__(self, other):
        return self.VALID_VALUES.index(self.value) <= self.VALID_VALUES.index(other.value)


if __name__ == '__main__':
    import random
    cards_a = []
    cards_b = []
    print('Testing the creation of many cards.')
    for suit in Card.VALID_SUITS:
        for value in Card.VALID_VALUES:
            cards_a.append(Card(value, suit))
            cards_b.append(Card(value,  suit))
            print(cards_a[-1], cards_b[-1])
    
    print('-'*20)

    random.shuffle(cards_a)
    random.shuffle(cards_b)
    print('Testing the comparison methods.')
    for i in range(len(cards_a)):
        if cards_a[i] > cards_b[i]:
            symbol = '>'
        elif cards_a[i] < cards_b[i]:
            symbol = '<'
        elif cards_a[i] == cards_b[i]:
            symbol = '=='
        else:
            raise Exception(f'{cards_a[i]} and {cards_b[i]} cannot be compared.')
        print(cards_a[i], symbol, cards_b[i])

    print('-'*20)
    print('Testing to see if a invalid card can be created.')
    try:
        bad_card = Card('1', '*')
        print('bad card ', bad_card)
    except ValueError as e:
        print(repr(e))
