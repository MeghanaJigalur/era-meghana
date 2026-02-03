name = input("Enter your name: ")
age = input("Enter your current age: ")
# Type casting (string → integer)
age = int(age)
# Calculate age in 2030 (2026 → 2030 = +4 years)
new_age = age + 4
# Output result
print("Hey", name + ", you will be", new_age, "years old in 2030!")