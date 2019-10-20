(Uses python3)

Above script compares two poker hands to determine which one wins.
In this version the cards don't have suits and there are no flushes, straights or straight flushes.
The two hands are given as strings of five characters, where each character is one of 23456789TJQKA.
The answer is in format -  "First hand wins!", "Second hand wins!" or "It's a tie!".

A hand wins if it has a more valuable combination than the other or if they have the same combination but
the cards of one are higher than the cards of the other.

combinations could be - four_of_a_kind, full_house, triples, two_pairs, one_pair, high_card


Execution example:

python poker.py AAAQQ QQAAA


IF incorrect values passed in hand or incorrect number of parameters then will print error message.