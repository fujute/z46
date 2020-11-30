from flask import Flask
from flask import render_template
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    print ("Azure TechKnight 26-Nov-2020", now)
    userName = "Azure TechKnight : " + now.strftime("%X")
    return render_template('index.html', title='Welcome', username=userName)