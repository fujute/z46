from flask import Flask
import dateime

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    print ("Azure TechKnight 26-Nov-2020", now)
    myText = "Hello, Azure " + now.strftime("%X")
    return myText
