lucky_numbers = [4, 3, 9, 12, 22, 55]
friends = ["Omolola", "Adelore", "Stephanie", "Dorcas", "Don"]

print(friends)
print("\n")

print(friends.index("Dorcas"))
print("\n")

print(friends.count("Omolola"))
print("\n")

friends.sort()
print(friends)
print("\n")

lucky_numbers.sort()
print(lucky_numbers)
print("\n")

friends.append("Oluwatosin")
print(friends)
print("\n")

friends.extend(lucky_numbers)
print(friends)
print("\n")

friends2 = friends.copy()
print(friends2)
print("\n")

friends.insert(1, "Titilope")
print(friends)
print("\n")

friends.pop()
print(friends)
print("\n")

friends.remove("Stephanie")
print(friends)
print("\n")

friends.clear()
print(friends)
print("\n")

