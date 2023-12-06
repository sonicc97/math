father = input("How old is the father?")
mother = input("How old is the mother?")

print("Father years:", father)
print("Mother years:", mother)

if father > mother:
    print("The father is older!")
elif father < mother:
    print("The mother is older!")
elif father == mother:
    print("They are the same age.")