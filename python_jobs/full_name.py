first_name = "Ada"
last_name = "Lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = "You are the coolest!"
print(f"Hello, {full_name.title()}")
print(message)
    
print("Python")
print("\tPython")


nostartch_url = 'https://nostartch.com'
print(nostartch_url.removeprefix('https://'))

#If you like the new value with pre-fix removed, either reassign it to original variable or assign it to a new variable

simple_url = nostartch_url.removeprefix('https://')
print(simple_url)