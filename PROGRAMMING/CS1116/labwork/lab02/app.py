from flask import Flask, render_template, request

app = Flask(__name__)

# Problem 1
@app.route("/spy", methods=["GET","POST"])
def spy():
        if request.method == "GET":
            return render_template("spyform.html")
        else:
            given_name = request.form["given_name"]
            family_name = request.form["family_name"]

            return render_template("spyresponse.html", given_name = given_name, family_name=family_name)


# Problem 2
@app.route("/morse", methods=["GET","POST"])
def morse():
    if request.method == "GET":
        return render_template("morse_form.html")
    else:
        message = request.form["message"]
        cleaned_message = message.strip().upper()
        morse = ""
        morse_dict = {
            "A": ".-",
            "B": "-...",
            "C": "-.-",
            " ": "/"
        }

        if message == "":
            return render_template("morse_form.html", error="Error: no message entered. Enter a message")

        for char in message:
            if char not in morse_dict:
                return(render_template("morse_form.html", error="Error: character(s) not in Morse Dictionary. Try Again"))

        for char in cleaned_message:
            code = morse_dict[char]
            morse = morse + code + "   "
            
        return render_template("morse_response.html", message = message, morse = morse)

# Problem 3
@app.route("/lengths", methods=["GET","POST"])
def lengths():
    if request.method == "GET":
        return render_template("lengths_form.html")
    else:
        inches = request.form["inches"]
        cm = request.form["cm"]


        if inches == "" and cm == "":
            return render_template("lengths_form.html", error="Error: both fields left empty. Try again")

        if inches != "" and cm != "":
            return render_template("lengths_form.html", error="Error: enter either inches OR centimetres, not both. Try again")
        
        if inches != "" and cm == "":
            inches = float(inches)
            inchestocm = inches*2.54
            return render_template("lengths_form.html", cm=inchestocm)
            
        if inches == "" and cm != "":
            cm = float(cm)
            cmtoinches = cm/(2.54)
            return render_template("lengths_form.html", inches=cmtoinches)


        