#!/usr/bin/env python3

import random

articles = ['the', 'a']
subjects = ['cat', 'dog', 'man', 'woman']
verbs = ['sang', 'ran', 'jumped']
adverbials = ['loudly', 'quietly', 'well', 'badly']

for i in range(5):
  article = random.choice(articles)
  subject = random.choice(subjects)
  verb = random.choice(verbs)
  type = random.randint(0, 1)
  if type == 0:
    adverbial = random.choice(adverbials)
    print(article, subject, verb, adverbial)
  else:
    print(article, subject, verb)
