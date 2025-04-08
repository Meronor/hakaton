from flask import Flask, request, render_template, redirect, url_for, flash
from instance.set import set_user
from instance.get import get_password

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'


@app.route('/')  # Главная страница
def home():
    return render_template('index.html')


@app.route('/naviga')  # Главная страница
def naviga():
    return render_template('naviga.html')


@app.route('/doc')  # Главная страница
def doc():
    return render_template('doc.html')


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

            if not password or len(password) < 7:
                flash('Пароль должен содержать минимум 8 символов', 'error')
                return redirect(url_for('register'))

            if password != password_confirm:
                flash('Пароли не совпадают', 'error')
                return redirect(url_for('register'))

            if set_user(username, email, password):
                flash('Регистрация прошла успешно!', 'success')
                print("nice")
                return redirect(url_for('home'))
            else:
                print('error')
                flash('Пользователь с таким login/email уже существует', 'error')
                return redirect(url_for('register'))
        else:
            if password == get_password(email):
                flash('Авторизация прошла успешно!', 'success')
                return redirect(url_for('home'))
            else:
                print(password, get_password(email))
                flash('Неверный логин/пароль', 'error')
                return redirect(url_for('register'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
