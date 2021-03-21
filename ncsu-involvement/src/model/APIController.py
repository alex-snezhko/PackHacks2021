from Manager import Manager
from User import User
from Organization import Organization
from Event import Event
import json
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify

app = Flask(__name__)
current_user = None

@app.route("/")
def index():
    return "/login"

@app.route("/login", methods=["POST"])
def login():
    if request.is_json:
        req = request.get_json()
        login_data = json.loads(req)
        current_user = Manager.login(login_data['username'], login_data['password'])
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
        req = request.get_json()
        user_data = json.loads(req)
        
        if Manager.getUserByName(user_data["username"]) is None:
            user = User(user_data["username"], user_data["password"], user_data["majors"], user_data["minors"], user_data["interests"], user_data["organizations"])
            Manager.users.append(user)
            Manager.save()
            return jsonify(**{'result': 200, 'data': {'message': 'user successfully registered'}})
        else:
            return jsonify(**{'result': 400, 'data': {'message': 'username already exists'}})
    else:
            return jsonify(**{'result': 400, 'data': {'message': 'request was not json'}})

@app.route("/logout", methods=["POST"])
def logout():
    current_user = None
    return jsonify(**{'result': 200, 'data': {'message': 'logout success'}})

@app.route("/getinvolved/organizations/<username>", methods=["GET"])
def getRecommendedOrgs(username):
    return Manager.getUserByName(username).getRecommendedOrganizations()

@app.route("/getinvolved/events/<username>", methods=["GET"])
def getRecommendedEvents(username):
    return Manager.getUserByName(username).getRecommendedEvents()