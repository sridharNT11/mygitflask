from flask import app, request, Blueprint, jsonify, redirect, url_for,flash, render_template, session
from core.library.route_group import RouteGroup
from core.model.UserModel import UserModel
from .. import Helper,Cryptography

from core.library.sms import SMS
from core.library.email import EMAIL

app = Blueprint('user', __name__)


@app.route('/')
def index():
	return 'index page'


@app.route('/home')
def home():
	return "welcome home page"
