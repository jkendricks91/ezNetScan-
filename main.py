from flask import Flask, render_template, request, redirect, flash
from netscanner import ping_scan

app = Flask(__name__)

app.secret_key = 'enter-secret-key-here'

USERS = {
    "username": "password"
}


@app.route('/')
def index():
    return redirect('/login')


@app.route('/scanner', methods=['GET', 'POST'])
def scanner():
    output = ""

    if request.method == 'POST':
        prefix = request.form.get('prefix')

        # Basic validation
        if prefix:
            output, _ = ping_scan(prefix, 1, 254)
        else:
            output = "Please enter a valid network prefix."

    return render_template('index.html', output=output)

@app.route("/login", methods=["GET", "POST"])
def login():
    global current_user

    if request.method == "POST":
        try:
            user_var = request.form.get('username')
            pass_var = request.form.get('password')

            if user_var in USERS and USERS[user_var] == pass_var:
                current_user = user_var
                return redirect('/scanner')
            else:
                flash('Login error', 'error')
                return redirect('/login')
            
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    
    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)
