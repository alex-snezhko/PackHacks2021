from Manager import Manager
# from User import User
# from Organization import Organization
# from Event import Event
import json
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from flask_cors import CORS
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet
import nltk
import pandas as pd

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

app = Flask(__name__, static_folder='./build', static_url_path='/')
CORS(app)

man = Manager()

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/login", methods=["POST"])
def login():
    if request.is_json:
        login_data = request.get_json()
        print(login_data)
        current_user = man.login(login_data['username'], login_data['password'])
        if current_user is not None:
            return jsonify(**{'result': 200, 'data': {'message': 'login successful', 'current_user': login_data['username']}})
        else:
            return jsonify(**{'result': 400, 'data': {'message': 'invalid username or password'}})
    else:
        return jsonify(**{'result': 400, 'data': {'message': 'request was not json'}})
    

@app.route("/register", methods=["POST"])
def register():
    # Check if username already exists
    # If it is, then dont make a new account
    # Otherwise, create the new user and send them back to login
    if request.is_json:
        user_data = request.get_json()
        print(user_data)

        if man.getUserByName(user_data["username"]) is None:
            # user = User(user_data["username"], user_data["password"])
            user = {'username': user_data["username"], 'password': user_data["password"], 'department': None, 'interests': [] }
            man.users.append(user)
            man.save()
            return jsonify(**{'result': 200, 'data': {'message': 'user successfully registered'}})
        else:
            return jsonify(**{'result': 400, 'data': {'message': 'username already exists'}})
    else:
        return jsonify(**{'result': 400, 'data': {'message': 'request was not json'}})

# @app.route("/logout", methods=["POST"])
# def logout():
#     current_user = None
#     return jsonify(**{'result': 200, 'data': {'message': 'logout success'}})

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

@app.route("/recommendedOrganizations/<username>", methods=["GET"])
def getRecommendedOrgs(username):

    user = man.getUserByName(username)
    user_skills = user['interests']
    lemma_skills = set()
    for skill in user_skills:
        lemma_skills.add(lemma(skill).lower())
    recommendation = set()
    image = set()
    for i in range(1,data_clubs.shape[0]):
        sent =nltk.word_tokenize(data_clubs['preprocessed'][i])

        for word in sent: 
            if word in lemma_skills:
                recommendation.add(i)

    res = []
    for i, idx in enumerate(recommendation):
        res.append({ 'name': data_clubs[data_clubs.index== idx]['name'].values[0], 'description':data_clubs[data_clubs.index== idx]['desc'].values[0],
                'link':data_clubs[data_clubs.index== idx]['link'].values[0],'img':data_clubs[data_clubs.index== idx]['img'].values[0]})

    return jsonify(**{'result': 200, 'data': res})
    # return json.dumps(res), 201
    # return man.getUserByName(username).getRecommendedOrganizations()

@app.route("/recommendedEvents/<username>", methods=["GET"])
def getRecommendedEvents(username):
    user = man.getUserByName(username)
    user_skills = user['interests']
    lemma_skills = set()
    for skill in user_skills:
        lemma_skills.add(lemma(skill).lower())
    recommendation = set()
    image = set()
    for i in range(1,data_events.shape[0]):
        sent =nltk.word_tokenize(data_events['preprocessed'][i])

        for word in sent: 
            if word in lemma_skills:
                recommendation.add(i)

    res = []
    for i, idx in enumerate(recommendation):
        res.append({ 'name': data_events[data_events.index== idx]['name'].values[0], 'description':data_events[data_events.index== idx]['desc'].values[0],
                'link':data_events[data_events.index== idx]['link'].values[0],'img':data_events[data_events.index== idx]['img'].values[0],'time':data_events[data_events.index== idx]['time'].values[0], 'loc':data_events[data_events.index== idx]['loc'].values[0] })

    # return json.dumps(res), 201
    return jsonify(**{'result': 200, 'data': res})
    # return man.getUserByName(username).getRecommendedEvents()

