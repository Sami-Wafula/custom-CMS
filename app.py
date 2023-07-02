
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
	pass

@login_manager.user_loader
def user_loader(username):
	if username not in users:
		return None

	user = User()
	user.id = username
	return user

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		if users.get('username') and users[username]['password'] == password:
			user = User()
			user.id = username
			login_user(user)
			return redirect(url_for('admin'))

	return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/admin')
@login_required
def admin():
	return render_template('admin.html')

if __name__ == '__main__':
	app.run()
