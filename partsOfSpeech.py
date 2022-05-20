#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

df = pd.read_csv("looping.csv")

file = open("looping.csv","r") #open file
data = file.read() #read all lines

# Count the total word ans sentences
total_wor = data.count(" ")
total_words = int(total_wor) + 1
#print ("\n")

total_sen = data.count(".")
total_sentences = int (total_sen)



sentences = nltk.sent_tokenize(data) #tokenize sentences

word_count_list = []
sentence_count_list = []
verb_count_list = []
noun_count_list = []
adjective_count_list = []
adverb_count_list = []
preposition_count_list = []
punctuation_count_list = []

verb= []#empty to array to hold all parth of speech
noun= []
adj = []
advb=[]
prep=[]
punc=[]


#count the number of verbs

for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'VB' or pos == 'VBD' or pos == 'VBN' or pos == 'VBP'or pos == 'VBZ' or pos == 'VBG'):
             verb.append(word)


print ("These are Verbs : \n" , verb)
verb_count= len(verb)



#count the number of nouns

for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
            noun.append(word)


print ("\nThese are Nouns : \n",noun)
noun_count= len(noun)



#count the number of Adjectives
for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'JJ' or pos == 'JJR' or pos == 'JJS'):
             adj.append(word)


print ("These are Adjectives : \n" , adj)
adj_count= len(adj)

#count the number of Adverbs
for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'RB' or pos == 'RBR' or pos == 'RBS'):
             advb.append(word)


print ("These are Adverbs    : \n" , advb)
adverb_count = len(advb)

#count the number of prepositions
for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
          if (pos == 'IN'):
            prep.append(word)


print ("\nThese are Prepositions : \n",prep)
prepo_count= len(prep)

#count the number of punctuations
for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if (pos == ',' or pos == '?' or pos == '!' or pos == '.'):
            punc.append(word)


print ("\nThese are Punctuations : \n",punc)
punc_count = len(punc)

# print ("\nTotal number of words in this file are  :  ", total_words)
# print ("\nTotal number of sentences in this file are  : ",  total_sentences)
# print("\nTotal number of Verbs are : ", verb_count)
# print("\ntotal NUmber of Nouns are : ", noun_count)
# print("\nTotal number Adjectives are :", adj_count)
# print("\nTotal number Adverbs are : ", adverb_count)
# print("\ntotal NUmber of Prepositions : ", prepo_count)
# print("\ntotal NUmber of Punctuations : ", punc_count)

word_count_list.append(total_words)
sentence_count_list.append(total_sentences)
verb_count_list.append(verb_count)
noun_count_list.append(noun_count)
adjective_count_list.append(adj_count)
adverb_count_list.append(adverb_count)
preposition_count_list.append(prepo_count)
punctuation_count_list.append(punc_count)


# In[6]:


df['Words Count'] = word_count_list
df['Sentences Count'] = sentence_count_list
df['Verb Count'] = verb_count_list
df ['Noun Count'] = noun_count_list
df ['Adjective Count'] = adjective_count_list
df ['Adverb Count'] = adverb_count_list
df ['Preposition Count'] = preposition_count_list
df ['Punctuation Count'] = punctuation_count_list


df.to_csv("file3.csv", index=False)


# In[ ]:




