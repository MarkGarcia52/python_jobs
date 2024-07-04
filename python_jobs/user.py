# Loop through key-value pairs
# This website is designed to store information about a user

# It would store their username, first name, and last

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
# you can also use it when abbreviated
# for k, v, in user_0.items()
    print(f"\nKey: {key}")
    print(f"Value: {value}")

