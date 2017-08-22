#!/usr/bin/python

class NoteCard():
  def __init__(self, subject, key, definition):
    # assert isinstance(subject, str)
    # assert isinstance(key, str)
    # assert isinstance(definition, str)
    self._subject = subject
    self._key = key
    self._definition = definition

  def get_subject(self):
    return self._subject

  def get_key(self):
    return self._key

  def get_definition(self):
    return self._definition

  def set_subject(self, subject):
    self._subject = subject

  def set_key(self, key):
    self._key = key

  def set_definition(self, definition):
    self._definition = definition

  def display(self):
    print("Subject:    " + self._subject)
    print("Key:        " + self._key)
    print("Definition: " + self._definition)
