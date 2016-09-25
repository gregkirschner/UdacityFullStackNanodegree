import time, webbrowser, datetime

breaks_needed = 2
break_count = 0
break_hours = 2

break_seconds = break_hours * 60 * 60

print "Program initial time:  {}".format(time.ctime())
while coding and break_count < breaks_needed:
	session = break_count + 1
	print 'New coding session #{} - beginning at {}\n'.format(session, time.ctime())
	time.sleep(break_hours)
	break_count += 1
	webbrowser.open('https://www.google.com/#q=intermission')
	print 'Break #{} @ {}\n\n'.format(break_count, time.ctime())


