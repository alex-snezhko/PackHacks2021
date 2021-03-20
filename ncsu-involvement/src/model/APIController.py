import Manager
import User
import Organization
import Event
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)
current_user = None

@app.route("/")
def index():
    if not session.get("logged_in"):
        return render_template("login.html")
    else:
        return render_template("getinvolved.html")

@app.route("/login", methods=["POST"])
def login():
    current_user = Manager.login(request.form['username'], request.form['password'])
    if current_user is not None:
        session['logged_in'] = True
    else:
        flash("invalid username/password")
    return index()

@app.route("/getinvolved/organizations/<username>", methods=["GET"])
def getRecommendedOrgs(username):
    return Manager.getUserByName(username).getRecommendedOrganizations()

@app.route("/getinvolved/events/<username>", methods=["GET"])
def getRecommendedEvents(username):
    return Manager.getUserByName(username).getRecommendedEvents()