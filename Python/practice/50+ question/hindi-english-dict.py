# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
hindi_dict = {
    "aam": "mango",
    "seb": "apple",
    "kela": "banana",
    "doodh": "milk",
    "paani": "water"
}
print("Available words:", list(hindi_dict.keys()))

word = input("Enter a Hindi word to get its English translation: ").lower()
translation = hindi_dict.get(word)

if translation:
    print(f"The English translation of '{word}' is '{translation}'.")
else:
    print("Sorry, this word is not in the dictionary.")

