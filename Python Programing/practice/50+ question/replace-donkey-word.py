# Replace every occurrence of "Donkey" with "#####" in the file "word.txt"
with open("text/word.txt", "r", encoding="utf-8") as f:
    content = f.read()

newcontent = content.replace("donkey", "######")

with open("text/word.txt", "w", encoding="utf-8") as f:
    f.write(newcontent)
