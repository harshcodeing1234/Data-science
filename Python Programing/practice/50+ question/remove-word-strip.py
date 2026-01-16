# Function to remove a word and strip spaces

def removeWord(lst, word):
    # Strip all items first, then remove the given word
    cleanedList = [item.strip() for item in lst if item.strip() != word]
    return cleanedList

# Example usage
words = [" apple ", "banana", " mango ", "apple", "grapes "]
print("Original list:", words)

result = removeWord(words, "apple")
print("After removing 'apple':", result)

