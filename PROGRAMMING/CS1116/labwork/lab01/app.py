from flask import Flask, render_template

import random 

from random import randint

app = Flask(__name__)

# Problem 1 + Problem 2

@app.route("/rps/<player>")
def rps(player):
    list1 = ["rock", "paper", "scissors"]

    win = "Player wins!"
    lose = "Computer wins!"
    draw = "Its a draw"

    mychoice = random.choice(list1)
    player = player.lower()

    if player == "rock":
        if mychoice == "scissors":
            return render_template("rps.html", name=win,  mychoice=mychoice, player=player)
        elif mychoice == "paper":
            return render_template("rps.html", name=lose, mychoice=mychoice, player=player)
        else:
            return render_template("rps.html", name=draw, mychoice=mychoice, player=player)

    if player == "scissors":
        if mychoice == "rock":
            return render_template("rps.html", name=lose, mychoice=mychoice, player=player)
        elif mychoice == "paper":
            return render_template("rps.html", name=win, mychoice=mychoice, player=player)
        else: 
            return render_template("rps.html", name=draw, mychoice=mychoice, player=player)
    
    if player == "paper":
        if mychoice == "rock":
            return render_template("rps.html", name=win, mychoice=mychoice, player=player)
        elif mychoice == "scissors":
            return render_template("rps.html", name=lose, mychoice=mychoice, player=player)
        else: 
            return render_template("rps.html", name=draw, mychoice=mychoice, player=player)

# Problem 3: outputs one line of lotto numbers

# @app.route("/could_it_be_me")
# def send_lotto_numbers():
#     line = []

#     for i in range(0,6):
#         n = randint(0,47)
#         line.append(n)
        
#     return render_template("lotto.html", line=line)

# Problem 4
@app.route("/could_it_be_me/<int:num_lines>")
def send_lottery_numbers(num_lines):
    lines = []
    x = 1
    
    while num_lines >= x:
        line = []
        for i in range(0,6):
            n = randint(0,47)
            line.append(n)
        lines.append(line)
        x += 1

    return render_template("lotto.html", lines = lines)

