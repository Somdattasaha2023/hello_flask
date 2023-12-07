def search4vowels(phrase:str)  -> set:
  "Return any vowels found in a supplied phrase"
  vowels = set('aeiou')
  return vowels.intersection(set(phrase))


def search4digits(phrase:str)  -> set:
  "Return any digits found in a supplied word"
  digits = set('0123456789')
  return digits.intersection(set(phrase))


def search4letters(phrase:str,letters:str='aeiou')  -> set:
     vowels = set(letters)
     return vowels.intersection(set(phrase))