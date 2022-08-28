from flask import render_template
from app import app

@app.route("/")
def index():
  user = {"username": "Ikromshi"}
  posts = [
    {
      "author": {"username": "John"}, 
      "body": "A beautiful day in Portland!"
    },
    { 
      "author": {"username": "Tony"}, 
      "body": "I like men's beard"}
  ]
  return render_template("index.html", age=13, title="Home",  posts=posts)