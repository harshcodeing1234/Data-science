# Program to store friends' favorite languages

fav_lang = {}  # empty dictionary

for i in range(4):
    name = input(f"Enter friend {i+1} name: ")
    language = input(f"Enter {name}'s favorite language: ")
    fav_lang[name] = language

print("\nFriends and their favorite languages:")
print(fav_lang)
