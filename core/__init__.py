from flask import Flask, url_for, request ,redirect,render_template
# from flask_socketio import SocketIO, emit
# from flask_caching import Cache
import os, time
import datetime
from datetime import datetime as dt
import traceback
import logging

app = Flask(__name__,static_url_path='/static')


app.config.from_object('core.config.SECRET_KEY')
app.config.from_object('core.config.ProductionConfig')

# app.config["DEBUG"] = True
# print("app.config")
# print(app.config)

# print(datetime.datetime.now())

os.environ['TZ'] = app.config["TIMEZONE"]
time.tzset()


# print(datetime.datetime.now())

config = app.config
from core.library.cryptography import Cryptography
from core.library.helper import Helper
from core.model.Log import Log
from core.library.route_group import RouteGroup

current_app = app

from core.controller.UserController import app as user

app.register_blueprint(user, url_prefix='')




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 404


class SQLAlchemyHandler(logging.Handler):

    def emit(self, record):
        trace = None
        exc = record.__dict__['exc_info']
        if exc:
            trace = traceback.format_exc()

        path = request.path
        method = request.method
        ip = request.remote_addr    

        data = {
        		'url':path,
        		'logger_name':record.__dict__['name'],
                'level':record.__dict__['levelname'],
                'context':trace,
                'message':record.__dict__['msg'],
                'created_at':dt.now(),
                'ip_address':ip
            }    
        Log().insert(data)    
        return "Some thing went wrong while processing your request. Please try after sometime or get in touch with system administrator."

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = SQLAlchemyHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)



loggers = [logger, logging.getLogger('sqlalchemy'), logging.getLogger('flask.app')]

for l in loggers:
    l.addHandler(ch)


# @app.before_request
# def before_request():
#     if request.url.startswith('http://'):
#         print("http")
#         url = request.url.replace('http://', 'https://', 1)
#         code = 301
#         return redirect(url, code=code)
