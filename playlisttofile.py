from gmusicapi import Api
import getpass

api = Api()
username = raw_input("What's the email used: ")
pw = getpass.getpass("What's the password: ")
logged_in = api.login(username,pw)

playlists = api.get_all_playlist_ids()
print playlists

snag = raw_input("Enter the playlist id that you would like to get: ")

playlist_info = api.get_playlist_songs(snag)
xspf = []
for playlist in playlist_info:
	track = "<track><title>" + playlist.get('name') + "</title><creator>" + playlist.get('artist') + "</creator></track>"
	xspf.append(track)
	print "Artist: " + playlist.get('artist')
	print "Album: " + playlist.get('album')
	print "Song: " + playlist.get('name')

title = raw_input("What do you want to name the playlist: ")
filename = raw_input("What do you want to name the file: ")

file = open(filename+'.xspf', 'w')

file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
file.write('<playlist version="1" xmlns="http://xspf.org/ns/0/">\n')
file.write('<title>'+title+'</title>\n')
file.write('<tracklist>\n')
for song in xspf:
	file.write(song.encode('utf-8')+'\n')
file.write('</tracklist>\n')
file.write('</playlist>\n')