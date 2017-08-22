#!/usr/bin/python

"""

Improvements:
  include all non-colonated lines in a definition, rather than only one line

"""

from noteparser import NoteParser
from reviewer   import Reviewer
import sys

def main(argv):
  note_parser = NoteParser()
  note_cards = note_parser.parse_notes(argv[0]) # Returns NoteCards instance
  # print("YEET\n\n\n")
  # note_cards.print_cards()

  reviewer = Reviewer(note_cards)
  reviewer.review(True, True)
  return

if __name__ == "__main__":
  main(sys.argv[1:])