'''
Created on Dec 16, 2012

@author: djstrong
'''

class RealEvent(object):
    '''
    classdocs
    '''


    def __init__(self, sprawca, zdarzenie, obiekt, narzedzie, event):
        '''
        Constructor
        '''
        self.event = event
        self.sprawca = sprawca
        self.zdarzenie = zdarzenie
        self.obiekt = obiekt
        self.narzedzie = narzedzie
    
    def __str__(self):
        return " | ".join(map(lambda x: str(", ".join(list(x))), [self.sprawca, self.zdarzenie, self.obiekt, self.narzedzie]))
        
    def value(self):
        v = 0.0
        if len(self.sprawca)>=1:
            v += 1.0 + (len(self.sprawca)-1)*0.01
        if len(self.zdarzenie)>=1:
            v += 1.0 + (len(self.zdarzenie)-1)*0.01
        if len(self.obiekt)>=1:
            v += 1.0 + (len(self.obiekt)-1)*0.01
        if len(self.narzedzie)>=1:
            v += 1.0 + (len(self.narzedzie)-1)*0.01
        return v
    
    def ok(self):
        if self.value()>=3:
            return True
        else:
            return False
        
    def trac(self):
        r = ""
        a = []
        for s in self.event.sprawca:
            if s in self.sprawca:
                a.append("'''" + s + "'''")
            else:
                a.append(s)
        r += ", ".join(a)
        r += ' | '
        
        a = []
        for s in self.event.zdarzenie:
            if s in self.zdarzenie:
                a.append("'''" + s + "'''")
            else:
                a.append(s)
        r += ", ".join(a)
        r += ' | ' 

        a = []
        for s in self.event.obiekt:
            if s in self.obiekt:
                a.append("'''" + s + "'''")
            else:
                a.append(s)
        r += ", ".join(a)
        r += ' | ' 

        a = []
        for s in self.event.narzedzie:
            if s in self.narzedzie:
                a.append("'''" + s + "'''")
            else:
                a.append(s)
        r += ", ".join(a)

        return '* '+r