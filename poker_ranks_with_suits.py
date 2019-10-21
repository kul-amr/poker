from collections import Counter


card_vals = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
suits = ['H','D','C','S']


# get the cards order by val descending
def high_card(cards):

    cards_faces = [d['face'] for d in cards]
    return {'rank':'high-card','weight':1}, sorted(cards_faces,key=lambda k:card_vals[k],reverse=True)


# check if one pair of same value cards exist and return with rest of the cards ordered desc
def one_pair(cards):

    cards_faces = [d['face'] for d in cards]
    counts = Counter(cards_faces)

    card_pairs = [k for k,v in counts.items() if v==2]

    if len(card_pairs) != 1:
        return False, False

    cards_list = [c for c in cards_faces if c != card_pairs[0]]

    return {'rank':'one-pair','weight':2} , card_pairs + sorted(cards_list, key=lambda k:card_vals[k],reverse=True)


# check if two pairs of same value cards exist and return with rest of the cards ordered desc
def two_pairs(cards):

    cards_faces = [d['face'] for d in cards]
    counts = Counter(cards_faces)

    card_pairs = [k for k, v in counts.items() if v == 2]

    if len(card_pairs) != 2:
        return False, False

    cards_list = [c for c in cards_faces if c not in card_pairs]

    return {'rank':'two-pairs','weight':3}, card_pairs + sorted(cards_list, key=lambda k: card_vals[k], reverse=True)


# check if three cards of same value exist and return with rest of the cards ordered desc
def triples(cards):

    cards_faces = [d['face'] for d in cards]
    counts = Counter(cards_faces)

    card_triples = [k for k, v in counts.items() if v == 3]

    if len(card_triples) != 1:
        return False, False

    cards_list = [c for c in cards_faces if c != card_triples[0]]

    return {'rank':'triples','weight':4}, card_triples + sorted(cards_list, key=lambda k: card_vals[k], reverse=True)


# check if all card values in sequence
def straight(cards):

    cards_faces = [d['face'] for d in cards]
    counts = Counter(cards_faces)
    non_uniq_cards = [k for k, v in counts.items() if v != 1]

    if (len(non_uniq_cards) > 0):
        return False, False

    sorted_faces = sorted(cards_faces, key=lambda k: card_vals[k], reverse=True)
    diff_in_elems = [card_vals[sorted_faces[i]] - card_vals[sorted_faces[i - 1]] for i in range(1, len(sorted_faces))]

    if all(diff == -1 for diff in diff_in_elems):
        return {'rank': 'straight', 'weight': 5}, sorted_faces

    return False, False


# check if cards are of same suit
def flush(cards):

    card_suit = cards[0]['suit']

    if all(s==card_suit for s in [card_d['suit'] for card_d in cards[1:] ]):
        return {'rank':'flush','weight':6}, sorted([d['face'] for d in cards],key=lambda k: card_vals[k], reverse=True)

    return False, False


# check if one triple and one pair of same value cards exist and return those
def full_house(cards):

    counts = Counter([d['face'] for d in cards])

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

    return {'rank':'full-house','weight':7}, [card_triple,card_double]


# check if four cards of same value exist and return those
def four_of_a_kind(cards):

    counts = Counter([d['face'] for d in cards])

    card_fours = [k for k,v in counts.items() if v==4 ]

    if len(card_fours) != 1:
        return False, False

    other_card = [k for k,v in counts.items() if k != card_fours[0]]

    return {'rank':'four-of-a-kind','weight':8}, card_fours+other_card


# check if cards are of same suit and values in sequence
def straight_flush(cards):

    card_suit = cards[0]['suit']
    cards_faces = [d['face'] for d in cards]

    counts = Counter(cards_faces)
    non_uniq_cards = [k for k, v in counts.items() if v!=1 ]

    if (len(non_uniq_cards)> 0) or (any(s != card_suit for s in [card_d['suit'] for card_d in cards[1:]])) :
        return False, False

    sorted_faces = sorted(cards_faces,key=lambda k: card_vals[k], reverse=True)
    diff_in_elems = [card_vals[sorted_faces[i]] - card_vals[sorted_faces[i-1]] for i in range(1,len(sorted_faces))]

    if all(diff == -1 for diff in diff_in_elems):
        return {'rank': 'straight-flush', 'weight': 9}, sorted_faces

    return False, False


# check if cards are ten, jack, queen, king and ace of same suit
def royal_flush(cards):

    royal_faces = 'TJQKA'
    card_suit = cards[0]['suit']

    cards_faces = [d['face'] for d in cards]

    for c in royal_faces:
        if cards_faces.count(c) !=1:
            return False, False

    if (all(i in royal_faces for i in cards_faces)) and (all(s==card_suit for s in [card_d['suit'] for card_d in cards[1:]])):
        return {'rank': 'royal-flush', 'weight': 10}, sorted(cards_faces,key=lambda k: card_vals[k], reverse=True)

    return False, False


