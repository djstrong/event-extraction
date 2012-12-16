# -*- coding: utf-8 -*-
'''
Created on Dec 12, 2012

@author: djstrong
'''

from Knowledge import Knowledge
from Morfologik import Morfologik
import locale

if __name__ == '__main__':
    
    k = Knowledge()
    k.import_data()
    k.print_knowledge()
    
    m = Morfologik()
    #print m.get("wód")
    #print m.get(u"wód")
    #print m.get("ZĄŁŚÓĆŻ")
    #print m.get("wódczane")
    
    texts=[u"""W inscenizacji bitwy na Polach Grunwaldu zwyciężyły wojska polskie i litewskie. Mimo kontuzji Jagiełły, który spadł z konia, Polakom udało się rozstrzygnąć na swoją korzyść losy bitwy.""",
u"""Na Polach Grunwaldzkich gotowa już jest średniowieczna osada rycerska, w której zamieszka około 2 tysięcy rycerzy z Polski i całej Europy. 14 lipca wezmą oni udział w bitwie, która będzie inscenizacją tej z 1410 roku.""",
u"""Inscenizacja "Braci Karamazow" Dostojewskiego, z którą przyjechał  do Wiednia Krystian Lupa ze Starym Teatrem z Krakowa, zapowiada  się jako "objawienie" - napisała austriacka agencja APA.""",
u"""Operę "Makbet" G.Verdiego przedstawi w niedzielę, w Starym Browarze, zespół Teatru Wielkiego w Poznaniu. Poznańska inscenizacja będzie operowym debiutem reżyserskim dyrektora Teatru STU Krzysztofa Jasińskiego.""",
u"""Premierą "Wesela" Stanisława Wyspiańskiego rozpoczął sezon Teatr Polski w Szczecinie. Reżyserem spektaklu jest twórca "Metra" Janusz Józefowicz. Józefowicz, przygotowując inscenizację jednego z największych dramatów polskich, zapowiadał, że podejmie próbę odpowiedzi na pytanie, czym jest tradycja narodowa.""",
u"""Setnym przedstawieniem "Wesela" Stanisława Wyspiańskiego w inscenizacji olsztyńskiego Teatru im. Stefana Jaracza w sto lat po prapremierze dramatu rozpoczną się w piątek IX Olsztyńskie Spotkania Teatralne, które potrwają do 25 marca.""",
u"""Inscenizacją plenerowego spektaklu "Carmen" Georgesa Bizeta inauguruje nowy sezon Teatr Wielki w Poznaniu. Dyrekcja opery planuje pięć premier. W nowym sezonie poznańska opera będzie klimatyzowana.""",
u"""Wszyscy przetrzymywani od czwartku w Soczi nad Morzem Czarnym zakładnicy zostali uwolnieni przez porywaczy, którzy oddali się w ręce władz. Służby specjalne (FSB) mają "poważne wątpliwości czy rzeczywiście byli to zakładnicy" i uważa, że mogłaby to być "inscenizacja z fałszywymi zakładnikami" - powiedział wiceminister spraw wewnętrznych Władimir Kozłow.""",
u"""Odgrywana po angielsku inscenizacja "Ferdydurke" Witolda Gombrowicza w wykonaniu Teatru Provisorium - Kompanii Teatralnej z Lublina dostała w piątek prestiżową nagrodę "Fringe First" na tegorocznym festiwalu teatralnym w Edynburgu. W uzasadnieniu nagrody, przyznawanej przez krytyków i widzów, podkreślono "nowy język ekspresji i porywającą inscenizację" teatru z Lublina.""",
u"""Chwalony przez teatromanów i recenzentów "Ślub" Witolda Gombrowicza w inscenizacji Waldemara Śmigasiewicza i w wykonaniu aktorów Teatru im. Wojciecha Bogusławskiego zobaczą wkrótce widzowie Zielonej Góry i Łodzi."""]
    for text in texts:
        input = m.podstawowe_formy(text)
        #print input
        #print input.all_podstawowe
        k.fitting_events(input)
        #k.fitting_texts(input)
        print
        
    print 'finished'
