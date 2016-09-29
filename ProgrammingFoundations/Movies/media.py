import webbrowser

class Movie():
	""" This class provides a way to store movie related information. """  
		#__Doc__:  media.Movie.__doc__ can access this comment info directly under class.

	VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']  #Class variable. This can be accessed by the
	              # class itself, i.e. calling "media.Movie.VALID_RATINGS" or by calling it
	              # on a specific movie, i.e. calling "rushmore.VALID_RATINGS".
	              # Global variables should be in caps.

	def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer)



