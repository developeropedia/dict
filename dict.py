import csv
from csv import DictReader
from collections import Counter
import pandas as pd
import nltk
nltk.download('punkt')
#from nltk.corpus import state_union
# from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
# import csv

tagged_file = open('C:/Users/hpwor/Downloads/Nim/tagged.csv', 'w')
writer = csv.writer(tagged_file)

partsOfSpeech = []
partsOfSpeech.append("Tweet")
partsOfSpeech.append("Tagged")

header = []
sentences = []
data = []
final = []
taggedList = []

def process_content(tokenized, field):
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            counts = Counter(tag for word,tag in tagged)
            for c in counts:
                if(c not in partsOfSpeech):
                    partsOfSpeech.append(c)
            data.append((field,counts))
            taggedList.append((field, tagged))



    except Exception as e:
        print(str(e))

file_handle = open("C:/Users/hpwor/Downloads/Nim/looping.csv", "r+")
csv_reader = csv.reader(file_handle)
for row in csv_reader:

    for field in row:
        tokenized = sent_tokenize(field)

        process_content(tokenized, field)

count = 0
for k,d in data:
    output = []
    output.append(k)
    output.append(taggedList[count])
    for p in partsOfSpeech[2:]:
        output.append(d[p])
    final.append(output)
    count = count + 1


writer.writerow(partsOfSpeech)
writer.writerows(final)

file_handle.close()
tagged_file.close()