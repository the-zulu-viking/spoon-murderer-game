from flask import Flask, render_template, redirect, url_for, abort, request, g
import random as rd
import datetime as dt


app = Flask(__name__)

ts = dt.datetime.now()
buddies_list = ['Fenne', 'Henrik', 'Ingeborg', 'Lina', 'Mai', 'Malte', 'Maria', 'Pablo', 'Sven', 'Thijs', 'Tilly']

buddies = ['Fenne', 'Henrik', 'Ingeborg', 'Lina', 'Mai', 'Malte', 'Maria', 'Pablo', 'Sven', 'Thijs', 'Tilly']
rd.shuffle(buddies)
print(ts)
print("This is the order" , buddies)


@app.route("/")
def index():
        
    return render_template("index.html")
    

@app.route("/target" ,methods=["GET", "POST"])
def target():

    if request.method == 'POST':
        answer =  request.form
        member = answer.get('member')
        i= buddies.index(member)

        if i <10:
            return render_template("thanks.html", target=buddies[i+1] )
        elif i ==10:
            return render_template("thanks.html", target=buddies[0] )
        else:
            abort
    
    return render_template("target.html",bud= buddies_list)

@app.route("/thanks" )
def thanks(target):
    
    return render_template("target.html" )

if __name__ == "__main__":
    app.run(debug=True)