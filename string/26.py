s = input("Enter message: ")

shift = int(input("Enter shift: "))


result = ""


for ch in s:

    if ch.isalpha():

        result += chr(ord(ch) + shift)

    else:

        result += ch


print("Encrypted:", result)

