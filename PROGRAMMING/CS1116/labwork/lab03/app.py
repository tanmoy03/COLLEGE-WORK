from flask import Flask, render_template
from forms import ShiftForm, ConversionForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

@app.route("/shift", methods=["GET", "POST"])
def shift():
    form = ShiftForm()

    if form.validate_on_submit():
        
        plaintext = form.plaintext.data
        shift = form.shift.data

        
        shift = int(shift)
        ciphertext = ""

        for char in plaintext:
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                ciphertext += char
        
        form.ciphertext.data = ciphertext

        return render_template("shift_form.html", form=form, ciphertext=ciphertext)

    return render_template("shift_form.html", form=form)
        
@app.route("/conversion", methods=["GET", "POST"])
def conversion():
    form = ConversionForm()
    if form.validate_on_submit():
        before = form.before.data
        tempbefore = form.tempbefore.data
        after = form.after.data

        if before == "Farenheit":
            if after == "Celsius":
                tempafter = (5/9) * (int(tempbefore) - 32)
            elif after == "Kelvin":
                tempafter = (5/9) * (int(tempbefore) - 32) + 273
            else:
                tempafter=tempbefore
        
        elif before == "Celsius":
            if after == "Farenheit":
                tempafter = (9/5) * int(tempbefore) + 32
            elif after == "Kelvin":
                tempafter = tempbefore + 273
            else: 
                tempafter=tempbefore
        
        elif before == "Kelvin":
            if after == "Farenheit":
                tempafter = (9/5) * (int(tempbefore) - 273) + 32
            elif after == "Celsius":
                tempafter = tempbefore - 273
            else:
                tempafter=tempbefore
        
        print(tempafter)
        form.tempafter.data = tempafter

    return render_template("conversion_form.html", form=form)