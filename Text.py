'''
Created on Dec 12, 2012

@author: djstrong
'''

class Text(object):
    '''
    classdocs
    '''


    def __init__(self, text_id):
        '''
        Constructor
        '''
        self.text_id = text_id
        self.events = {}
        self.relations = {}
    
    def __str__(self):
        return " | ".join([str(self.text_id), str(self.events), str(self.relations)])
    
    def add_event(self, event):
        self.events[event.event_id] = event
        
    def add_relation(self, relation):
        self.relations[(relation.event_id1, relation.event_id2)] = relation
