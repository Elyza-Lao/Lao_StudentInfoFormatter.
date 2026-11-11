import string

first_name = str(input("Enter first name: "))
last_name = str(input("Enter last name: "))
section = str(input("Enter section: "))
favorite_subject = str(input("Enter favorite subject: "))

print("\nFormatted Output:")

formatted_name = string.capwords(first_name + " " + last_name)
name_code = (first_name + " " + last_name).upper()
formatted_section = section.upper()
formatted_favorite_subject = string.capwords(favorite_subject)
character_count = len(first_name + last_name)

print("Name:", formatted_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Favorite Subject:", formatted_favorite_subject)
print("Character Count:", character_count)