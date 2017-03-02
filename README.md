# SNCL
Scrapy NLTK Corpus-Linguistics

Odabrane kompentente praktičnog dijela završnog rada. Radi veličine izostavljena je baza podataka i izrađeni korpusi.<br>
Za prikupljanje podataka koristi se <a href="http://scrapy.org/">Scrapy</a> i <a href="https://developers.facebook.com/docs/graph-api">Graph API</a><br>
Za izradu korpusa, analizu i klasifikaciju <a href="http://www.nltk.org/">Natural Language Toolkit</a><br>
Rad je obuhvatio proces izrade i analize korpusa. Prikupljanje tekstova neformalne komunikacije koristeći Facebook API i skrejpanjem 
(web scraping) foruma bug.hr/forum. Na tekstovima su primjenjene korpusne tehnike za normalizaciju i ostale lingvističke metode. Korištenje korpusa demonstrirano je kroz automatsku klasifikaciju teksta koristeći naivni Bayesov klasifikator.

Jednostavni dijagram sustava:<br><br>
<img src="https://raw.githubusercontent.com/franraknic/sncl/master/dijagram.png" width="400" height="250"><br><br>
Primjer grafiranja pojavljivanja nekih riječi u tekstu:<br><br>
<img src="https://raw.githubusercontent.com/franraknic/sncl/master/dispersion.png" width="700" height="400"><br><br>
