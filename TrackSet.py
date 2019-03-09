#----------------------------------------------------------------------
#!/usr/bin/env python
# Shannon Stasek
# Mario Kart Tournament
#----------------------------------------------------------------------

import random

#----------------------------------------------------------------------

class TrackSet:

    '''class for representing a list of of Mario Kart 8 Tracks 0 through 47'''

    #------------------------------------------------------------------

    def __init__(self):
        
        '''create the list of tracks in MK8 0 through 47'''
        
        self.init()

    #------------------------------------------------------------------
    
    def init(self):

        '''sets the list of tracks numbered 0 through 47 and sets the
            top track to 47'''
        
        self.tracks = list(range(48))
        self.topTrack = 47

    #------------------------------------------------------------------

    def selectOne(self):

        '''returns the number corresponding to the next track and updates
        the list; returns c, the track number'''

        mario_track = random.randint(0, self.topTrack)
        c = self.tracks[mario_track]
        self.tracks.pop(mario_track)
        self.topTrack -=1
        return c

        

#----------------------------------------------------------------------
