from flask import render_template
from app import app
from random import randint

@app.route("/")
def index():
  return "Hello"
