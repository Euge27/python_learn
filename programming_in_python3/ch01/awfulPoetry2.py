#!/usr/bin/env python3

import random

lines = input('input lines (1~10)')
if not lines:
  raise ValueError('input a number')

try:
  lines = int(lines)
except ValueError as err:
  raise err

if not 1 <= lines <= 10:
  raise ValueError('lines must between 1 and 10')

articles = ['the', 'a']
subjects = ['cat', 'dog', 'man', 'woman']
verbs = ['sang', 'ran', 'jumped']
adverbials = ['loudly', 'quietly', 'well', 'badly']

for i in range(lines):
  article = random.choice(articles)
  subject = random.choice(subjects)
  verb = random.choice(verbs)
  type = random.randint(0, 1)
  if type == 0:
    adverbial = random.choice(adverbials)
    print(article, subject, verb, adverbial)
  else:
    print(article, subject, verb)
