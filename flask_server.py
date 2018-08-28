from flask import Flask
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    json_obj = {"hello":"flask!"}
    return json.dumps(json_obj)

@app.route('/hello')
def hello():
    return 'Hello,World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def sgow_subpath(subpath):
    return 'Subpath %s' % subpath
