'''
Created on Dec 13, 2012

@author: djstrong
'''

import cPickle as pickle
import re
import locale
from InputText import InputText

class Morfologik(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        try:
            pkl_file = open('morfologik.pkl', 'rb')
            self.slownik = pickle.load(pkl_file)
            pkl_file.close()
        except IOError:
            self.slownik = {}
            f = open("morfologik.txt")
            for line in f:
                line = line.rstrip()
                #print line
                line = line.decode('utf8').encode('iso-8859-2', 'ignore')
                odmieniona, podstawowa, znaczniki = line.split('\t')
                if odmieniona not in self.slownik:
                    self.slownik[odmieniona] = [podstawowa]
                else:
                    self.slownik[odmieniona].append(podstawowa)
            f.close()
            
            output = open('morfologik.pkl', 'wb')
            pickle.dump(self.slownik, output, -1)
            output.close()

    def get_unicode(self, slowo):
        slowo = slowo.encode('iso-8859-2', 'ignore')
        return self.get_iso(slowo)

    def get_utf8(self, slowo):
        slowo = slowo.decode('utf8')
        return self.get_unicode(slowo)
    
    def get_iso(self, slowo):
        if slowo not in self.slownik:
            return []
        return self.list_to_unicode(self.slownik[slowo])

    def list_to_unicode(self, lista):
        return map(lambda x: x.decode('iso-8859-2'), lista)

    def podstawowe_formy(self, text):
        # text in unicode
        input = InputText(text)
        #text = text.decode('utf8').encode('iso-8859-2', 'ignore')
        pattern = r'\w+'
        #locale.setlocale(locale.LC_ALL, "pl_PL")
        #print re.findall(pattern, text, re.LOCALE)
        #print re.findall(pattern, text)
        r = {}
        for w in re.findall(pattern, text, re.UNICODE):
            #w=w.decode('utf8')
            r[w] = set(self.get_unicode(w)) | set(self.get_unicode(w.lower()))
            #print w, set(self.get(w))
            
        input.set_podstawowe(r)
        return input