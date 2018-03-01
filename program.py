from random import randint
from string import punctuation
import sys, os, glob
track_list = glob.glob('drake/*.txt')
"""Creates a track list using a specific path to the drake data holding
all the lyrics. For now, this only works on MattChiang's computer and
would require modifying certain functions on other people's computers"""

def random_song(lst):
	"""Picks a random song from the track list"""
	song = lst[randint(0, len(lst) - 1)]
	return song

def iseven(line_index):
	"""Checks if the line is at the start of a couplet"""
	if line_index % 2 == 0:
		return True
	else:
		return False

def translate(song):
	"""Make the format look nice.
	>>> translate('drake/wutang_forever.txt')
	'Wutang Forever'
	"""
	title = song.split('/')[1]
	title = [word[0].upper() + word[1:] for word in title.split('_')]
	title = ' '.join(title)
	if '.txt' in title:
		title = title.replace('.txt', '')
	return title

def spotify(title): # improvement: create a dictionary
	"""Matches title with Spotify URI key"""
	if title.lower() == 'tuscan leather':
		URI = "spotify:track:4IJ7ZoJ8z8cAIbqYShF3ZZ"
	if title.lower() == 'furthest thing':
		URI = "spotify:track:6cT5orvyKqwghJp6KB9vG0"
	if title.lower() == 'started from the bottom':
		URI = "spotify:track:6V2D8Lls36APk0THDjBDfE"
	if title.lower() == 'wutang forever':
		URI = "spotify:track:6KziiQUOoCmC7Kc7Rv4jar"
	if title.lower() == 'own it':
		URI = "spotify:track:3ptQ2qKjiGOIW1USCFXVtT"
	if title.lower() == 'worst behavior':
		URI = "spotify:track:6oF3Es1YzzmLKjGBfThUvD"
	if title.lower() == 'hold on were going home':
		URI = "spotify:track:14Rcq31SafFBHNEwXrtR2B"
	if title.lower() == 'from time':
		URI = "spotify:track:10VBBaul4zVD0reteuIHM2"
	if title.lower() == 'connect':
		URI = "spotify:track:2cx10hB95ygrUp2RsZW7Oh"
	if title.lower() == 'the language':
		URI = "spotify:track:3Qu5bTS5AvgS0TpeGhQyfc"
	if title.lower() == '305 to my city':
		URI = "spotify:track:1y9g5UW31xBqvOi10tcXGX"
	if title.lower() == 'too much':
		URI = "spotify:track:6kIh5c8x8vzOe6OKW1X59U"
	if title.lower() == 'pound cake paris morton music 2':
		URI = "spotify:track:1HDaPtZuixue2q6VGNRdVO"
	if title.lower() == 'come thru':
		URI = "spotify:track:5CDy1I6rSt6vXdqIb87A6f"
	if title.lower() == 'all me':
		URI = "spotify:track:4kNvYhyl8R6m1vykVkcuBu"
	if title.lower() == 'the motion':
		URI = "spotify:track:30Nz9gLN6DKAk2DIKtE9Oa"
	return URI

def generator():
	"""Generate a random lyric by first checking if the first line
	is the beginning of a couplet. If the line picked happens to be
	the end of the song, then the first line is picked."""
	song = random_song(track_list)
	title = translate(song)
	song_URI = spotify(title)
	text_file = open(song, "r")
	lines = text_file.read().split("\n")
	for line in lines:
		if line == '':
			del lines[lines.index(line)]
	num_lines = len(lines) - 1
	random_line_index = randint(0, num_lines)
	if random_line_index == num_lines: # at the end of the song, so start at the beginning
		intro = lines[0]
		if intro[-1] in punctuation:
			return intro + ' ' + lines[1], ' - ' + title, song_URI
		return intro + ', ' + lines[1], ' - ' + title, song_URI
	first_line = lines[random_line_index]
	next_line = lines[random_line_index + 1]
	if iseven(random_line_index):
		if first_line[-1] in punctuation:
			return first_line + ' ' + next_line, ' - ' + title, song_URI
		return first_line + ", "  + next_line, ' - ' + title, song_URI
	else:
		next_next_line = lines[random_line_index + 2]
		if next_line[-1] in punctuation:
			return next_line + ' ' + next_next_line, ' - ' + title, song_URI
		return next_line + ", " + next_next_line, ' - ' + title, song_URI
