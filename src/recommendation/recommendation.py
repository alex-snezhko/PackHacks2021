from flask import Flask, json, request
import json

#lemmatization
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet


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
          
 
#create a Flask app 
app = Flask(__name__) 

#recommendation result 
@app.route('/recommendation',methods=['GET'])

def recommendation(interests):
    user_skills = request.json
    lemma_skills = set()
    for skill in user_skills:
        lemma_skills.add(lemma(skill).lower())
    recommendation = set()
    for i in range(1,data.shape[0]):
        sent =nltk.word_tokenize(data['preprocessed'][i])
        
        for word in sent: 
            if word in lemma_skills:
                recommendation.add(data[data.index== i-1]['name'].values[0])

    recommendation = tuple(recommendation)
    return json.dumps(recommendation), 201
  
if __name__ == '__main__':
    data=pd.read_json('clubs_preprocessed.json')
    print('Server Started...')
    app.run(host='0.0.0.0')
