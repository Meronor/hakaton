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

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)  # Хешируем пароль

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


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
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')

        # Валидация данных
        if username and email:
            if not email or '@' not in email:
                flash('Пожалуйста, введите корректный email', 'error')
                return redirect(url_for('register'))

            if not password or len(password) < 8:
                flash('Пароль должен содержать минимум 8 символов', 'error')
                return redirect(url_for('register'))

            if password != password_confirm:
                flash('Пароли не совпадают', 'error')
                return redirect(url_for('register'))

            if email in [user.email for user in users] or username in [user.username for user in User.query.all()]:
                flash('Пользователь с таким login/email уже существует', 'error')
                return redirect(url_for('register'))

            try:
                new_user = User(
                    username=username,
                    email=email,
                    password=generate_password_hash(password),
                )

                db.session.add(new_user)
                db.session.commit()

            except Exception as e:
                db.session.rollback()
                return {'error': f'Ошибка при регистрации: {str(e)}'}, 500

            flash('Регистрация прошла успешно!', 'success')

            return redirect(url_for('home'))

        if (email in [user.email for user in users] or
                username in [user.username for user in User.query.all()]):
            user = User.query.filter_by(username=username).first()
            if user.check_password(password):
                flash('Вы успешно вошли!', 'success')
                return redirect(url_for('home'))

        return redirect(url_for('home'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
