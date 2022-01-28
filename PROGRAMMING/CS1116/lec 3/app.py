from flask import Flask, render_template

app = Flask(__name__)

@app.route("/greet_by_name/<name>")
def send_greeting_by_name(name):
    return render_template("greet1.html", name=name)

@app.route("/greet_across_the_world/<language>")
def send_greeting_in_language(language):
    hello_dict = {"en": "Hello", "fr": "Bonjour", "es": "Hola"}
    if language in hello_dict:
        greeting = hello_dict[language]
    else:
        greeting = "Hi"
    return render_template("greet2.html", greeting = greeting)

@app.route("/ciao")
@app.route("/adios/<name>")
@app.route("/au_revoir/<name>")
def send_parting_by_name(name= None):
    return render_template("bye.html", name=name)