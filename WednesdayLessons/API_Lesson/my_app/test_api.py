import requests
from flask import Flask, render_template, request

app = Flask("MyAPITest")

def send_simple_message(email):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org/messages",
        auth=("api", "key-95930168696abf549f49037e039116e0"),
        data={"from": "Doppleganger <mailgun@sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org>",
              "to": [email],
              "subject": "I know you",
              "text": "Because I am you!"})

@app.route("/")
def new_form():
    return render_template("new_form.html")

@app.route("/sendmessage", methods=["POST"])
def sign_up():
    form_data = request.form
    email = form_data["email"]
    send_simple_message(email)
    return "All OK!"

app.run(debug=True)



# send_simple_message()
