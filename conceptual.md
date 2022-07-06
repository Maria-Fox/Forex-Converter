### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Some important differences b/w Python and JS are object-types (lists/arrays, how to grab dictionary items, etc.). Comparison types, and basic syntax for functions, loops, etc.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

<!-- spacing is off but the file is changing it upon save -->

if dict["c"]:
return dict["c"]

if c in dict:
return dict["c"]

dict.get("c",["there's no c"])

<!-- default if key does not exist -->

if c in dict.keys():
print("It exists")
else:
"it does not exist"

- What is a unit test?

A unit test is a single function/method examination testing whether or not the operation/goal of the function/method is working correctly. This function/method is run against multiple tests to confirm the source code is ready for use. It does not incorporate integration.

- What is an integration test?

An integration test is testing whether multiple functinos/methods interact with one another correctly. Run against various tests to ensure the source code is connecting with one another and ready for use.

- What is the role of web application framework, like Flask?

A web application framework, such as Flask allows for simple, and quick developments from the browser to the API. A framework has many built in modules and methods to allow for a quick compiling of the web pages, and response headers. This allows for a standard way to support/build and deploy web applications on the WWW.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from a URL placeholder parameter using Flask?

Using Flask, you can collect data from a URL placeholder parameter by pulling the input through a query string. From there, you can use AXIOS to complete a request to the API and pass in the input value.

<!-- grab in JS page, pass into route as <param>, pass into view function w/ o <> -->

EX: @app.route("/home/<scoreId>)
def view_function(scoreId):
return view function response

- How do you collect data from the query string using Flask?

To collect the data from flask we need to add, "From flask import request". Then, we can request the info using:

@app.route('/data')
def data(): # here we want to get the value of user (i.e. ?user=some-value)
user = request.args.get('user')

<!-- the above gives you the actual value of string/ param being passed in -->

  <!-- if you want just the string itself: -->

return request.query_string

- How do you collect data from the body of the request using Flask?

Using Flask, you can collect data from the body of the request by cerating a key/value dictionairy. For ex:

from flask import request

form: request.form["name"], URL query params: request.args.get("search-item")

return jsonify({"result: {variable_name}})

OR SIMPLY REQUEST.DATA

The front end would then use the response.data.result to pull the infromation necessary.

- What is a cookie and what kinds of things are they commonly used for?

A cookie is a broswer centered form of keeping key/values pair data pieces on your computer. Cookies are commnly used for keeping window session preferences, items in carts, etc.

- What is the session object in Flask?

The session item in Flask is a key/value pair used to store data in the API. This allows the front end to communicate to the back-end and request/ hold pertinant information.

- What does Flask's `jsonify()` do?

Flask's 'jsonify()' turns the input within the parens into JSON allowing the item being transfered to be the correct JSON syntax and then able to be parsed from JS or any other language. Method returns a response object.
