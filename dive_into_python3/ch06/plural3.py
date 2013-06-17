import re

def build_match_and_apply_functions(pattern, search, replace):
  def matches_rule(word):
    return re.search(pattern, word)

  def apply_rule(word):
    return re.sub(search, replace, word)

  return (matches_rule, apply_rule)

patterns = \
 (
     (match_sxz, apply_sxz),
     (match_h, apply_h),
     (match_y, apply_y),
     (match_default, apply_deault)
  )

 rules = [build_match_and_apply_functions(pattern, search, replace)
     for (pattern, search, replace) in patterns]

 def plural(noun):
   for matches_rule, apply_rule in rules:
     if matches_rule(noun):
       return apply_rule(noun)
