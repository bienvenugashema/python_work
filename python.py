# word =input("Enter a word: ")
# print(len(word))

# words = input("Enter your words: ").replace(" ", "")
# print(len(words))
# print(words)


array = []
x = 0
words = input("Enter five words words: ").split()
if len(words) != 5:
    print("You must enter five words")
else:    
    for word in words:
        array.append(f"{word} => {len(word)}")
print(array)

