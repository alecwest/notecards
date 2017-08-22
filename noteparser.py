#!/usr/bin/python

from notecards import NoteCards
from notecard  import NoteCard
import re
import pprint

class NoteParser():
  def __init__(self):
    # Notes will be parsed into note_tree
    self.note_tree = []
    # Once parsed, all notes will be added to notecards
    self.note_cards = NoteCards()
    self.content = None

  def print_notes(self):
    pp = pprint.PrettyPrinter(indent=4)
    pprint.pprint(self.note_tree)
    # while not self.note_cards.is_empty():
    #   self.note_cards.remove_index(0, False).display()

  def parse_notes(self, text_file):
    def remove_tabs(element):
      return element.replace("    ", "\t").replace("\t", "")

    def add_to_note_cards(subject, key, definition):
      card = NoteCard(subject, key, definition)
      return self.note_cards.add_card(card)

    def append_to_note_tree(note_tree, element, path, has_colon):
      curr_location = note_tree[0]
      # Iterate through path to find element's proper location
      for key in path[1:]:
        # Iterate through current location's children to find next location
        for each in curr_location[1]:
          # Once found, update current location
          if each[0] == key:
            curr_location = each
      # Once path is complete, append element to array of children
      curr_location[1].append(element)
      # Add to note cards if path length is 2+ (has subject and at least one path element to be the key)
      if len(path) > 1 and not has_colon:
        # Format to add to note_cards
        subject = path[0]
        key = ' > '.join(path[1:])
        add_to_note_cards(path[0], key, element)

    def parse(note_tree, notes, parent, path, tab_depth):
      if len(notes) == 0:
        return note_tree

      # Get next line to parse
      next_line = notes[0]
      del notes[0]
      # Get subject for card (Should be first line of file)
      subject = path[0]

      # Get number of tabs to compare to previous line's depth
      next_tab_depth = len(next_line) - len(next_line.lstrip("\t"))
      depth_difference = tab_depth - next_tab_depth

      # Delete elements from path if next_line has fewer tabs 
      if depth_difference > 0:
        for i in range(depth_difference):
          del path[len(path) - 1]

      if re.search(":\s*$", next_line):
        # Get key for card 
        key = remove_tabs(next_line).replace(":", "").rstrip()
        # Create tuple containing key and empty array to be filled recursively
        next_element = (key, [])
        # Add element to parent tuple's array
        append_to_note_tree(note_tree, next_element, path, True)
        # Add element's key to path array
        path.append(key)
        return parse(note_tree, notes, next_element, path, next_tab_depth + 1)
      else:
        next_line = remove_tabs(next_line)
        # TODO: MAKE THIS WORK
        # full_definition = ""
        # while not re.search(":\s*$", next_line):
        #   full_definition += remove_tabs(next_line) + "\n"
        #   next_line = notes[0]
        #   del notes[0]
        #   if len(notes) == 0:
        #     break
        append_to_note_tree(note_tree, next_line, path, False)
      return parse(note_tree, notes, parent, path, next_tab_depth)

    ###### BEGIN PARSE FUNCTION ######
    # Reset values each time parse is called
    self.note_tree = []
    self.note_cards = NoteCards()
    self.content = None
    with open(text_file, 'r') as txt:
      self.content = txt.read()
      # print(self.content)

    # Split by line and remove all empty lines
    notes = [line.replace("\n", "") for line in self.content.split("\n") if line.strip() != ""]
    # Declare head tuple
    key = notes[0].replace(":", "").rstrip()
    head = (key, [])
    # Initialize path. First line is expected to have a colon at the end
    path = [remove_tabs(key)]
    del notes[0]

    # Add first node to note_tree so a parent element exists
    self.note_tree.append(head)
    try:
      self.note_tree = parse(self.note_tree, notes, self.note_tree[0], path, 0)
      return self.note_cards
    except IndexError as e:
      print(e)
      print("Check your notes...you may be missing some colons.") 

