from collections import Counter


card_vals = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}


# get the cards order by val descending
def high_card(cards):

    return {'rank':'high-card','weight':1}, sorted(list(cards),key=lambda k:card_vals[k],reverse=True)


# check if one pair of same value cards exist and return with rest of the cards ordered desc
def one_pair(cards):

    counts = Counter(list(cards))

    card_pairs = [k for k,v in counts.items() if v==2]

    if len(card_pairs) != 1:
        return False, False

    cards_list = [c for c in list(cards) if c != card_pairs[0]]

    return {'rank':'one-pair','weight':2} , card_pairs + sorted(cards_list, key=lambda k:card_vals[k],reverse=True)


# check if two pairs of same value cards exist and return with rest of the cards ordered desc
def two_pairs(cards):

    counts = Counter(list(cards))

    card_pairs = [k for k, v in counts.items() if v == 2]

    if len(card_pairs) != 2:
        return False, False

    cards_list = [c for c in list(cards) if c not in card_pairs]

    return {'rank':'two-pairs','weight':3}, card_pairs + sorted(cards_list, key=lambda k: card_vals[k], reverse=True)


# check if three cards of same value exist and return with rest of the cards ordered desc
def triples(cards):

    counts = Counter(list(cards))

    card_triples = [k for k, v in counts.items() if v == 3]

    if len(card_triples) != 1:
        return False, False

    cards_list = [c for c in list(cards) if c != card_triples[0]]

    return {'rank':'triples','weight':4}, card_triples + sorted(cards_list, key=lambda k: card_vals[k], reverse=True)


# check if one triple and one pair of same value cards exist and return those
def full_house(cards):

    counts = Counter(list(cards))

    if len(counts) != 2:
        return False, False

    card_triple, card_double = None, None

    for k, v in counts.items():
        if v ==3 :
            card_triple = k
        elif v == 2:
            card_double = k

    if card_triple is None or card_double is None:
        return False, False

    return {'rank':'full-house','weight':5}, [card_triple,card_double]


# check if four cards of same value exist and return those
def four_of_a_kind(cards):

    counts = Counter(list(cards))

    card_fours = [k for k,v in counts.items() if v==4 ]

    if len(card_fours) != 1:
        return False, False

    other_card = [k for k,v in counts.items() if k != card_fours[0]]

    return {'rank':'four-of-a-kind','weight':6}, card_fours+other_card