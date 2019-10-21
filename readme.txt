(Uses python3)


Version 1 (without suit):

    Script poker.py compares two poker hands to determine which one wins.
    In this version, the cards don't have suits and there are no flushes, straights or straight flushes.

    The two hands are given as strings of five characters, where each character is one of 23456789TJQKA.
    The answer is in format -  "First hand wins!", "Second hand wins!" or "It's a tie!".

    A hand wins if it has a more valuable combination than the other or if they have the same combination but
    the cards of one are higher than the cards of the other.

    combinations/rank of a hand could be - four_of_a_kind, full_house, triples, two_pairs, one_pair, high_card


    Execution example:

    python poker.py AAAQQ QQAAA


    IF incorrect values passed in hand or incorrect number of parameters then will print error message.
    

========================================================================================================================

Version 2 (with suit):

    Script poker_with_suits.py compares two poker hands to determine which one wins.
    In this version, the cards have suits and combinations like flushes, straights or straight flushes exist.

    The two hands are given as strings of ten characters- distributed as five pairs separated by a space- each pair is
    a face value and a suit, where each face value is one of 23456789TJQKA and suit is one of 'H','D','C','S'.

    The answer is in format -  "First hand wins!", "Second hand wins!" or "It's a tie!".

    A hand wins if it has a more valuable combination than the other or if they have the same combination but
    the cards of one are higher than the cards of the other.

    Combinations/rank of a hand could be -

    royal-flush     => cards are ten, jack, queen, king and ace of same suit,
    straight-flush  => cards are of same suit and values in sequence,
    four_of_a_kind  => four cards of same value,
    full_house      => one triple and one pair of same value cards,
    flush           => cards are of same suit,
    straight        => all card values in sequence,
    triples         => three cards of same value,
    two_pairs       => two pairs of same value cards,
    one_pair        => one pair of same value cards,
    high_card       => cards order by val descending


    Execution example:

    python poker_with_suits.py '3C JC 5C TC 9C' '4H 6D AD 9H 9D'


    IF incorrect values passed in hand or incorrect number of parameters then will print error message.
