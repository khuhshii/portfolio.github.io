from flask import Flask,render_template,request,send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__,template_folder="Self Portfolio")


@app.route("/")
def home():
    return send_file('index.html')

@app.route("/about")
def about():
    return send_file('about.html')

@app.route("/contact")
def contact():
    return send_file('contact.html')

@app.route("/proj")
def proj():
    return send_file('proj.html')

@app.route("/resume")
def resume():
    return send_file('resume.html')


if __name__=="__main__":
    app.run(debug=True)