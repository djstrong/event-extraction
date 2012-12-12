'''
Created on Dec 12, 2012

@author: djstrong
'''

class Event(object):
    '''
    classdocs
    '''


    def __init__(self, event_id, sprawca, zdarzenie, obiekt, narzedzie):
        '''
        Constructor
        '''
        self.event_id = event_id
        self.sprawca = sprawca
        self.zdarzenie = zdarzenie
        self.obiekt = obiekt
        self.narzedzie = narzedzie

    def __str__(self):
        return " | ".join([str(self.event_id), self.sprawca, self.zdarzenie, self.obiekt, self.narzedzie])
