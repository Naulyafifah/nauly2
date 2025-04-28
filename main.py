from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def gate():
    return render_template('login.html')

@app.route('/dashboard/<name>')
def dashboard(name):
    return render_template('main.html', nama=name)

@app.route('/form_login', methods=['POST'])
def from_login():
    input_user = request.form.get('username')
    return redirect(url_for('dashboard', name=input_user))

if __name__ == "__main__":    
    app.run(debug=True,port=3030)
