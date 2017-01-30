import webbrowser

class Movie():
	""" This class provides info related to movies """
	VALID_RATINGS = ["G","PG","PG-13","R"]
	def __init__(self, movie_title, movie_storyline, movie_poster_url, movie_youtube_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_url = movie_poster_url
		self.youtube_url = movie_youtube_url
		
	def show_trailer(self):
		webbrowser.open(self.youtube_url)