'''
Created on Dec 13, 2012

@author: djstrong
'''

import re

class Utils(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def podstawowe_formy(self, text):
        #
        #text = text.decode('utf8').encode('iso-8859-2', 'ignore')
        pattern = r'\w+'
        #locale.setlocale(locale.LC_ALL, "pl_PL")
        #print re.findall(pattern, text, re.LOCALE)
        #print re.findall(pattern, text)
        r = {}
        for w in re.findall(pattern, text, re.UNICODE):
            #w=w.decode('utf8')
            r[w] = set(self.get(w)) | set(self.get(w.lower()))
            #print w, set(self.get(w))
            
        return r