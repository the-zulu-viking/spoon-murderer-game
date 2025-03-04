from flask import Flask, render_template, redirect, url_for, abort, request, g
import random as rd
import datetime as dt


app = Flask(__name__)

ts = dt.datetime.now()
players_list = ['Fenne', 'Henrik', 'Ingeborg', 'Lina', 'Mai', 'Malte', 'Maria', 'Pablo', 'Sven', 'Thijs', 'Tilly']

shuffled_list = players_list.copy()
rd.shuffle(shuffled_list)
print(ts)
print("This is the order" , shuffled_list)


@app.route("/")
def index():
        
    return render_template("index.html")
    

@app.route("/target" ,methods=["GET", "POST"])
def target():

    if request.method == 'POST':
        answer =  request.form
        member = answer.get('member')
        i = shuffled_list.index(member)

        if i <(len(players_list)-1):
            return render_template("thanks.html", target=shuffled_list[i+1] )
        elif i ==(len(players_list)-1):
            return render_template("thanks.html", target=shuffled_list[0] )
        else:
            abort
    
    return render_template("target.html", bud= players_list)

@app.route("/thanks" )
def thanks(target):
    
    return render_template("target.html" )

if __name__ == "__main__":
    app.run(debug=True)