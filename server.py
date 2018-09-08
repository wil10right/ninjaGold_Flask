#ninja_gold
from flask import Flask, session, redirect, render_template, request
import random, datetime
app=Flask(__name__)
app.secret_key="Sp@ghetti"

# start routes
@app.route('/')
def goldGame():
    if 'gold' not in session:
        session['gold'] = 0
    if 'actions' not in session:
        session['actions'] = []
    return render_template('index.html', x=session['gold'])

@app.route('/process_money', methods=['POST'])
def processMoney():
    print(request.form)
    now = str(datetime.datetime.now())
    if request.form['building'] == 'farm':
        session['num'] = random.randint(10,20)
        session['gold'] += session['num']
        session['actions'].insert(0, "<p style='color: green'>You found "+str(session['num'])+" gold in your Farm.  "+now+"</p>")

    if request.form['building'] == 'cave':
        session['num'] = random.randint(5,10)
        session['gold'] += session['num']
        session['actions'].insert(0, "<p style='color: green'>You found "+str(session['num'])+" gold in a dank Cave.  "+now+"</p>")

    if request.form['building'] == 'house':
        session['num'] = random.randint(2,5)
        session['gold'] += session['num']
        session['actions'].insert(0, "<p style='color: green'>You found "+str(session['num'])+" gold in your House.  "+now+"</p>")

    if request.form['building'] == 'casinos':
        session['num'] = random.randint(-50,50)
        if session['num'] > 0:
            session['gold'] += session['num']
            session['actions'].insert(0, "<p style='color: green'>You WON "+str(session['num'])+" at the Casino.  "+now+"</p>")
        if session['num'] <= 0:
            session['gold'] += session['num']
            session['actions'].insert(0, "<p style='color: red'>You LOST "+str(session['num']*-1)+" at the Casino.  "+now+"</p>")

    return redirect('/')

@app.route('/reset', methods=['POST'])
def resetSession():
    session.clear()
    return redirect('/')
# end routes
app.run(debug=True)