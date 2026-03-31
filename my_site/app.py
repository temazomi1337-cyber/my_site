from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Мій сайт</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background: #1e1e2f;
            color: white;
        }
        nav a {
            margin: 10px;
            color: #00ffcc;
            text-decoration: none;
        }
        input {
            padding: 10px;
            border-radius: 5px;
            border: none;
        }
        button {
            padding: 10px;
            border: none;
            background: #00ffcc;
            cursor: pointer;
        }
        .msg {
            margin-top: 20px;
            color: yellow;
        }
    </style>
</head>
<body>

    <h1>🚀 Мій сайт на Python</h1>

    <nav>
        <a href="/">Головна</a>
        <a href="/about">Про сайт</a>
    </nav>

    <h2>Форма</h2>

    <form method="POST">
        <input type="text" name="name" placeholder="Введи своє ім'я" required>
        <button type="submit">Надіслати</button>
    </form>

    {% if message %}
        <p class="msg">{{ message }}</p>
    {% endif %}

</body>
</html>
"""

about_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Про сайт</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background: #1e1e2f;
            color: white;
        }
        a {
            color: #00ffcc;
        }
    </style>
</head>
<body>

    <h1>Про цей сайт</h1>
    <a href="/">Назад</a>

    <p>Цей сайт зроблений на Python Flask 😎</p>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        message = f"Привіт, {name}! Раді бачити тебе 😎"
    return render_template_string(html, message=message)

@app.route("/about")
def about():
    return render_template_string(about_html)

if __name__ == "__main__":
    app.run(debug=True)