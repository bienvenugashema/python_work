array = []
x = 0
while x < 5:
    text = input("Enter a text: ").replace(" ", "")
    array.append(f"{text} => {len(text)}")
    x += 1
print(array)