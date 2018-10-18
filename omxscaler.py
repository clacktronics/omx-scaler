from omxplayer.player import OMXPlayer
from sys import argv
from time import sleep

VIDEO_FILE = argv[1]


player = OMXPlayer(VIDEO_FILE, args=['--no-osd'], pause=True)

VIDEO_LOCATION = [0,0,player.width(),player.height()]

print VIDEO_LOCATION

import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''

while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    stdscr.addstr(2, 20, ', '.join(str(x) for x in VIDEO_LOCATION))
    stdscr.addstr(10, 20, ' ')
    
    if key == ord('m'):
	vidx = VIDEO_LOCATION[2] - VIDEO_LOCATION[0]
	vidy = VIDEO_LOCATION[3] - VIDEO_LOCATION[1]
	vidx /= 0.99
	vidy /= 0.99
	VIDEO_LOCATION[2] = VIDEO_LOCATION[0] + int(vidx)
	VIDEO_LOCATION[3] = VIDEO_LOCATION[1] + int(vidy)
        player.set_video_pos(*VIDEO_LOCATION)
    if key == ord('n'):
	vidx = VIDEO_LOCATION[2] - VIDEO_LOCATION[0]
	vidy = VIDEO_LOCATION[3] - VIDEO_LOCATION[1]
	vidx *= 0.99
	vidy *= 0.99
        VIDEO_LOCATION[2] = VIDEO_LOCATION[0] + int(vidx)
        VIDEO_LOCATION[3] = VIDEO_LOCATION[1] + int(vidy)
        player.set_video_pos(*VIDEO_LOCATION)
    if key == curses.KEY_LEFT: 
        stdscr.addstr(3, 20, "LEFT ")
	VIDEO_LOCATION[0] -= 1
	VIDEO_LOCATION[2] -= 1 
	player.set_video_pos(*VIDEO_LOCATION)
    elif key == curses.KEY_RIGHT: 
        stdscr.addstr(3, 20, "RIGHT")
	VIDEO_LOCATION[0] += 1
	VIDEO_LOCATION[2] += 1 
	player.set_video_pos(*VIDEO_LOCATION)
    elif key == curses.KEY_UP: 
        stdscr.addstr(3, 20, "UP   ")
	VIDEO_LOCATION[1] -= 1
	VIDEO_LOCATION[3] -= 1 
	player.set_video_pos(*VIDEO_LOCATION)
    elif key == curses.KEY_DOWN: 
        stdscr.addstr(3, 20, "DOWN ")
	VIDEO_LOCATION[1] += 1
	VIDEO_LOCATION[3] += 1 
	player.set_video_pos(*VIDEO_LOCATION)
else:
    player.quit()
