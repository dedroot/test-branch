print("create commit for testing tags and auto changelog")

try:
    age = int(input("How old are you? : "))
except ValueError:
    print("Enter a valid integer!")
    exit()

if age > 130:
    print("Are you lying?")
    exit()
if age <= 2:
    print("How do you have the permission to use computer?")
    exit()

print(age)
