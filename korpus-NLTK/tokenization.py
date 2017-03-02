import sqlite3
import nltk
import re
from nltk.tokenize import MWETokenizer, TweetTokenizer



limit = "limit 5000" #limit number of results
Q_ALL = "select text from scraped order by scraped.date_posted " + limit


con = sqlite3.connect('baza.db')
cur = con.cursor()
cur.execute(Q_ALL)

data = cur.fetchall()
data = [a[0] for a in data]
data_string = " ".join(data) #list of texts to string

#TweetTokenizer
tokenizer = TweetTokenizer(preserve_case=False)
tokens = tokenizer.tokenize(data_string)

#remove punctuation and links from tokens
fil = re.compile('.*[A-Za-z0-9].*')
urls = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

tokens = [w for w in tokens if fil.match(w)]
tokens = [w for w in tokens if not urls.match(w)]

print("All tokens: %d" % len(tokens))
print("Unique tokens: %d" % len(set(tokens)))
print("Lexical diveristy: %f" % (len(set(tokens)) / len(tokens)))
fdist = nltk.FreqDist([t for t in tokens if len(t) > 4])
common = fdist.most_common(20)
fdist_a = nltk.FreqDist(tokens)
common_a = fdist_a.most_common(30)

print('Most common with more than 4 letters')
print(common)
print('-'*20)
print('Most common')
print(common_a)
print('-'*20)

nltktext = nltk.Text(tokens)


nltktext.dispersion_plot(['hvala', 'windows', 'android', 'linux'])

#MWE Tokenizer
mwetok = MWETokenizer([('veliki', 'problem'), ('ne', 'radi'), ('hvala', 'puno')], separator='+')
mwe_tokens = mwetok.tokenize(tokens)

