from http import client
from flask import Flask, pytest
from unittest import TestCase
# from forex_python.converter import CurrencyRates, CurrencyCodesimport 
from convert import Converter_class
from app import app
# from app.py import @app.route("/")

class ConverterClassTestCase(TestCase):
  '''Testing the class'''

# test methods must start with "test_"

  def setUp(self):
    """Initiate before every test """

    self.client = app.test_client()
    app.config['TESTING'] = True

# initiated client in setUp
  def test_home_route(self):
      '''Test root directory status & response '''

      # make assertions/ tests here. Start with route test
      with self.client:
        response = client.get("/home")
        html = response.get_data(as_text=True)

# using TestCase methods imported and passed in as param
        self.assertEqual(response.status_code,200)
        self.assertIn("<h3>Currency Codes</h3>", response.data)

  def test_valid_submit_form(self):
      '''Test if user input is valid by running through the submit_form method'''

  # unsure if the get route here is correct bc it's a get request to API, but needs user input to be passed in. Alternative in nxt comment. 
      # with self.client as client:
      response = self.client.get('https:/theforexapi.com/api/latest/base%3D%3Cbase%3E/symbols%3D%3Csymbols%3EHTTP/2?con-from=usd&con-to=usd&amount=50')
      # response = self.client.post('/https://theforexapi.com/api/latest/base=<base>/symbols=<symbols>HTTP/2', data ={"base":"USD", "symbols": "usd", "amount": "1"})

      self.assertEqual(response.json["result"], "ok")
      self.assertIn('<h2 id="conversion-header">Conversion Breakdown:</h2>', response.data)
      self.assertEqual(Converter_class.submit_form("usd","usd"),"usd")
      # how do i pass in the amount?!
