
is_female = False

if is_female:
    print("You are a female.")
else:
    print("You are not a female")

print("\n")


is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both.")
else:
    print("You are neither a male nor tall")

print("\n")

is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a short male")
else:
    print("You are neither short nor tall")
    