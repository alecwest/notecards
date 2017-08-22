#!/usr/bin/python

import unittest
import sys
sys.path.append('../')
from notecard import NoteCard
from notecards import NoteCards
from noteparser import NoteParser
# from node import Node
# from tree import Tree

class TestNoteCards(unittest.TestCase):
  def setUp(self):
    # Setup for cards and notecards
    self.my_collection = NoteCards()
    self.card1 = NoteCard("CSC", "UnitTest", "Essential to testing code.")
    self.card2 = NoteCard("CSC", "Python", "A neat language.")
    self.card3 = NoteCard("CSC", "Java", "A neat language that I should probably focus on more...")
    self.my_collection.add_card(self.card1)
    self.my_collection.add_card(self.card2)
    self.my_collection.add_card(self.card3)

    # Setup for nodes and trees


  def test_create_card(self):
    card = NoteCard("CSC", "UnitTest", "Essential to testing code.")
    self.assertEqual('CSC', card.get_subject())
    self.assertEqual('UnitTest', card.get_key())
    self.assertEqual('Essential to testing code.', card.get_definition())

  def test_add_cards_to_notecards(self):
    bad_card = NoteCard("NOTCSC", "Card", "Won't be added to my_collection")
    good_card = NoteCard("CSC", "Card", "Will be added to my_collection")
    self.assertFalse(self.my_collection.is_empty())
    self.assertEqual(-1, self.my_collection.add_card(bad_card))
    self.assertEqual(3, self.my_collection.add_card(good_card))

  def test_remove_cards_from_notecards(self):
    self.assertEqual(self.card1, self.my_collection.remove_key("UnitTest"))
    self.assertEqual(None, self.my_collection.remove_index(4))
    self.assertEqual(self.card3, self.my_collection.remove_index(1))
    self.assertEqual(self.card2, self.my_collection.remove_index(0))
    self.assertEqual(None, self.my_collection.remove_index(0))

  def test_shuffle_populates_shuffled_cards(self):
    self.assertEqual(3, len(self.my_collection.shuffle()))

  def test_note_parser_reads_file(self):
    return

  # # Tests for nodes and trees
  # def test_add_children_nodes_to_node(self):
  #   parent_content = ("Key", "Definition")
  #   parent = Node(parent_content)
  #   child1 = Node(("Child1", "Child def"))
  #   child2 = Node(("Child2", "Child def"))
  #   child3 = Node(("Child3", "Child def"))
  #   self.assertFalse(parent.set_content("Not a tuple"))
  #   self.assertEqual(parent_content, parent.get_content())
  #   self.assertTrue(parent.set_content(("Tuple","Will pass")))
  #   self.assertEqual(("Tuple", "Will pass"), parent.get_content())
  #   self.assertEqual(0, parent.number_children())
  #   self.assertEqual(0, parent.add_child(child1))
  #   self.assertEqual(1, parent.number_children())
  #   self.assertEqual(1, parent.add_child(child2))
  #   self.assertEqual(2, parent.add_child(child3))
  #   self.assertEqual(child2, parent.get_child(1))
  #   self.assertEqual(child2, parent.remove_child(1))
  #   self.assertEqual([child1, child3], parent.get_children())



if __name__ == '__main__':
  unittest.main()