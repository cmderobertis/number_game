from flask import Flask, render_template, session, request, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'hello hi what is going on here'


@app.route('/')
def index():
    if not 'number' in session:
        session['number'] = random.randint(1, 100)
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    num = session['number']
    session['guess'] = request.form['guess']
    guess = int(session['guess'])
    if guess > num:
        session['response'] = 'too high'
        return redirect('/')
    elif guess < num:
        session['response'] = 'too low'
        return redirect('/')
    else:
        session['response'] = 'correct'
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
