'''
Created on Dec 13, 2012

@author: djstrong
'''

class InputText(object):
    '''
    classdocs
    '''


    def __init__(self, text):
        '''
        Constructor
        '''
        self.text = text
        
    def set_podstawowe(self, podstawowe):
        self.podstawowe = podstawowe
        self.all_podstawowe=set()
        for k,v in podstawowe.iteritems():
            self.all_podstawowe.add(k)
            self.all_podstawowe.update(v)
