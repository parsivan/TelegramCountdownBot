from flask import Flask, redirect
import git

app = Flask(__name__)

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('/home/parsivan/TelegramCountdownBot')
    origin = repo.remotes.origin
    origin.pull()  # pulls the currently checked-out branch (pythonanywhere)
    return '', 200


@app.route('/')
def share_bot():
    return redirect("https://t.me/CountdownTimeKeeperBot")
