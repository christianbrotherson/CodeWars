# My Original Code
# def replace_exclamation(s):
#   vowels = ('a','e','i','o','u')
#   for i in s:
#     if i.lower() in vowels:
#       s = s.replace(i, '!')
#   return s

#Best Practice
def replace_exclamation(s):
  return "".join("!" if i in "aeiouAEIOU" else i for i in s)
