import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

# Gets my username
username = sys.argv[1]

# My user ID: 1243448978

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create Spotify object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

displayName = user['display_name']
followers = user['followers']['total']

# Main loop
while True:
    print()
    print("Welcome to Spotipy " + displayName + "!")
    print("You have: " + str(followers) + " followers.")
    print()
    print("0 - Search for artist")
    print("1 - Exit")
    userInput = input("Your choice: ")
    if userInput == "0":
        print()
        artistQuery = input("Please enter the name of the artist you want to look up: ")

        # Artist information
        searchResult = spotifyObject.search(artistQuery, 1, 0, 'artist')
        artist = searchResult['artists']['items'][0]
        artistID = artist['id']
        genres = []

        # Genre information
        for genre in artist['genres']:
            genres.append(genre)

        # Gets all the artist genres and prints them
        genreMessage = "This artist is known for: "
        iterator = 0
        for i in genres:
            if iterator == len(genres) - 1:
                genreMessage += "and " + str(i) + "."
            else:
                genreMessage += str(i) + ", "
            iterator += 1

        print(genreMessage)

    # Ends the main loop
    elif userInput == "1":
        break

    else:
        userInput = input("Looks like you gave a bad input :( \n"
                          "Please try again: ")



# Branch test

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))