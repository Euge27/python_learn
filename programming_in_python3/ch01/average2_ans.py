#!/usr/bin/env python3

numbers = []
count = 0
sum = 0
lowest = None
highest = None

while True:
  try:
    str = input('enter a number or Enter to finish:')
    if not str:
      break;
    digit = int(str)
    numbers.append(digit)
    count += 1
    sum += digit
    if lowest is None or digit < lowest:
      lowest = digit
    if highest is None or digit > highest:
      highest = digit
  except ValueError as err:
    print('not a number')
    continue

if count > 0:
  print('numbers:{}'.format(numbers))
  print('count = {} sum = {} lowest = {} highest = {} mean = {}'.format(count, sum, lowest, highest, sum/count))
