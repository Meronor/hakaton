from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Файл в папке проекта
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    last_login = db.Column(db.DateTime)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

with app.app_context():
    db.create_all()

users = {}

@app.route('/')  # Главная страница
def home():
    return render_template('index.html')

@app.route('/naviga')  # Главная страница
def naviga():
    return render_template('naviga.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')

        # Валидация данных
        if not email or '@' not in email:
            flash('Пожалуйста, введите корректный email', 'error')
            return redirect(url_for('register'))

        if not password or len(password) < 8:
            flash('Пароль должен содержать минимум 8 символов', 'error')
            return redirect(url_for('register'))

        if password != password_confirm:
            flash('Пароли не совпадают', 'error')
            return redirect(url_for('register'))

        if email in users:
            flash('Пользователь с таким email уже существует', 'error')
            return redirect(url_for('register'))

        # Хеширование пароля и сохранение пользователя
        users[email] = {
            'password': generate_password_hash(password),
            'email': email
        }

        flash('Регистрация прошла успешно!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
