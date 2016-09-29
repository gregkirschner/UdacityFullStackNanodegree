import webbrowser

class Video():
	""" This class provides a way to store videos (movies, TV shows). """
	def __init__(self, title, duration):
		self.title = title
		self.duration = duration


class Movie(Video): #inherits from Video
	""" This class provides a way to store movie related information. """  
		#__Doc__:  media.Movie.__doc__ can access this comment info directly under class.

	VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']  #Class variable. This can be accessed by the
	              # class itself, i.e. calling "media.Movie.VALID_RATINGS" or by calling it
	              # on a specific movie, i.e. calling "rushmore.VALID_RATINGS".
	              # Global variables should be in caps.

	def __init__(self, title, duration, storyline, poster_image_url, trailer_youtube_url):
		Video.__init__(self, title, duration)  # Uses Video constructor for shared elements
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer)



rush = Movie('Rushmore', 99, 'story of rushmore',
 'poster of rushmore', 'url for rushmore')
print rush.duration

