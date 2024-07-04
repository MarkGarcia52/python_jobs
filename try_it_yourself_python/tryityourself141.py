# Write a function called city_country()
#   That takes in the name of a city and its country
#       Return a string formatted like this:
#           Santiago, Chile

# Call function with atleast three city country pairs and print values returned

def city_country (city, country):
    """Print city and country of three places"""
    place = f"{city}, {country}"
    return place.title()

location = city_country('santiago', 'chile')
print(location)
location = city_country('new York', 'new York')
print(location)
location = city_country('guatemala', 'guatemala')
print(location)

# Write a function called make_album() that builds a dictionary
#   describing a music album
#       The function should take in an artist name an an album title
#           and it should return a dictionary containing these two pieces of
#               information. Use the function to make three dictionaries
#                   representing different albums

# Print each return value to show that the dictionaries are storing the album 
#   Information correctly

def make_album(artist_name, album_title, number_songs=None):
    """Print a music album with artist name and title"""
    if number_songs:
        album = (f" Your favorite album is {album_title.title()} " 
            f"by {artist_name.title()} and it has {number_songs.title()} songs total.")
    else:
        album = (f" Your favorite album is {album_title.title()} " 
            f"by {artist_name.title()}")
    return album

song = make_album('nirvana', 'nevermind', '7')
print(song)

song = make_album('N.W.A', 'straight outta compton')
print(song)

song = make_album('kendrick lamar', 'to pimp a butterfly')
print(song)

# Start with your program artist and title

# Write a while loop that allow users to enter an album's artist and title

def make_album():
    """Print a music album with artist name and title"""
    
while True:
    print("\nPlease tell me your favorite artist and title, with amount of songs")
    print("(enter 'q' at any time to quit)\n")

    artist = input("Name your favorite artist: ")
    if artist == 'q':
        break

    title = input("Name the title: ")
    if title == 'q':
        break

    song = input("How many songs: ")
    if song == 'q':
        break

    album = print(f"\nYour favorite artist is: {artist}")
    album = print(f"Your favorite title is: {title}")
    album = print(f"The album contains: {song} songs")
        
    