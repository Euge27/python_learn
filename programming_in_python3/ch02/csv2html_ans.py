#!/usr/bin/env python3

import sys
import xml.sax.saxutils as xmlutil

def main():
  maxwith = 100
  print_start()
  count = 0
  while True:
    try:
      line = input()
      if count == 0:
        color = "lightgreen"
      elif count % 2:
        color = "white"
      else:
        color = "lightyellow"
      print_line(line, color, maxwith)
      count += 1
    except EOFError:
      break;
  print_end()


def print_start():
  print("<table border='1'>")


def print_line(line, color, maxwith):
  print("<tr bgcolor='{0}'>".format(color))
  fields = extract_fields(line)
  for field in fields:
    if not field:
      print("<td></td>")
    else:
      number = field.replace(",", "")
      try:
        x = float(number)
        print("<td aligh='right'>{0:d}</td>".format(round(x)))
      except ValueError:
        field = field.title()
        field = field.replace(" And ", " and ")
        if len(field) <= maxwith:
          field = xmlutil.escape(field)
        else:
          field = "{0} ...".format(
              xmlutil.escape(field[:maxwith]))
        print("<td>{0}</td>".format(field))
  print("</tr>")


def extract_fields(line):
  fields = []
  field = ""
  quote = None
  for c in line:
    if c in "\"'":
      if quote is None:
        quote = c
      elif quote == c:
        quote = None
      else:
        field += c
      continue
    if quote is None and c == ",":
      fields.append(field)
      field = ""
    else:
      field += c
  if field:
    fields.append(field)
  return fields

def print_end():
   print("</table>")


main()
