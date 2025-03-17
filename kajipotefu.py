arr1 = ['a', 'i', 'o', 'e', 'u']
arr2 = ['k', 'j', 'p', 't', 'f']


def kajipo(text):
    result = []
    for char in text:
        if char in arr1:
            index = arr1.index(char)
            result.append(arr2[index])
        elif char in arr2:
            index = arr2.index(char)
            result.append(arr1[index])
        else:
            result.append(char)
    return ''.join(result)


user_input = input("Enter text: ")


result = kajipo(user_input)

print("Updated text:", result)