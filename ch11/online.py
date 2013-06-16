line_number = 0

with open('chinese.txt') as file:
  for line in file:
    line_number += 1
    print('{:>4} {}'.format(line_number, line.rstrip()))
