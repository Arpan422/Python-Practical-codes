name = input("Enter your full name:")
low=name.lower()
print(sum(ord(ch) - 96 for ch in name))
