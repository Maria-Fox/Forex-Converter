from flask import Flask, Response, jsonify, make_response, redirect, render_template, session, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
import datetime
# datetime used for currency rate to pull day rate

app = Flask (__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
# enables the flask session cookies 
3
debug = DebugToolbarExtension(app)

# substantiate an instance of the CurrencyRates class
c_rates = CurrencyRates()
c_codes = CurrencyCodes()
date_obj = datetime.datetime.now()

api_route_rate = "https://theforexapi.com/api/latest HTTP/2"


# print(f"**********************{c_codes}***********************")


# contains year, month, dat,hour,,minute, second, and microsecond

@app.route("/home")
def viewHome():
  return render_template("/index.html")


@app.route("/https://theforexapi.com/api/latest/base=<base>/symbols=<symbols>HTTP/2" )
# https://theforexapi.com/api/latest?base=USD&symbols=GBP HTTP/2
def submit_form(base, symbols):
  # grab form input
  base = request.args["con-from"].upper()
  symbols = request.args["con-to"].upper()
  amount = float(request.args["amount"])
  amount_type = type(amount)
  print(f"***********************************type{amount_type}")
  print(f"***********************************type{symbols}")
  currency_types= ["USD", "EUR", "JPY", "GBP", "IDR", "BGN", "ILS", "DKK", "CAD", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"]



  return render_template("index.html", amount=amount, base =base, symbols= symbols, conversion_rate=conversion_rate, converted_amount=converted_amount, currency_symbol = currency_symbol)

  

  # if amount_type is type(str):
  #     conversion_rate = None
  #     converted_amount = None
  #     currency_symbol = None
  #     flash("Please include a valid amount greater than 0.") 
  # elif base and symbols not in currency_types:
  #     conversion_rate = None
  #     converted_amount = None
  #     currency_symbol = None
  #     flash("Please ensure currency types from and to are valid.")
  # else:
  #     flash("Else ran.")
  #     conversion_rate = c_rates.get_rate(base, symbols)
  #     converted_amount = c_rates.convert(base,symbols, amount)
  #     currency_symbol= c_codes.get_symbol(symbols)


# this worked
  # if symbols and base not in currency_types:
  #     conversion_rate = None
  #     converted_amount = None
  #     currency_symbol = None
  #     from_symbol = None
  #     flash("Please ensure currency codes entered are valid.")
  # elif amount.isdigit() == False:
  #     conversion_rate = None
  #     converted_amount = None
  #     currency_symbol = None
  #     from_symbol = None
  #     flash("Please include a valid amount greater than 0.")  
  # else:
  #     flash("Else ran.")
  #     float_amount = float(request.args["amount"])
  #     conversion_rate = c_rates.get_rate(base, symbols)
  #     converted_amount = c_rates.convert(base,symbols, float_amount)
  #     currency_symbol= c_codes.get_symbol(symbols)
  #     from_symbol = c_codes.get_symbol(base)


    # elif isinstance(amount_type,str) == True
    # elif amount.isdigit() == False:
# only works on whole numbers
    # try:
    #     amount = float(request.form['amount'])
    # except:
    #     flash("Not a valid amount")


  #    if base not in currency_types and symbols not in currency_types:
  #     conversion_rate = None
  #     converted_amount = None
  #     currency_symbol = None
  #     flash("Please ensure currency types from and to are valid.")
  # elif isinstance(amount,str):
  #     conversion_rate = None
  #     converted_amount = None
  #     currency_symbol = None
  #     flash("Please include a valid amount greater than 0.") 
  # else:
  #     flash("Else ran.")
  #     conversion_rate = c_rates.get_rate(base, symbols)
  #     converted_amount = c_rates.convert(base,symbols, amount)
  #     converted_amount = round(converted_amount, 2)
  #     currency_symbol= c_codes.get_symbol(symbols)