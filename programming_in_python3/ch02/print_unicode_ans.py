#!/usr/bin/env python3

import sys
import unicodedata

def print_unicode_table(words):
  print("decimal   hex   chr   {0:^40}".format("name"))
  print("-------   ---   ---   {0:-<40}".format(""))

  code = ord(" ")
  end = min(0xD800, sys.maxunicode)

  while code < end:
    c = chr(code)
    name = unicodedata.name(c, "*** unknown ***")
    if len(words) == 0 or word_in_unicode_table(words, name):
      print("{0:7}  {0:5X}  {0:^3c}  {1}".format(
        code, name.title()))
    code += 1

def word_in_unicode_table(words, name):
  for word in words:
    if word.lower() not in name.lower():
      return False
  return True

words = []
if len(sys.argv) > 1:
  if sys.argv[1] in ("-h", "--help"):
    print("usage: {0} [stringlist]".format(sys.argv[0]))
    words = None
  else:
    words = sys.argv[1:]
if words != None:
  print_unicode_table(words)
