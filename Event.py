'''
Created on Dec 12, 2012

@author: djstrong
'''
from RealEvent import RealEvent

class Event(object):
    '''
    classdocs
    '''


    def __init__(self, event_id, sprawca, zdarzenie, obiekt, narzedzie):
        '''
        Constructor
        '''
        self.event_id = event_id
        self.sprawca = set(filter(lambda x: x!='', sprawca.decode('utf8').split(', ')))
        self.zdarzenie = set(filter(lambda x: x!='', zdarzenie.decode('utf8').split(', ')))
        self.obiekt = set(filter(lambda x: x!='', obiekt.decode('utf8').split(', ')))
        self.narzedzie = set(filter(lambda x: x!='', narzedzie.decode('utf8').split(', ')))

    def __str__(self):
        return " | ".join(map(lambda x: str(", ".join(list(x))), [str(self.event_id), self.sprawca, self.zdarzenie, self.obiekt, self.narzedzie]))

    def similarity(self, input):
        l = 0
        for s in [self.sprawca, self.zdarzenie, self.obiekt, self.narzedzie]:
            for word in s:
                if word in input.all_podstawowe:
                    l+=1
                    break
        return float(l)/4
    
    def create_event(self, input):
        return RealEvent(self.sprawca&input.all_podstawowe, self.zdarzenie&input.all_podstawowe, self.obiekt&input.all_podstawowe, self.narzedzie&input.all_podstawowe, self)