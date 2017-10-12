from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    a = form_data["email"]
    print a
    return "All OK! We'll get in touch via " + a

app.run(debug=True)
