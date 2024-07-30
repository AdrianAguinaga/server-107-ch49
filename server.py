from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

@app.get("/about")
def about():
    return "this is the about page rules"
    

@app.get("/login")
def login():
    return "plase provide your credentials"

app.run(debug=True)