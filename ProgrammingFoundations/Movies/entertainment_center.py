import media, fresh_tomatoes

rushmore_story = "An eccentric boy, who loves his school (Rushmore) falls in love with \
a teacher at the school. A battle with his middle-aged mentor breaks out when he finds \
out that he and the teacher are dating."

rushmore = media.Movie('Rushmore', rushmore_story, 
	'http://www.impawards.com/1998/posters/rushmore_ver1.jpg',
	'https://www.youtube.com/watch?v=GxCNDpvGyss')

movies = []

movies.append(rushmore)

## Open Movie website:
#fresh_tomatoes.open_movies_page(movies)

print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__ )
print (media.Movie.__name__)
print (media.Movie.__module__)
print (media.Movie.__dict__)
print (media.Movie.__bases__)  #Classes from which the class inherits