@app.route("/searchOrganizations/<search_query>", methods=["GET"])
def getSearchedOrganizations(search_query):
    # user = man.getUserByName(username)
    user_skills = [search_query]
    lemma_skills = set()
    for skill in user_skills:
        lemma_skills.add(lemma(skill).lower())
    recommendation = set()
    image = set()
    for i in range(1,data_clubs.shape[0]):
        sent =nltk.word_tokenize(data_clubs['preprocessed'][i])

        for word in sent: 
            if word in lemma_skills:
                recommendation.add(i)

    res = []
    for i, idx in enumerate(recommendation):
        res.append({ 'name': data_clubs[data_clubs.index== idx]['name'].values[0], 'description':data_clubs[data_clubs.index== idx]['desc'].values[0],
                'link':data_clubs[data_clubs.index== idx]['link'].values[0],'img':data_clubs[data_clubs.index== idx]['img'].values[0]})

    return jsonify(**{'result': 200, 'data': res})

@app.route("/searchOrganizationsAll", methods=["GET"])
def getSearchedOrganizationsAll():
    # user = man.getUserByName(username)
    user_skills = []
    lemma_skills = set()
    for skill in user_skills:
        lemma_skills.add(lemma(skill).lower())
    recommendation = set()
    image = set()
    for i in range(1,data_clubs.shape[0]):
        sent =nltk.word_tokenize(data_clubs['preprocessed'][i])

        for word in sent: 
            recommendation.add(i)

    res = []
    for i, idx in enumerate(recommendation):
        res.append({ 'name': data_clubs[data_clubs.index== idx]['name'].values[0], 'description':data_clubs[data_clubs.index== idx]['desc'].values[0],
                'link':data_clubs[data_clubs.index== idx]['link'].values[0],'img':data_clubs[data_clubs.index== idx]['img'].values[0]})

    return jsonify(**{'result': 200, 'data': res})

@app.route("/searchEvents/<search_query>", methods=["GET"])
def getSearchedEvents(search_query):
    # user = man.getUserByName(username)
    user_skills = [search_query]
    lemma_skills = set()
    for skill in user_skills:
        lemma_skills.add(lemma(skill).lower())
    recommendation = set()
    image = set()
    for i in range(1,data_events.shape[0]):
        sent =nltk.word_tokenize(data_events['preprocessed'][i])

        for word in sent: 
            if word in lemma_skills:
                recommendation.add(i)

    res = []
    for i, idx in enumerate(recommendation):
        res.append({ 'name': data_events[data_events.index== idx]['name'].values[0], 'description':data_events[data_events.index== idx]['desc'].values[0],
                'link':data_events[data_events.index== idx]['link'].values[0],'img':data_events[data_events.index== idx]['img'].values[0],'time':data_events[data_events.index== idx]['time'].values[0], 'loc':data_events[data_events.index== idx]['loc'].values[0] })

    # return json.dumps(res), 201
    return jsonify(**{'result': 200, 'data': res})

@app.route("/searchEventsAll", methods=["GET"])
def getSearchedEventsAll():
    # user = man.getUserByName(username)
    user_skills = []
    lemma_skills = set()
    for skill in user_skills:
        lemma_skills.add(lemma(skill).lower())
    recommendation = set()
    image = set()
    for i in range(1,data_events.shape[0]):
        sent =nltk.word_tokenize(data_events['preprocessed'][i])

        for word in sent: 
            # if word in lemma_skills:
                recommendation.add(i)

    res = []
    for i, idx in enumerate(recommendation):
        res.append({ 'name': data_events[data_events.index== idx]['name'].values[0], 'description':data_events[data_events.index== idx]['desc'].values[0],
                'link':data_events[data_events.index== idx]['link'].values[0],'img':data_events[data_events.index== idx]['img'].values[0],'time':data_events[data_events.index== idx]['time'].values[0], 'loc':data_events[data_events.index== idx]['loc'].values[0] })

    # return json.dumps(res), 201
    return jsonify(**{'result': 200, 'data': res})

@app.route("/setUserInfo/<username>", methods=["POST"])
def setUserInfo(username):
    if request.is_json:
        user_data = request.get_json()

        user = man.getUserByName(username)
        if user is not None:
            # TODO this might not work the way I intend it to
            user['interests'] = user_data['interests']
            user['department'] = user_data['department']
            man.save()
            return jsonify(**{'result': 200, 'data': {'message': 'user successfully registered'}})
        else:
            return jsonify(**{'result': 400, 'data': {'message': 'username does not exist'}})
    else:
        return jsonify(**{'result': 400, 'data': {'message': 'request was not json'}})
    

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

data_events=pd.read_json('events_preprocessed.json')
data_clubs=pd.read_json('clubs_preprocessed.json')
if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
    app.run()