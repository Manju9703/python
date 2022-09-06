vowels = 'aeiou'

a =input("enter the sentence")

a = a.casefold()

count = {}.fromkeys(vowels,0)
for char in a:
   if char in count:
       count[char] += 1
print(count)
