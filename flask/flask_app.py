# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import git

app = Flask(__name__)

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./orbe')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

@app.route('/')
def hello_world():
    return 'Hello from Flask!'