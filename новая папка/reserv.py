import codecs
import json
import os
import re
import nltk
 
def read_tr(dir):
    data1 = []
    for file in os.listdir(dir):
        with codecs.open(os.path.join(dir, file), 'r', 'utf-8') as f:
            data1.append(json.load(f))
            # data1['from']
            # data1['to']
            # data1['subject']
            # data1['body']
            # data1['is_spam']
    return data1

def read_mn(dir):
    data2 = []
    for file in os.listdir(dir):
        with codecs.open(os.path.join(dir, file), 'r', 'utf-8') as f:
            data2.append(json.load(f))
            # data_mn['from']
            # data_mn['to']
            # data_mn['subject']
            # data_mn['body']
            # data_mn['is_spam']
    return data2
    
data_tr = read_tr('/home/partizan/classif2/spam_data/train')
data_mn = read_mn('/home/partizan/classif2/spam_data/test')

#print data_mn[1]['body']
#print len(data_tr)

def train(data_tr):
    n = 0
    contr = []
    sym_mas = []
    while n < len(data_tr):
          contr.append([0, False])
          tokens1 = nltk.word_tokenize(data_tr[n]['body']) 
          for i in tokens1:
              if sym_mas.count(i) == 0:
                 kol = tokens1.count(i)
                 sym_mas.append(i)
                 if kol > 12:
                    contr[n][0] = +1
          sym_mass = []
          if data_tr[n] == '':
             contr[n][0] = +10
          try:
            s1 = data_tr[n].split('@')
            b = int(s1[0])
            contr[n][0] = + 5
          except: None
          s1 = data_tr[n]['from'].split('@')
          if len(s1) > 8:
            contr[n][0] = + 1
          if tokens1.count('buy') > 3:
             contr[n][0] = +4
          if tokens1.count('online') > 3:
             contr[n][0] = +4
          if tokens1.count('sell') > 3:
             contr[n][0] = +4
          for i in tokens1:
              s1 = i.split('.')
              try:
                if s1[1] == 'ru' or s1[1] == 'com' or s1[1] == 'net':  
                   contr[n][0] = +5
              except: None
          print n
          n = n + 1
        
    return contr    

print train(data_tr)

