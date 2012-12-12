'''
Created on Dec 12, 2012

@author: djstrong
'''

import csv
from Event import Event
from Text import Text
from Relation import Relation

class Knowledge(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.texts = {}
    
    def import_data(self):
        self.__import_events()
        self.__import_relations()
    
    def __import_events(self):
        with open('events.csv', 'rb') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            
            for row in reader:
                try:    
                    text_id = int(row["notatka"])
                    event_id = int(row["nr"])
                except ValueError:
                    continue
                sprawca = row["sprawca"]
                zdarzenie = row["zdarzenie"]
                obiekt = row["obiekt"]
                narzedzie = row["narzedzie"]
                
                
                if text_id not in self.texts:
                    self.texts[text_id] = Text(text_id)
                
                event = Event(event_id, sprawca, zdarzenie, obiekt, narzedzie)
                self.texts[text_id].add_event(event)
                
    def __import_relations(self):
        with open('relations.csv', 'rb') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            
            for row in reader:
                try:    
                    event_id1 = int(row["nr1"])
                    event_id2 = int(row["nr2"])
                    text_id = int(row["notatka"])
                except ValueError:
                    continue
                rodzaj = row["rodzaj"]
                powiazanie = row["powiazanie"]
                
                if text_id not in self.texts:
                    self.texts[text_id] = Text(text_id)
                
                relation = Relation(event_id1, event_id2, rodzaj, powiazanie)
                self.texts[text_id].add_relation(relation)
                
    def print_knowledge(self):
        for k, v in self.texts.iteritems():
            print k
            for _, v2 in v.events.iteritems():
                print v2
            for _, v2 in v.relations.iteritems():
                print v2
            print
