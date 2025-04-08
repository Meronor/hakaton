from flask import Flask, request, render_template

app = Flask(__name__)


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
        # Здесь вы можете обработать email и password, например, сохранить их в базе данных
        print(f'Email: {email}, Password: {password}')
        return f'Email: {email}, Password: {password}'
    return render_template('pomosh.html')

if __name__ == '__main__':
    app.run(debug=True)
