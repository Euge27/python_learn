#!/usr/bin/env python3

import sys
import xml.sax.saxutils as xmlutil

def main(args):
  ft = process_options(args)
  if ft[0] is None:
    return
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
      print_line(line, color, ft)
      count += 1
    except EOFError:
      break;
  print_end()


def print_start():
  print("<table border='1'>")


def print_line(line, color, ft):
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
        if len(field) <= int(ft[0]):
          field = xmlutil.escape(field)
        else:
          field = "{0} ...".format(
              xmlutil.escape(field[:ft[0].ft[1]]))
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

def process_options(argv):
  maxwith = 100
  format = ".0f"
  if len(argv) > 1 and argv[1] in ("-h", "--help"):
    print("{} maxwith=<int> format=<format>".format(argv[0]))
    return None, None
  else:
    for arg in argv[1:]:
      if arg.startswith(maxwith):
        try:
          maxwith = int(arg[len(maxwith):])
        except valueError:
          pass
      elif arg.startswith(format):
        format = arg[len(format):]
  return maxwith, format


main(sys.argv)
