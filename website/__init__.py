from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='ifidefidj ijdfidjfijd' # To encrypt the cookies/ secure data 

    return app

