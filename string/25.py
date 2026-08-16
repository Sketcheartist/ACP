s = input("Enter a string: ")


chars = list(set(s))
chars.sort(key=s.count, reverse=True)


if len(chars) > 1:

    print("Second most frequent:", chars[1])

else:

    print("No second character")
