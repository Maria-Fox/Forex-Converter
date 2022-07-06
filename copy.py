from flask import Flask, redirect, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
import datetime
# datetime used for currency rate to pull day rate

app = Flask (__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
# enables the flask session cookies 
debug = DebugToolbarExtension(app)

# substantiate an instance of the CurrencyRates class
c_rates = CurrencyRates()
c_codes = CurrencyCodes()

@app.route("/home")
def viewHome():
  return render_template("/index.html")


@app.route("/https://theforexapi.com/api/latest/base=<base>/symbols=<symbols>HTTP/2" )
# https://theforexapi.com/api/latest?base=USD&symbols=GBP HTTP/2
def submit_form(base, symbols):
  # grab form input
  base = request.args["con-from"].upper()
  symbols = request.args["con-to"].upper()
  amount = request.args["amount"]

  # print(f"***********************************type{amount}")
  # print(f"***********************************type{base}")
  # print(f"***********************************type{symbols}")

  currency_types= ["EUR", "IDR", "BGN","ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR" ]

  try: 
      amount = float(request.args["amount"])
      conversion_rate = c_rates.get_rate(base, symbols)
      converted_amount = c_rates.convert(base,symbols, amount)
      converted_amount = round(converted_amount, 2)
      currency_symbol= c_codes.get_symbol(symbols)
      from_symbol = c_codes.get_symbol(base)

      return render_template("index.html", amount=amount, base =base, symbols= symbols, conversion_rate=conversion_rate, converted_amount=converted_amount, currency_symbol = currency_symbol, from_symbol = from_symbol)

# RatesNotAvailableError - specific error but API is down as of 220705
  except NameError:
        flash("Please enter a valid currency")

  except (ValueError, TypeError):
        flash("Oops something went wrong")
        # return redirect('/home')