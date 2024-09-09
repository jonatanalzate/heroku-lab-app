from flask import Flask, request, jsonify

import os

app = Flask(__name__)

@app.route('/cedula', methods=['POST'])
def cedula():
    data = request.get_json()
    cedula = data.get('cedula')
    if cedula:
        return jsonify({"message": f"Recibimos la cédula: {cedula}"}), 200
    else:
        return jsonify({"error": "Por favor envía una cédula válida."}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)