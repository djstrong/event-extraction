'''
Created on Dec 12, 2012

@author: djstrong
'''

class Relation(object):
    '''
    classdocs
    '''


    def __init__(self, event_id1, event_id2, rodzaj, powiazanie):
        '''
        Constructor
        '''
        self.event_id1 = event_id1
        self.event_id2 = event_id2
        self.rodzaj = rodzaj
        self.powiazanie = powiazanie
        
    def __str__(self):
        return " | ".join([str(self.event_id1), str(self.event_id2), self.rodzaj, self.powiazanie])
