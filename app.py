from flask import Flask, request, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from user import User

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def home():
    return 'Welcome! <a href="/login">Login</a> | <a href="/register">Register</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.authenticate(email, password)
        if user:
            login_user(user)
            return redirect(url_for('protected'))
        else:
            return 'Invalid login'
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/protected')
@login_required
def protected():
    return render_template('protected.html', email=current_user.email)

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Placeholder for registration logic
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
