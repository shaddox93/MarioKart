#----------------------------------------------------------------------
#!/usr/bin/env python
# Shannon Stasek
# Mario Kart Tournament
#----------------------------------------------------------------------

from TrackSet import *
from Button import *
from graphics import *

#----------------------------------------------------------------------

def drawKart(filename, x, y, window):

    '''draw image specified by filename centered at (x, y) in window'''

    p = Point(x, y)
    prefixes = ['tracks/', '../tracks/', './']
    for prefix in prefixes:
        fname = '{}{}'.format(prefix, filename)
        try:
            image = Image(p, fname)
            image.draw(window)
            return image
        except:
            pass

#----------------------------------------------------------------------

def trackInfo(trackNumber):

    '''returns the filename for the specified mario kart track

    each cup has 4 tracks with 12 cups total, represented below
    by the cups variable
    
    filename is of the form: ##s.gif
    where ## is a two digit number (leading 0 if less than 10)
    and s is a letter corresponding to the track cup'''

    # calculate suit and face numbers
    cupNum = trackNumber // 4
    cupTrackNum = trackNumber % 4

    # calculate name of file
    # face is a number from 1 to 13 with leading zeros for 1-9
    cups = 'mftphblegrcv'
    filename = '{:>02}{}.gif'.format(cupTrackNum + 1, cups[cupNum])
    return filename

#----------------------------------------------------------------------

def createWindow():
    
    win = GraphWin('Mario Tournament 2: Electric Boogaloo', 800, 800)
    win.setBackground('light blue')
    return win
    
#----------------------------------------------------------------------

def drawLogoStart(win):
    
    logo = drawKart("startLogo.gif", 400, 400, win)
    win.getMouse()
    logo.undraw()
    
#----------------------------------------------------------------------

def drawKartStart(win):

    header = Text(Point(400, 25), 'Mario Tournament 2: Electric Boogaloo')
    header.setStyle("bold")
    header.setSize(18)
    header.draw(win)
    
    quitButton = Button(win, Point(725, 750), 80, 40, 'Quit')
    quitButton.activate()
    trackButton = Button(win, Point(625, 750), 90, 40, 'Next Round')
    startButton = Button(win, Point(525, 750), 80, 40, 'Start')
    startButton.activate()
    
    x = win.getMouse()
    while not startButton.clicked(x):
        x = win.getMouse()
    
    startButton.deactivate()

    track = Text(Point(100, 75), 'Round 1 Track List:')
    track.setStyle("bold")
    track.draw(win)

    return quitButton, trackButton

#----------------------------------------------------------------------
    
def drawFourTracks(d, startx, y, win):
    
    for i in range(0, 4):
        c = d.selectOne()
        filename = trackInfo(c)
        drawKart(filename, startx, y, win)
        startx += 200

#----------------------------------------------------------------------
    
def main():

    win = createWindow()
    
    drawLogoStart(win)
    
    quitButton, trackButton = drawKartStart(win)
    trackButton.activate()
    
    d = TrackSet()

    # display initial 4 tracks for round 1
    drawFourTracks(d, 100, 150, win)

    # setting variable amounts for next tracks
    currentRound = 2
    yval = 310
    ytext = 235
    
    # wait for button click to draw 3 additional rounds including final round
    while currentRound <= 5:
        y = win.getMouse()
        if trackButton.clicked(y) and currentRound <=4:
            if currentRound <4:
                track = Text(Point(100, ytext), 'Round ' + str(currentRound) + ' Track List:')
                track.setStyle("bold")
                track.draw(win)
            else:
                track = Text(Point(100, ytext), 'FINAL ROUND!')
                track.setStyle("bold")
                track.draw(win)
                trackButton.deactivate()
            drawFourTracks(d, 100, yval, win)
            yval += 160
            ytext += 160
            currentRound+=1
        elif quitButton.clicked(y) and currentRound <=5:
            break
            
    win.close()
    
main()
