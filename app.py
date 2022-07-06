from flask import Flask, redirect, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
import datetime

from convert import Converter_class

app = Flask (__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
# enables the flask session cookies 
debug = DebugToolbarExtension(app)

# substantiate an instance of Converter_class in refactor.py
sub_con_class= Converter_class()

@app.route("/home")
def viewHome():
  '''Navigates user to main page'''

  return render_template("index.html")


@app.route("/https://theforexapi.com/api/latest/base=<base>/symbols=<symbols>HTTP/2" )
def submit_form(base, symbols):
  '''Processes user input and returns conversion breakdown'''

  response = sub_con_class.submit_form(base, symbols)
  print(f"******************{response}")
  # the response if the full html page passing in the values

  return response
