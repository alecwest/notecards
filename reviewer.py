#!/usr/bin/python

from noteparser import NoteParser
import sys

def pause(text = "Press Enter to continue... "):
  if sys.version_info[0] < 3:
    return raw_input(text)
  else:
    return input(text)

class Reviewer():
  def __init__(self, note_cards):
    # note_cards is instance of NoteCards class
    self.note_cards = note_cards
    self.shuffled = False
    self.terms_first = True

  def review(self, shuffled_cards, terms_first):
    self.note_cards.shuffle()

    continue_review = True
    index = 0
    while continue_review:
      print("\n")
      if terms_first:
        print(self.note_cards.get(index, shuffled_cards).get_key())
        # Wait for enter
        pause()
        print(self.note_cards.get(index, shuffled_cards).get_definition())
      else:
        print(self.note_cards.get(index, shuffled_cards).get_definition())
        # Wait for enter
        pause()
        print(self.note_cards.get(index, shuffled_cards).get_key())
      print("\n")
      index += 1
      if index == self.note_cards.size():
        # Ask to restart and reshuffle
        restart = pause("Restart? Y/n: ").lower()
        if restart == 'y':
          index = 0
          reshuffle = pause("Reshuffle? Y/n: ")
          if reshuffle == 'y':
            self.note_cards.shuffle()
        else:
          continue_review = False
