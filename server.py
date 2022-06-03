from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html', count = session['count'])
    
@app.route('/add2', methods=['POST'])
def add2():
    session['count'] =  session['count']+1
    return redirect('/')

@app.route('/destroysession', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__": 
    app.run(debug=True)