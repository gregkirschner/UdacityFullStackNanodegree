import urllib

def open_file(file_input):
	text_file = open(file_input)
	contents = text_file.read()
	text_file.close()
	return contents

def check_file(file_input):
	contents = open_file(file_input)
	#Google website that returns "True" of "False" for explitives in a piece of text
	connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=' + contents)
	profane = connection.read()
	connection.close()
	if profane.lower() == 'true':
		print "Profanity alert!"
	else:
		print "You're good to go!"


check_file('profanity_file.txt')