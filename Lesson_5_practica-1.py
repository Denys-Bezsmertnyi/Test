def upper_letters(a):
   return a.lower()
def low_letters(a):
   return a.upper()

words = str(input())
print(''.join(map(low_letters,words)))
print(''.join(map(upper_letters,words)))