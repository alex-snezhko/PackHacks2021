from Manager import Manager
from User import User
from Organization import Organization
from Event import Event
import json
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

man = Manager()

@app.route("/")
def index():
    return "/login"

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

        if man.getUserByName(user_data["username"]) is None:
            user = User(user_data["username"], user_data["password"])
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

@app.route("/recommendedOrganizations/<username>", methods=["GET"])
def getRecommendedOrgs(username):
    return man.getUserByName(username).getRecommendedOrganizations()

@app.route("/recommendedEvents/<username>", methods=["GET"])
def getRecommendedEvents(username):
    return man.getUserByName(username).getRecommendedEvents()

@app.route("/searchOrganizations/<search_query>", methods=["GET"])
def getSearchedOrganizations(search_query):
    # **************************
    # TODO it seems that there is an issue serializing the model classes (Event, Organization, User). Figure out how to do this.
    # **************************


    # TODO return all organizations that reasonably match search query
    pass

@app.route("/searchEvents/<search_query>", methods=["GET"])
def getSearchedEvents(search_query):
    # TODO return all events that reasonably match search query
    pass

@app.route("/setUserInfo/<username>", methods=["POST"])
def setUserInfo(username):
    if request.is_json:
        user_data = request.get_json()

        user = man.getUserByName(username)
        if user is not None:
            # TODO this might not work the way I intend it to
            user.interests = user_data['interests']
            user.department = user_data['department']
            man.save()
            return jsonify(**{'result': 200, 'data': {'message': 'user successfully registered'}})
        else:
            return jsonify(**{'result': 400, 'data': {'message': 'username does not exist'}})
    else:
        return jsonify(**{'result': 400, 'data': {'message': 'request was not json'}})


if __name__ == "__main__":
    app.run(ssl_context='adhoc')