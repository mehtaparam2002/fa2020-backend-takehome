from flask import Flask, redirect

import random

app = Flask(__name__)

"""

TASK

Implement an endpoint `/api/fetch` that returns the contents of `data.csv` as JSON

1) Load/transcribe `data.csv`
2) Save each entry's full name, time zone, and department
3) Return the JSON data at the endpoint

"""

# your work here

import pandas as pd #used to read the CSV
from flask import jsonify, request

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True #formats the json file into the required format

df = pd.read_csv('data.csv') #reads the CSV and sets it to a varible
df['name'] = df['first_name'].map(str) + ' ' + df['last_name'].map(str)  #Concatenates the first name and last name column to one colum with the person's full name.
drop_columns = ['id', 'first_name', 'last_name']
df = df.drop(drop_columns, axis = 1) #drops the columns not needed to display

new_dict = df.to_dict(orient = 'records') #need to convert string to a dictionary as jsonify accepts a dictionary data type

@app.route('/api/fetch', methods=['GET']) #create the route for the backend
def makeJson():
    if request.method == 'GET': 
        return jsonify(new_dict)


"""

DOCUMENTATION WEBPAGE BELOW

"""


@app.route("/")
def redirect_to_api():
    return redirect("/api", code=301)

@app.route("/api")
def api_home():
    return """
        <style>
            body {
                font-family: sans-serif;
                max-width: 900px;
                width: 90%;
                margin: 0 auto 0 auto;
                padding: 5vh 30px 0 30px;
                background: rgb(240,240,240);
            }

            pre, code {
                background: #121212;
                color: white;
            }

            code {
                padding: 4px;
            }

            pre code {
                padding: 0;
            }

            pre {
                padding: 10px;
            }

            hr {
                margin: 2em 0;
            }
        </style>
        <h1>Founders Fall 2020 Backend Take-Home API</h1>
        <p>Add the endpoint <code>`/api/fetch`</code> accessible via a GET request which returns the list of employees from <code>`data.csv`</code> as JSON.</p><hr />
        <h2>API (to be implemented)</h2>
        <h4>Request</h4>
<pre><code><b>GET</b>
Scheme: http
Filename: /api/fetch</code></pre>
        <h4>Response</h4>
<pre><code>employees: [
            <br />  {
            <br />      name: <i>FULL NAME OF EMPLOYEE</i>,
            <br />      timezone: <i>TIMEZONE</i>,
            <br />      dept: <i>EMPLOYEE'S DEPARTMENT</i>,
            <br />  }
            <br />  ...
        <br />]</code></pre>"""
