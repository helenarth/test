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
    return data1

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


def train(data_tr):
    n = 0
    contr = []
    sym_mas = []
    while n < len(data_tr):
          contr.append([0, 0, 0, 0, 0, 0, data_tr[n]['is_spam']])
          tokens1 = nltk.word_tokenize(data_tr[n]['subject']) 
          for i in tokens1:
              if re.search('spam',i) or re.search('SPAM',i):
                 #print n
                 contr[n][0] = +120
                 contr[n][1] = +120
                 contr[n][2] = +120
                 contr[n][3] = +120
                 contr[n][4] = +120
                 contr[n][5] = +120
          #print n
          n = n + 1  
    return contr    

def classif(data_mn, contr1, way_mn):
    n = 0
    f = open('train.txt', 'w')
    contr = []
    sym_mas = []
    while n < len(data_mn):
          contr.append([0, 0, 0, 0, 0, 0, way_mn[n]])
          tokens1 = nltk.word_tokenize(data_mn[n]['subject']) 
          for i in tokens1:
              if re.search('spam',i) or re.search('SPAM',i):
                 #print way_mn[n]
                 contr[n][0] = +120
                 contr[n][1] = +120
                 contr[n][2] = +120
                 contr[n][3] = +120
                 contr[n][4] = +120
                 contr[n][5] = +120
          n = n + 1 
    new_contr_tr = []
    new_contr_mn = []
    n = 0
    while n < len(contr1):
        per = (contr1[n][0] + contr1[n][1] + contr1[n][2] + contr1[n][3] + contr1[n][4] + contr1[n][5]) / 6
        new_contr_tr.append([per, contr1[n][6]])
        n = n + 1
    n = 0
    while n < len(contr):
        per = (contr[n][0] + contr[n][1] + contr[n][2] + contr[n][3] + contr[n][4] + contr[n][5]) / 6
        new_contr_mn.append([per, contr[n][6]])
        n = n + 1
  

    new_contr_tr = sorted(new_contr_tr) 
    #print new_contr_tr
    n = 0
    m = 0
    bool = False
    bool1 = False
    fnd_num = 0
    mer = 0
    gen_mass = []
    osn_mass = []
    while n < len(new_contr_mn): 
          while m < len(new_contr_tr):
                if new_contr_tr[m][0] == new_contr_mn[n][0]:
                   fnd_num = m 
                   break                     
                m = m + 1 
          print fnd_num
          m = 0
          #gen_mass.append((new_contr_tr[fnd_num][1]))
          f.write(str(new_contr_tr[fnd_num][1]) + " " + way_mn[n] + "\n")
          #print gen_mass
          #gen_mass = []
          n = n + 1    
    print new_contr_tr[3463]
    f.close()        
    return osn_mass                                               
mass1 =  train(data_tr)

classif(data_mn, mass1, way_mn)







