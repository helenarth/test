import codecs
import json
import os
import re
import nltk
import numpy as np
 
def read_tr(dir):
    data1 = []
    way_tr = []
    for file in os.listdir(dir):        
        with codecs.open(os.path.join(dir, file), 'r', 'utf-8') as f:
            data1.append(json.load(f))       
            way_tr.append(file)     
    return data1, way_tr

def read_mn(dir):
    data2 = []
    way_mn = []
    for file in os.listdir(dir):
        with codecs.open(os.path.join(dir, file), 'r', 'utf-8') as f:
            data2.append(json.load(f))
            way_mn.append(file)
    return data2, way_mn
    
data_tr = read_tr('/home/partizan/classif2/spam_data/train')
data_mn, way_mn = read_mn('/home/partizan/classif2/spam_data/test')


def train(data_tr, way_tr, data_mn, way_mn):
    n = 0
    vect_tr = []
    vect_mn = []
    while n < len(data_tr):
          vect_tr.append([0, 0, 0, data_tr[n]['is_spam']])
          tokens = nltk.word_tokenize(data_tr[n]['subject']) 
          for i in tokens:
              if re.search('spam',i) or re.search('SPAM',i):
                 vect_tr[n][0] = vect_tr[n][0] +20
              if re.search('Re', i):
                 vect_tr[n][1] = vect_tr[n][1] -20
              if re.search('CLICK', i) or re.search('click', i):
                 vect_tr[n][2] = vect_tr[n][2] +20
          n = n + 1  
    n = 0
    while n < len(data_mn):
          vect_mn.append([0, 0, 0, way_mn[n]])
          tokens = nltk.word_tokenize(data_mn[n]['subject']) 
          for i in tokens:
              if re.search('spam',i) or re.search('SPAM',i):
                 vect_mn[n][0] = vect_mn[n][0] +20
              if re.search('Re', i):
                 vect_mn[n][1] = vect_mn[n][0] -20 
              if re.search('CLICK', i) or re.search('click', i):
                 vect_tr[n][2] = vect_tr[n][2] +20              
          n = n + 1  
    #print way_mn
    return vect_tr, vect_mn 

def classif(vect_tr, vect_mn):
    f = open('test.txt','w')
    n = 0
    m = 0
    num_mass = []
    num = 0
    sorted(vect_tr)
    while (n < len(data_mn)):
          koaf = 0         
          while (m < len(data_tr)):
                iter = np.sqrt((vect_tr[m][0] - vect_mn[n][0])**2 + (vect_tr[m][1] - vect_mn[n][1])**2 + (vect_tr[m][2] - vect_mn[n][2])**2)
                if (m == 0):
                   koaf = iter
                   num = m
                else:
                   if iter < koaf:
                      koaf = iter
                      num = m
                m = m + 1
          col_tr = 0
          col_fl = 0
          try:
            if vect_tr[num - 1][3] == True: 
               col_tr = col_tr + 1
            else:
               col_fl = col_fl + 1
          except: print 1
          try:
            if vect_tr[num + 1][3] == True: 
               col_tr = col_tr + 1
            else:
               col_fl = col_fl + 1
          except: print 1
          if vect_tr[num][3] == True:
             col_tr = col_tr + 1
          else:
             col_fl = col_fl + 1
          if col_fl > col_tr:
             f.write(u'%s\t%s\n' % (way_mn[n], False))
          else:
             f.write(u'%s\t%s\n' % (way_mn[n], True))
          print col_fl, col_tr
          num_mass = []
          m = 0
          n = n + 1
    f.close()

data_tr, way_tr = read_tr('/home/partizan/classif2/spam_data/train')
data_mn, way_mn = read_mn('/home/partizan/classif2/spam_data/test')

print len(data_tr), " ", len(way_tr)
print len(data_mn), " ", len(way_mn)

vect_tr, vect_mn = train(data_tr, way_tr, data_mn, way_mn)
classif(vect_tr, vect_mn)


