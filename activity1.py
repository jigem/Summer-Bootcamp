import os

os.system('cls')

word = "summer bootcamp"

#no.1
print(word.title())

#no.2
print(f"{word[0].upper()}{word[1:7]}{word[7:-1]}{word[-1].upper()}")

#no.3
special_letter = "L"
print(f"{special_letter}{word[8:11]}")

#no.4
print(f"{word[12:13].upper()}{word[5:6].upper()}")

#no.5
print(f"{word[11:-1].title()}{word[4:5]}")

#no.6
new = word.replace(" ", "l")
print (new.isalpha())