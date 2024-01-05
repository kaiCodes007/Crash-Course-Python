"""
City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
"Santiago, Chile". Call your function with at least three city-country pairs, and print thevalues that are returned.
"""
def city_country(city,country):
	message = f'"{city.title()}, {country.title()}"'
	return message

print(city_country('kathmandu','nepal'))
print(city_country('dhaka','bangladesh'))
print(city_country('dublin','ireland'))


"""
Write a function called make_album() that builds a dictionary describing a music album.Take an artist name and an album title 
It should return a dictionary containing these two pieces of information. Use the function
to make three dictionaries representing different albums. Print each return value
"""

def make_album(artist_name,album_name):
	album_detail = {'artist':artist_name, 'album':album_name}
	return album_detail

print('')
print(make_album('queens','a night at the opera'))
print(make_album('ac/dc','black in black'))
print(make_album("g n' roses",'appetite for destruction'))


"""
User Albums: Start with your program from above. Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include 
a quit value in the while loop
"""

def make_album(artist_name,album_name):
	album_detail = {'artist':artist_name,'album':album_name}
	return album_detail


while True:
	print("\nPlease enter the album details")
	print("Press q anytime to exit")

	artist = input("Please enter the artist name: ")

	if artist == 'q' :
	    break
	    
	album = input("Please enter the album name: ")

	if album == 'q': 
	    break   
	
	album_description = make_album(artist,album)
	print(album_description)	

	