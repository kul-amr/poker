import sys

from poker_ranks import *


# compare given two hands
def hand_compare(hand1,hand2):

    if valid_hand(hand1) and valid_hand(hand2):
        rank1, cards1 = get_rank(hand1)
        rank2, cards2 = get_rank(hand2)

        if rank1 and rank2:
            if rank1['weight'] > rank2['weight']:
                print("First hand wins!")
            elif rank1['weight'] < rank2['weight']:
                print("Second hand wins!")
            else:
                for i in range(len(cards1)):
                    if card_vals[cards1[i]] > card_vals[cards2[i]]:
                        print("First hand wins!")
                        return
                    elif card_vals[cards1[i]] < card_vals[cards2[i]]:
                        print("Second hand wins!")
                        return
                print("It's a tie!")
    else:
        print("Invalid hand - check the values passed")


# get the rank of given hand
def get_rank(hand):

    # all rank functions in rank weight sequence
    ranks = [four_of_a_kind, full_house, triples, two_pairs, one_pair, high_card]

    # get rank
    for f_rank in ranks:
        rank, cards = f_rank(hand)

        if rank and cards:
            return rank, cards

    return False, False


# check if the hand has valid values passed
def valid_hand(hand):

    valid = False

    if all(i in card_vals.keys() for i in hand) and len(hand)==5:
        valid = True

    return valid


if len(sys.argv) == 3:
    hand_compare(sys.argv[1],sys.argv[2])
else:
    print("Invalid Argument")
