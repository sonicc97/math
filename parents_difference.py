def my_max (a, b):
    return a if a > b else b
def my_min (a, b):
    return a if a < b else b

father_years = float(input("Enter father's age:"))
mother_years = float(input("Enter mother's age"))
older = my_max(father_years, mother_years)
younger = my_min(father_years, mother_years)
difference = older - younger

print("Older parents has:", older , "and the younger parents has:", younger)
print("Age difference =", difference)
