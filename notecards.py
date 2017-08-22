#!/usr/bin/python
from notecard import NoteCard
import random

class NoteCards():
  def __init__(self):
    self.cards = []
    self.shuffled_cards = []

  def get_subject(self):
    return self.cards[0].get_subject()

  # Method does not reshuffle cards.
  def set_subject(self, subject):
    old_subject = self.cards[0].get_subject()
    for card in self.cards:
      card.set_subject(subject)
    for card in self._shuffledcards:
      card.set_subject(subject)
    return old_subject

  def size(self):
    return len(self.cards)

  # def get_cards(self):
  #   return self.cards

  def get(self, index, shuffled):
    if shuffled:
      return self.shuffled_cards[index]
    else:
      return self.cards[index]

  def printcards(self):
    for card in self.cards:
      card.display()

  def add_card(self, notecard):
    if (self.size() > 0):
      if (self.get_subject() != notecard.get_subject()):
        # Card should not be added to collection of a different subject
        return -1  
    self.cards.append(notecard)
    # Return position of newly added card
    return (len(self.cards) - 1)

  def remove_index(self, index):
    if (len(self.cards) - 1 < index):
      return None
    card_to_remove = self.cards[index]
    del self.cards[index]
    return card_to_remove

  def remove_key(self, key):
    for card in self.cards:
      if card.get_key() == key:
        card_to_remove = card
        del self.cards[self.cards.index(card)]
        return card_to_remove
    return None

  def shuffle(self):
    self.shuffled_cards = random.sample(self.cards, self.size())

