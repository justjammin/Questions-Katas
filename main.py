vowels = ["a","e","i","o","u",]

Input = "whatever"

for letter in Input:
  if letter in vowels:
    Input=Input.replace(letter,"");
print(Input)

string = "leetcodeisacommunityforcoders"

newstr = string;
print("\nRemoving vowels from the given string");
vowels = ('a', 'e', 'i', 'o', 'u');
for x in string.lower():
    if x in vowels:
        newstr = newstr.replace(x,"");
print("New string after successfully removed all the vowels:");
print(newstr);