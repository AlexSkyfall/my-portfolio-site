from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            logging.warning("Некорректные данные: %s", data)
            return jsonify({'error': 'Все поля обязательны!'}), 400

        logging.info("Сообщение получено: %s", data)
        return jsonify({'success': 'Сообщение отправлено!'}), 200
    except Exception as e:
        logging.error("Ошибка сервера: %s", str(e))
        return jsonify({'error': 'Произошла ошибка на сервере'}), 500

if __name__ == '__main__':
    app.run(debug=True)
