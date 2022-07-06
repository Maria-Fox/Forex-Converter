from flask import Flask, redirect, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
import datetime

# c_rates = CurrencyRates()
# c_codes = CurrencyCodes()

class Converter_class:

  def __init__(self,CurrencyRates = CurrencyRates, CurrencyCodes = CurrencyCodes):
    self.c_rates = CurrencyRates()
    self.c_codes = CurrencyCodes()
    

  def submit_form(self, base, symbols):
      c_rates = CurrencyRates()
      c_codes = CurrencyCodes()
      base = request.args["con-from"].upper()
      symbols = request.args["con-to"].upper()
      amount = request.args["amount"]

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
          messages = flash("Please enter a valid currency code. To review the currency codes plasee scroll to the bottom of the page.")
          return render_template("index.html")

      except (ValueError, TypeError):
          flash("Please ensure the currency is correctly entered and the amount/ value submited is greater than 0.")
          return render_template("index.html", messages = messages)
