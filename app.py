from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None

    # Если отправили форму (POST), считаем
    if request.method == 'POST':
        try:
            a = float(request.form.get('a', 0))
            b = float(request.form.get('b', 0))
            op = request.form.get('op', '+')

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                if b == 0:
                    error = "На ноль делить нельзя!"
                else:
                    result = a / b
        except ValueError:
            error = "Вводи только числа!"

    # HTML с формой и результатом
    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Локальный калькулятор</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #1a1a2e;
                color: #ffffff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background: #16213e;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
                width: 320px;
            }}
            h2 {{
                color: #4cc9f0;
                text-align: center;
                margin-bottom: 20px;
            }}
            input, select {{
                width: 100%;
                padding: 10px;
                margin: 8px 0;
                border-radius: 6px;
                border: 1px solid #333;
                box-sizing: border-box;
            }}
            button {{
                width: 100%;
                padding: 12px;
                background-color: #4cc9f0;
                color: #000;
                border: none;
                border-radius: 6px;
                font-weight: bold;
                cursor: pointer;
            }}
            button:hover {{
                background-color: #3bb0d8;
            }}
            .result {{
                margin-top: 20px;
                text-align: center;
                font-size: 1.2em;
                color: #f0f0f0;
            }}
            .error {{
                color: #ff6b6b;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Калькулятор</h2>
            <form method="POST">
                <input type="number" step="any" name="a" placeholder="Первое число" required>
                <select name="op">
                    <option value="+">+</option>
                    <option value="-">-</option>
                    <option value="*">×</option>
                    <option value="/">÷</option>
                </select>
                <input type="number" step="any" name="b" placeholder="Второе число" required>
                <button type="submit">Посчитать</button>
            </form>

            <div class="result">
                {f"Результат: {result}" if result is not None else ""}
                {f"<span class='error'>{error}</span>" if error else ""}
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
