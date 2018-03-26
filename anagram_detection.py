def is_anagram(test, original):
    return True if sorted(test.lower()) == sorted(original.lower()) else False
