import nltk
import re
import pandas as pd
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.corpus import stopwords

# to lemmatize a word 
def lemma(input_txt):
            def wordnet_pos(pos_tag):
            
                '''Tags for the words in articles '''
                '''Used for lemmatizer '''
                if pos_tag.startswith('J'):
                    return wordnet.ADJ
                elif pos_tag.startswith('V'):
                    return wordnet.VERB
                elif pos_tag.startswith('N'):
                    return wordnet.NOUN
                elif pos_tag.startswith('R'):
                    return wordnet.ADV
                else:
                    return wordnet.NOUN

      
            pos_tags = pos_tag(nltk.word_tokenize(input_txt))

            #lemmatizer(grouping together the different forms of a word so there could be analyzed as a single item)
            input_txt = [WordNetLemmatizer().lemmatize(t[0], wordnet_pos(t[1])) for t in pos_tags]

            return ' '.join(input_txt)

          
def preprocess():
    
    data['preprocessed'] = data['desc']
    
    #convert string to lower case
    data.loc[:,'preprocessed'] = data.loc[:,'preprocessed'].str.lower()
    
    #remove punctuations 
    data['preprocessed'] = data['preprocessed'].map(lambda x: re.sub('[,\.!?]', '', x))

if __name__ == '__main__':
  #load the data
  data=pd.read_json('clubs.json')
  
  #preprocess the data
  preprocess()
  
  #saved the preprocessed data in json format
  data.to_json('clubs_preprocessed.json')

  
