from card import Card
from random import randint

def main():
    n = int(input('How many cards to print? '))
    suits = ['d', 'c', 'h', 's']
    for i in range(n):
        rank = randint(1,13)
        suit_num = randint(0,3)
        suit = suits[suit_num]
        card = Card(rank, suit)
        b_value = card.value()
        print('')
        print(card)
        print('Blackjack value:', b_value)


if __name__=='__main__':
    main()