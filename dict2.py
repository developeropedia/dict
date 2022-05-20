import csv
from csv import DictReader
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
#from nltk.corpus import state_union
# from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
# import csv


file_handle = open("C:/Users/hpwor/Downloads/Nim/looping.csv", "r+")
csv_reader = DictReader(file_handle)
for row in csv_reader:

    row = str(row)

    # custom_sent_tokenizer = PunktSentenceTokenizer(row)
    # custom_sent_tokenizer = sent_tokenize(row)
    # print(custom_sent_tokenizer)
    # tokenized = custom_sent_tokenizer.tokenize(row)

    def process_content():
        try:
            words = nltk.word_tokenize(row)
            #print(words)
            tagged = nltk.pos_tag(words)
            #print(tagged)

            #df = pd.read_csv("C:/Users/Nimra Iqbal/AppData/Local/Programs/Python/python39/looping.csv")
            # df['new_column'] = ""
            # file_handle.write(tagged)
            #df.to_csv("C:/Users/Nimra Iqbal/AppData/Local/Programs/Python/python39/looping.csv", index=False)
            print(tagged)



        except Exception as e:
            print(str(e))


    process_content()

file_handle.close()
