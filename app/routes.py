from flask import render_template
from app import app
from random import randint

@app.route("/")
def index():
  return "Hello"

@app.route("/quotes")
def renderQuotes():
  quotes = {
    1: {
      "quote": "Be yourself; everyone else is already taken.", 
      "author": "Oscar Wilde", 
      "img": "_"
    },
    2: {
      "quote": "So many books, so little time.",
      "author": "Frank Zappa",
      "img": "_"  
    },
    3: {
      "quote": "Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.",
      "author": "Bernard M. Baruch",
      "img": "_"
    },
    4: {
      "quote": "You know you're in love when you can't fall asleep because reality is finally better than your dreams.",
      "author": "Dr. Seuss",
      "img": "_"
    },
    5: {
      "quote": "In three words I can sum up everything I've learned about life: it goes on.",
      "author": "Robert Frost",
      "img": "_"
    },
    6: {
      "quote": "To live is the rarest thing in the world. Most people exist, that is all.",
      "author": "Oscar Wilde",
      "img": "_"
    },
    7: {
      "quote": "Live as if you were to die tomorrow. Learn as if you were to live forever.",
      "author": "Mahatma Gandhi",
      "img": "_"
    },
    8: {
      "quote": "It is better to be hated for what you are than to be loved for what you are not.",
      "author": "Andre Gide",
      "img": "_"
    },
    9: {
      "quote": "Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.",
      "author": "Marilyn Monroe",
      "img": "_"
    },
    10: {
      "quote": "Good friends, good books, and a sleepy conscience: this is the ideal life.",
      "author": "Mark Twain",
      "img": "_"
    },
  }

  randomIdx = randint(1, 10)
  return render_template("index.html", age=13,  randomQuote=quotes[randomIdx])